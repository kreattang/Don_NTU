#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 9:55
# @Author  : blvin.Don
# @File    : Contrast_Eight_UAVs.py


import turtle, copy
import random
import time
from math import fabs,degrees,atan,asin,sqrt,cos,sin
import numpy as np
from Contrast_exps.Get_distance import get_distance
from Contrast_exps.Get_Angle_TwoVec import Get_Angle_Between_Two_Vector
from Contrast_exps.Relative_Loaction_Turtle import Get_Relative_Location
import time
import matplotlib.pyplot as plt
# from Robot.Write_list_to_csv import wirte_list_to_csv
from Contrast_exps.fuzzy_rules import fuzzy_control
from Contrast_exps.defuzzificztion import defuzzificztion

start = time.time()


class Robot():
    def __init__(self,  location, target, color):
        self.robot = turtle.Pen()
        self.location_x = location[0]
        self.location_y = location[1]
        self.color = color
        self.robot.pencolor(color)
        self.robot.shape('circle')
        self.robot.pensize(5)
        self.target_x = target[0]
        self.target_y = target[1]
        self.robot.color('white')
        self.robot.circle(5)
        self.robot.penup()
        self.robot.goto(location[0],location[1])
        self.robot.pencolor(color)
        self.robot.pendown()
        self.velocity = 4
        self.heading  = self.robot.heading()
    def move(self):
        self.robot.setheading(0)
        loaction1,loaction2 = self.robot.position()
        # print(loaction1,loaction2)
        angle = degrees(atan(fabs(self.target_y - loaction2) / fabs(loaction1 - self.target_x)))
        # print(angle)
        if loaction1 < self.target_x:
            if loaction2 < self.target_y:
                self.robot.left(angle)
            if loaction2 >= self.target_y:
                self.robot.right(angle)
        if loaction1 > self.target_x:
            if loaction2 >= self.target_y:
                self.robot.left(angle)
                self.robot.right(180)
            if loaction2 < self.target_y:
                self.robot.right(angle)
                self.robot.left(180)
        if loaction1 == self.target_x:
            if loaction2 > self.target_y:
                self.robot.right(90)
            else:
                self.robot.left(90)
        if self.robot.distance(self.target_x,self.target_y) > 1:
            self.robot.forward(4)
        self.velocity = 4
        self.location_x,self.location_y = self.robot.position()
        self.heading = self.robot.heading()


    def move_heading_velocity(self,heading_angle,velocity):
        if heading_angle < 0:
            self.robot.left(fabs(heading_angle))
        else:
            self.robot.right(heading_angle)
        self.robot.forward(velocity)
        self.velocity = velocity
        self.location_x, self.location_y = self.robot.position()
        self.heading = self.robot.heading()




def conflict_detection(owner, intruders):
    conflict_UAV = []
    antecedent = [None] * 3
    for i in intruders:
        temp_conflict = []
        d = get_distance([owner[0], owner[1]], [i[0], i[1]])
        if d < 24:
            Relative_location = Get_Relative_Location([owner[0],owner[1]], [i[0],i[1]], owner[3])
            # print(Relative_location)
            if Relative_location:
                temp_conflict.append(Relative_location)

        if temp_conflict:
            conflict_UAV.append(temp_conflict)
            if temp_conflict[0] == 'F':
                if d < 6:
                    antecedent[1] = 'N'
                elif d > 16:
                    antecedent[1] = 'F'
                else:
                    antecedent[1] = 'M'
            if temp_conflict[0] == 'R':
                if d < 10:
                    antecedent[2] = 'N'
                else:
                    antecedent[2] = 'M'
            if temp_conflict[0] == 'L':
                if d < 10:
                    antecedent[0] = 'N'
                else:
                    antecedent[0] = 'M'

    if conflict_UAV:
        # print(conflict_UAV)
        if antecedent[0] == None:
            antecedent[0] = 'M'
        if antecedent[1] == None:
            antecedent[1] = 'F'
        if antecedent[2] == None:
            antecedent[2] = 'M'
        # print(antecedent)
        consequence = fuzzy_control(antecedent)
        # print(consequence)
        # print(defuzzificztion(consequence))

        return defuzzificztion(consequence)[0],defuzzificztion(consequence)[1]




def main(P1, P2, P3, P4, P5, P6, P7, P8):
    start = time.time()
    used_time = 0
    turtle.setup(700, 700, 600, 10)
    # turtle.clear()
    r1 = Robot(P1[0], P1[1], 'red')
    r2 = Robot(P2[0], P2[1],  'blue')
    r3 = Robot(P3[0], P3[1],  'green')
    r4 = Robot(P4[0], P4[1],  'black')
    r5 = Robot(P5[0], P5[1],  'indigo')
    r6 = Robot(P6[0], P6[1],  'chocolate')
    r7 = Robot(P7[0], P7[1],  'lawngreen')
    r8 = Robot(P8[0], P8[1],  'gray')
    robot_list = [r1, r2, r3, r4, r5, r6, r7, r8]

    Tr = [[[] for i in range(2)] for j in range(len(robot_list))]

    while True:

        # calculate the detection params
        detection_params = [[] for i in range(len(robot_list))]
        for r in robot_list:
            detection_params[robot_list.index(r)].append([r.location_x, r.location_y, r.velocity, r.heading])
            temp = copy.copy(robot_list)
            index = temp.index(r)
            del temp[index]
            intruders_temp = []
            for j in temp:
                intruders_temp.append([j.location_x, j.location_y, j.velocity, j.heading])
            detection_params[robot_list.index(r)].append(intruders_temp)

        target = 0
        # target used to check if reach target position
        for r in robot_list:
            if get_distance([r.location_x, r.location_y], [r.target_x, r.target_y]) < 10:
                target = target + 1
            else:
                order = conflict_detection(detection_params[robot_list.index(r)][0],
                                           detection_params[robot_list.index(r)][1])
                if order:
                    r.move_heading_velocity(order[0], order[1])
                    Tr[robot_list.index(r)][0].append(r.location_x)
                    Tr[robot_list.index(r)][1].append(r.location_y)
                else:
                    r.move()
                    Tr[robot_list.index(r)][0].append(r.location_x)
                    Tr[robot_list.index(r)][1].append(r.location_y)
                target = target + 0
        if target == len(robot_list):
            end = time.time()
            time.sleep(5)
            turtle.clearscreen()
            excepted_legth = 0
            real_legth = 0
            for i in Tr:
                temp = get_distance([i[0][0],i[1][0]],[i[0][-1],i[1][-1]])
                excepted_legth = excepted_legth + temp
            # print("期望距离：",excepted_legth)
            for j in Tr:
                for k in range(len(j[0])-1):
                    real_legth = real_legth + get_distance([j[0][k],j[1][k]],[j[0][k+1],j[1][k+1]])
            # print("实际距离：",real_legth)
            # print("路径度量",real_legth/excepted_legth)
            Tra_metric = real_legth/excepted_legth

            used_time = end - start
            episode = []
            for i in Tr:
                episode.append(len(i[0]))
            # print(episode)
            # print("到达目标所需步骤：", episode)
            # print("总共花费实际时间：", used_time)
            # print("时间度量：", (used_time/max(episode))/4)
            Time_metric = (used_time/max(episode))/4

            mean_min_separation = []
            for j in range(len(episode)):
                for k in range(len(Tr)):
                    for m in range(k+1,len(Tr)):
                        mean_min_separation.append(get_distance([Tr[k][0][j],Tr[k][0][j]],[Tr[m][0][j],Tr[m][1][j]]))

            # print("最小间隔：", min(mean_min_separation)/2)
            Sep_metric = min(mean_min_separation)
            print("本次度量：", Sep_metric, Tra_metric, Time_metric, '\n')
            return Sep_metric, Tra_metric, Time_metric
            # break


if __name__ == '__main__':
    collision_times = []
    Sep_metric, Tra_metric, Time_metric = [], [], []
    for i in range(50):
        print("第{}次".format(str(i+1)))


        UAV1_start_x, UAV1_start_y = 300 + random.randint(-50, 50), random.randint(-50, 50)
        UAV1_target_x, UAV1_target_y = -100 + random.randint(-50, 50), random.randint(-50, 50)
        UAV2_start_x, UAV2_start_y = 212 + random.randint(-50, 50), 212 + random.randint(-50, 50)
        UAV2_target_x, UAV2_target_y = -71 + random.randint(-50, 50), -71 + random.randint(-50, 50)
        UAV3_start_x, UAV3_start_y = 0 + random.randint(-50, 50), 300 + random.randint(-50, 50)
        UAV3_target_x, UAV3_target_y = 0 + random.randint(-50, 50), -100 + random.randint(-50, 50)
        UAV4_start_x, UAV4_start_y = -212 + random.randint(-50, 50), 212 + random.randint(-50, 50)
        UAV4_target_x, UAV4_target_y = 71 + random.randint(-50, 50), -71 + random.randint(-50, 50)
        UAV5_start_x, UAV5_start_y = -300 + random.randint(-50, 50), 0 + random.randint(-50, 50)
        UAV5_target_x, UAV5_target_y = 100 + random.randint(-50, 50), 0 + random.randint(-50, 50)
        UAV6_start_x, UAV6_start_y = -212 + random.randint(-50, 50), -212 + random.randint(-50, 50)
        UAV6_target_x, UAV6_target_y = 71 + random.randint(-50, 50), 71 + random.randint(-50, 50)
        UAV7_start_x, UAV7_start_y = 0 + random.randint(-50, 50), -300 + random.randint(-50, 50)
        UAV7_target_x, UAV7_target_y = 0 + random.randint(-50, 50), 100 + random.randint(-50, 50)
        UAV8_start_x, UAV8_start_y = 212 + random.randint(-50, 50), -212 + random.randint(-50, 50)
        UAV8_target_x, UAV8_target_y = -71 + random.randint(-50, 50), 71 + random.randint(-50, 50)

        print("坐标信息：", [[UAV1_start_x, UAV1_start_y], [UAV1_target_x, UAV1_target_y]], \
              [[UAV2_start_x, UAV2_start_y], [UAV2_target_x, UAV2_target_y]], \
              [[UAV3_start_x, UAV3_start_y], [UAV3_target_x, UAV3_target_y]], \
              [[UAV4_start_x, UAV4_start_y], [UAV4_target_x, UAV4_target_y]], \
              [[UAV5_start_x, UAV5_start_y], [UAV5_target_x, UAV5_target_y]], \
              [[UAV6_start_x, UAV6_start_y], [UAV6_target_x, UAV6_target_y]], \
              [[UAV7_start_x, UAV7_start_y], [UAV7_target_x, UAV7_target_y]], \
              [[UAV8_start_x, UAV8_start_y], [UAV8_target_x, UAV8_target_y]]
              )
        try:
            Sep, Tra, Time = \
                main([[UAV1_start_x, UAV1_start_y], [UAV1_target_x, UAV1_target_y]], \
                     [[UAV2_start_x, UAV2_start_y], [UAV2_target_x, UAV2_target_y]], \
                     [[UAV3_start_x, UAV3_start_y], [UAV3_target_x, UAV3_target_y]], \
                     [[UAV4_start_x, UAV4_start_y], [UAV4_target_x, UAV4_target_y]], \
                     [[UAV5_start_x, UAV5_start_y], [UAV5_target_x, UAV5_target_y]], \
                     [[UAV6_start_x, UAV6_start_y], [UAV6_target_x, UAV6_target_y]], \
                     [[UAV7_start_x, UAV7_start_y], [UAV7_target_x, UAV7_target_y]], \
                     [[UAV8_start_x, UAV8_start_y], [UAV8_target_x, UAV8_target_y]]
                     )
            collision_times.append(Sep)
            Sep_metric.append(Sep)
            Tra_metric.append(Tra)
            Time_metric.append(Time)
        except:
            print("碰撞次数：",collision_times)
            print("运行出错！")
            turtle.clearscreen()
    print(Sep_metric)
    print(Tra_metric)
    print(Time_metric)



# [37.65351, 65.97643, 48.64972, 66.77102, 51.66428, 46.81592, 25.36615, 4.34254, 5.00216, 51.88752, 45.20488, 19.20238, 73.54436, 48.40923, 49.27792, 19.83593, 25.10973, 52.85408, 20.0471, 47.03936, 67.87058, 73.83872, 33.05931, 76.34771, 38.23566, 28.63277, 13.67295, 16.13438, 48.03225, 91.85034, 62.5066, 51.61839, 32.03564, 44.91542, 13.007, 85.55792, 13.65954, 8.15782, 45.91143, 52.08483, 38.33407, 35.68301, 29.83929, 27.57733, 69.19144, 41.49158, 71.27195, 27.44391]
# [1.4261905444750202, 1.588715590334884, 1.283432850078246, 1.1362626171674644, 1.7631317672340037, 2.2505322050571244, 1.318732709655613, 1.2687340059320236, 1.4879607938834831, 1.0768023211624016, 1.1767827719259973, 1.559294536560843, 1.3402817516281664, 1.385822186538981, 1.3855168998927232, 1.369061694084655, 1.7880743175234448, 1.230387774175889, 1.1412594533313778, 1.2698073620398382, 1.2519102023653725, 2.1294998101520126, 1.6925394327729457, 1.068494504599201, 1.825848613369695, 1.2980297550365205, 1.4618248214464755, 1.4842174058510145, 1.83057016582508, 1.1186196365597545, 2.1396376055669246, 1.6672885765923826, 1.3780650181439311, 1.2369098910124268, 1.389897351104775, 1.7076500842298563, 1.1793977570749083, 1.618064320002823, 1.1000522212179227, 1.2634552496907232, 1.4378886642437165, 1.5670588011211193, 1.2556166386671135, 1.850627448453994, 1.1816825359091858, 1.3407937287238956, 1.629982890242528, 1.5992632006715102]
# [0.3748495784945458, 0.21732739381053867, 0.29661558093368146, 0.3909843862056732, 0.1284291209020746, 0.0873032491810922, 0.22794570417200785, 0.4084869875226702, 0.1564175890432442, 0.4498828378286255, 0.460301807578306, 0.32901267491389014, 0.2946287286119396, 0.22015697504743675, 0.29853121894929147, 0.26653618332943485, 0.0852270648748325, 0.2906263888114157, 0.3886938477874896, 0.24744335204092757, 0.19894109905169727, 0.10872133482586253, 0.2506614355225637, 0.5568140119314193, 0.1381408717464562, 0.20678177157778108, 0.21271438573328955, 0.2294555657815725, 0.13643813638598523, 0.3850807498978532, 0.14823091631635613, 0.17691072491702117, 0.1606402111876952, 0.18700415881474813, 0.25509620434801344, 0.12880098749308275, 0.3979775309562683, 0.29493866644459643, 0.4775524341051851, 0.425004686590886, 0.18188540818321358, 0.16765280429428145, 0.2635262959143695, 0.09288569295058285, 0.3270663125106538, 0.29766160199410807, 0.27334320960270664, 0.21496415271588354]
