#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 3/4/19 11:29 AM
# @Author  : tang
# @File    : six_robors.py

import turtle
import time
from math import fabs,degrees,atan,asin,sqrt,cos,sin
import numpy as np
from Robot.Get_distance import get_distance
from Robot.Get_Angle_TwoVec import Get_Angle_Between_Two_Vector
from contrast_exp_wen2015.Relative_Loaction_Turtle import Get_Relative_Location
import time
import matplotlib.pyplot as plt
from Robot.Write_list_to_csv import wirte_list_to_csv
from contrast_exp_wen2015.fuzzy_rules import fuzzy_control
from contrast_exp_wen2015.defuzzificztion import defuzzificztion

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
        if d < 4:
            print('Collision')
            break
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
        print(antecedent)
        consequence = fuzzy_control(antecedent)
        print(consequence)
        print(defuzzificztion(consequence))

        return defuzzificztion(consequence)[0],defuzzificztion(consequence)[1]







if __name__ == '__main__':
    turtle.setup(500, 500, 300, 10)
    r1 = Robot([-60,60],[60,-60],'red')
    r2 = Robot([-60,-60], [60, 60], 'blue')
    r3 = Robot([60, -60], [-60,60], 'green')
    r4 = Robot([60, 60], [-60,-60], 'purple')
    r5 = Robot([60,-10],[-60,10],'brown')
    r6 = Robot([-10,-60],[10,60],'navy')

    tr_r1 = [[] for i in range(2)]
    tr_r2 = [[] for j in range(2)]
    tr_r3 = [[] for k in range(2)]
    tr_r4 = [[] for l in range(2)]
    tr_r5 = [[] for m in range(2)]
    tr_r6 = [[] for x in range(2)]


    while True:
        order1 = conflict_detection([r1.location_x,r1.location_y,r1.velocity,r1.heading],[[r2.location_x,r2.location_y],[r3.location_x,r3.location_y],[r4.location_x,r4.location_y],[r5.location_x, r5.location_y, r5.velocity, r5.heading],[r6.location_x, r6.location_y, r6.velocity, r6.heading]])
        if order1:
            r1.move_heading_velocity(order1[1],order1[0])
        else:
            r1.move()
        order2 = conflict_detection([r2.location_x, r2.location_y, r2.velocity, r2.heading],
                                    [[r1.location_x, r1.location_y, r1.velocity, r1.heading],
                                     [r3.location_x, r3.location_y, r3.velocity, r3.heading],
                                     [r4.location_x, r4.location_y, r4.velocity, r4.heading],[r5.location_x, r5.location_y, r5.velocity, r5.heading],[r6.location_x, r6.location_y, r6.velocity, r6.heading]])
        if order2:
            r2.move_heading_velocity(order2[1],order2[0])
        else:
            r2.move()
        order3 = conflict_detection([r3.location_x, r3.location_y, r3.velocity, r3.heading],
                                    [[r1.location_x, r1.location_y, r1.velocity, r1.heading],
                                     [r2.location_x, r2.location_y, r2.velocity, r2.heading],[r4.location_x,r4.location_y,r4.velocity,r4.heading],[r5.location_x, r5.location_y, r5.velocity, r5.heading],[r6.location_x, r6.location_y, r6.velocity, r6.heading]])
        if order3:
            r3.move_heading_velocity(order3[1], order3[0])
        else:
            r3.move()
        order4 = conflict_detection([r4.location_x, r4.location_y, r4.velocity, r4.heading],
                                    [[r1.location_x, r1.location_y, r1.velocity, r1.heading],
                                     [r2.location_x, r2.location_y, r2.velocity, r2.heading],
                                     [r3.location_x, r3.location_y, r3.velocity, r3.heading],[r5.location_x, r5.location_y, r5.velocity, r5.heading],[r6.location_x, r6.location_y, r6.velocity, r6.heading]])
        if order4:
            r4.move_heading_velocity(order4[1], order4[0])
        else:
            r4.move()
        order5 = conflict_detection([r5.location_x, r5.location_y, r5.velocity, r5.heading],
                                    [[r1.location_x, r1.location_y, r1.velocity, r1.heading],
                                     [r2.location_x, r2.location_y, r2.velocity, r2.heading],
                                     [r3.location_x, r3.location_y, r3.velocity, r3.heading],[r4.location_x, r4.location_y, r4.velocity, r4.heading],[r6.location_x, r6.location_y, r6.velocity, r6.heading]])

        if order5:
            r5.move_heading_velocity(order5[1], order5[0])
        else:
            r5.move()

        order6 = conflict_detection([r6.location_x, r6.location_y, r6.velocity, r6.heading],
                                    [[r1.location_x, r1.location_y, r1.velocity, r1.heading],
                                     [r2.location_x, r2.location_y, r2.velocity, r2.heading],
                                     [r3.location_x, r3.location_y, r3.velocity, r3.heading],
                                     [r4.location_x, r4.location_y, r4.velocity, r4.heading],
                                     [r5.location_x, r5.location_y, r5.velocity, r5.heading]])

        if order6:
            r6.move_heading_velocity(order6[1], order6[0])
        else:
            r6.move()

        tr_r1[0].append(r1.location_x)
        tr_r1[1].append(r1.location_y)
        tr_r2[0].append(r2.location_x)
        tr_r2[1].append(r2.location_y)
        tr_r3[0].append(r3.location_x)
        tr_r3[1].append(r3.location_y)
        tr_r4[0].append(r4.location_x)
        tr_r4[1].append(r4.location_y)
        tr_r5[0].append(r5.location_x)
        tr_r5[1].append(r5.location_y)
        tr_r6[0].append(r6.location_x)
        tr_r6[1].append(r6.location_y)

        if get_distance([r1.location_x, r1.location_y], [r1.target_x, r1.target_y]) < 3 and get_distance(
            [r2.location_x, r2.location_y], [r2.target_x, r2.target_y]) < 3 and get_distance(
            [r3.location_x, r3.location_y], [r3.target_x, r3.target_y]) < 3 and get_distance(
            [r4.location_x, r4.location_y], [r4.target_x, r4.target_y]) < 3 and get_distance(
            [r5.location_x, r5.location_y], [r5.target_x, r5.target_y]) < 3 and get_distance(
            [r6.location_x, r6.location_y], [r6.target_x, r6.target_y]) < 3:
            break

    elapsed = (time.time() - start)
    print("Time used:", elapsed)

    fig = plt.figure()
    plt.plot(tr_r1[0], tr_r1[1], color='red', label='r1')
    plt.plot(tr_r2[0], tr_r2[1], color='blue', label='r2')
    plt.plot(tr_r3[0], tr_r3[1], color='green', label='r3')
    plt.plot(tr_r4[0], tr_r4[1], color='purple', label='r4')
    plt.plot(tr_r5[0], tr_r5[1], color='brown', label='r5')
    plt.plot(tr_r6[0], tr_r6[1], color='navy', label='r6')
    #
    # wirte_list_to_csv(tr_r1, 'tr_r1.csv')
    # wirte_list_to_csv(tr_r2, 'tr_r2.csv')
    # wirte_list_to_csv(tr_r3, 'tr_r3.csv')
    # wirte_list_to_csv(tr_r4, 'tr_r4.csv')

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0,
               ncol=3, mode="expand", borderaxespad=0.)
    length_to_target = min(len(tr_r1[0]), len(tr_r2[0]), len(tr_r3[0]), len(tr_r4[0]),len(tr_r5[0]),len(tr_r6[0]))
    print("episode:",length_to_target)
    expected_length = get_distance([tr_r1[0][0], tr_r1[1][0]], [tr_r1[0][-1], tr_r1[1][-1]]) + get_distance(
        [tr_r2[0][0], tr_r2[1][0]], [tr_r2[0][-1], tr_r2[1][-1]]) \
                      + get_distance([tr_r3[0][0], tr_r3[1][0]], [tr_r3[0][-1], tr_r3[1][-1]]) + get_distance(
        [tr_r4[0][0], tr_r4[1][0]], [tr_r4[0][-1], tr_r4[1][-1]])  + get_distance(
        [tr_r5[0][0], tr_r5[1][0]], [tr_r5[0][-1], tr_r5[1][-1]])+ get_distance(
        [tr_r6[0][0], tr_r6[1][0]], [tr_r6[0][-1], tr_r6[1][-1]])
    min_distance = []
    Trajectory = [tr_r1, tr_r2, tr_r3, tr_r4,tr_r5,tr_r6]
    # print(Trajectory[0][0])
    # print("计算Fitness！")
    for j in range(6):
        for k in range(j + 1, 6):
            for i in range(min(len(tr_r1[0]), len(tr_r2[0]), len(tr_r3[0]), len(tr_r4[0]),len(tr_r5[0]),len(tr_r6[0]))):
                min_distance.append(get_distance([Trajectory[j][0][i], Trajectory[j][1][i]],
                                                 [Trajectory[k][0][i], Trajectory[k][1][i]]))
    print("最小距离度量：", min(min_distance)/2)
    mean_min_separation = min(min_distance) / 2

    total_length = 0
    for t in Trajectory:
        for m in range(len(t[0]) - 1):
            total_length = total_length + get_distance([t[0][m], t[1][m]], [t[0][m + 1], t[1][m + 1]])

    print("最短路径度量：",total_length/expected_length)
    print(total_length,expected_length)



    plt.show()


