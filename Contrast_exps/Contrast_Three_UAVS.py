#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 14:33
# @Author  : blvin.Don
# @File    : Contrast_Three_UAVS.py


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




def main(P1, P2, P3):
    start = time.time()
    used_time = 0
    turtle.setup(700, 700, 600, 0)
    # turtle.clear()
    r1 = Robot(P1[0], P1[1], 'red')
    r2 = Robot(P2[0], P2[1],  'blue')
    r3 = Robot(P3[0], P3[1],  'green')
    robot_list = [r1, r2, r3]

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
    for i in range(100):
        print("第{}次".format(str(i+1)))
        UAV1_start_x, UAV1_start_y = random.randint(-300, 10), random.randint(10, 300)
        UAV1_target_x, UAV1_target_y = random.randint(10, 300), random.randint(-300, 10)
        UAV2_start_x, UAV2_start_y = random.randint(-300, 10), random.randint(-300, 10)
        UAV2_target_x, UAV2_target_y = random.randint(10, 300), random.randint(10, 300)
        UAV3_start_x, UAV3_start_y = random.randint(10, 300), random.randint(10, 300)
        UAV3_target_x, UAV3_target_y = random.randint(-300, 10), random.randint(-300, 10)
        print("坐标信息：", [[UAV1_start_x, UAV1_start_y], [UAV1_target_x, UAV1_target_y]], \
              [[UAV2_start_x, UAV2_start_y], [UAV2_target_x, UAV2_target_y]], \
              [[UAV3_start_x, UAV3_start_y], [UAV3_target_x, UAV3_target_y]])
        try:
            Sep, Tra, Time = \
                main([[UAV1_start_x, UAV1_start_y], [UAV1_target_x, UAV1_target_y]], \
                     [[UAV2_start_x, UAV2_start_y], [UAV2_target_x, UAV2_target_y]], \
                     [[UAV3_start_x, UAV3_start_y], [UAV3_target_x, UAV3_target_y]])
            collision_times.append(Sep)
            Sep_metric.append(Sep)
            Tra_metric.append(Tra)
            Time_metric.append(Time)
        except:
            print("运行出错！")
    print("碰撞次数：", collision_times)
    print("平均度量：", round(sum(Sep_metric)/len(Sep_metric), 3), round(sum(Tra_metric)/len(Tra_metric), 3), round(sum(Time_metric)/len(Time_metric), 3))


# 碰撞次数： [77.62494, 99.50533, 52.15611, 277.79425, 167.34076, 201.20378, 171.10667, 140.37603, 47.49412, 302.19447, 283.64077, 225.23673, 25.94809, 127.98419, 111.21981, 155.36196, 196.46968, 94.09362, 32.42091, 95.19039, 238.34723, 239.40292, 65.85987, 144.80583, 224.12616, 127.34884, 181.07562, 47.71042, 252.74877, 95.72106, 90.33653, 149.36858, 32.03206, 173.90477, 192.45063, 118.5917, 78.42051, 193.02365, 115.38643, 231.58532, 83.10519, 104.05896, 260.80345, 71.5342, 126.68328, 240.82953, 178.02956, 129.43862, 213.21018, 47.48302, 178.44, 89.15385, 127.40025, 209.9392, 86.88613, 139.5896, 197.11817, 40.70091, 170.58296, 230.94442, 174.67478, 57.03829, 127.25046, 225.29726, 143.473, 135.84504, 89.48189, 164.33572, 28.15483, 214.64138, 77.5231, 169.13122, 61.43402, 128.36515, 320.86875, 259.29537, 120.57316, 207.99322, 45.99435, 284.41834, 50.5089, 63.13604, 9.31615, 61.25175, 34.77844, 54.52983, 143.85547, 112.26152, 63.45922, 90.90457, 153.76974, 70.22411, 102.82234, 152.89143, 47.33183, 103.18963, 73.15055, 97.50656, 162.35776, 28.72299]
# 平均度量： 135.143 1.024 0.172