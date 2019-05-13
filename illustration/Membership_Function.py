#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 10:56
# @Author  : blvin.Don
# @File    : Membership_Function.py

import matplotlib.pyplot as plt
import numpy as np



# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)

if __name__ == '__main__' :
    t1 = np.arange(0, 5, 0.1)
    t2 = np.arange(0, 5, 0.02)

    plt.figure(12)
    plt.subplot(221)
    plt.plot([0, 2.5, 15, 20], [1, 1, 0, 0], label = 'D')
    plt.plot([0, 2.5, 15, 20], [0, 0, 1, 1], label = 'A')
    plt.ylim(0, 1.2)
    plt.xlim(0, 20)
    plt.xticks([2.5, 15, 20], [r'$2.5$', r'$15$', r'$20$'])
    plt.yticks([0, 1], [r'$0$', r'$1$'])
    plt.xlabel(r"$(a)$")
    plt.annotate("D", (2, 1.05))
    plt.annotate("A", (15, 1.05))
    # plt.subplots_adjust(left=0.9, right=1, wspace=0.25, hspace=0.25, bottom=0.13, top=0.91)

    plt.subplot(222)
    plt.plot([0, 1], [1, 0], label = 'DE')
    plt.plot([0, 1, 2], [0, 1, 0], label = 'MA')
    plt.plot([1, 2], [0, 1], label = 'AC')
    plt.ylim(0, 1.2)
    plt.xlim(0, 2)
    plt.xticks([1, 2], [r'$1$', r'$2$'])
    plt.yticks([0, 1], [r'$0$', r'$1$'])
    plt.annotate("DE", (0.05, 1.05))
    plt.annotate("MA", (0.91, 1.05))
    plt.annotate("AC", (1.85, 1.05))
    plt.xlabel(r"$(b)$")
    # plt.subplots_adjust(left=0.9, right=1, wspace=0.25, hspace=0.25, bottom=0.13, top=0.91)

    plt.subplot(212)
    plt.plot([0, 22.5], [1, 0])
    plt.plot([0, 22.5, 45], [0, 1, 0])
    plt.plot([22.5, 45, 67.5], [0, 1, 0])
    plt.plot([45, 67.5, 90], [0, 1, 0])
    plt.plot([67.5, 90], [0, 1])
    plt.ylim(0, 1.2)
    plt.xlim(0, 90)
    plt.xticks([22.5, 45, 67.5, 90], [r'$22.5$', r'$45$', r'$67.5$', r'$90$'])
    plt.yticks([0, 1], [r'$0$', r'$1$'])
    plt.annotate("VS", (1, 1.05))
    plt.annotate("S", (21.5, 1.05))
    plt.annotate("M", (44, 1.05))
    plt.annotate("L", (67, 1.05))
    plt.annotate("VL", (87, 1.05))
    plt.xlabel(r"$(c)$")
    # plt.subplots_adjust(left=0.9, right=1, wspace=0.25, hspace=0.25, bottom=0.13, top=0.91)
    plt.savefig('MF.pdf')
    plt.show()
