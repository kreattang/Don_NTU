#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 22:23
# @Author  : blvin.Don
# @File    : SVM2SVs.py

import csv
from sklearn.svm import SVC
from collections import Counter
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

X = []
Y = []
csv_reader = csv.reader(open('I:/Github_Repositories/Don_NTU/FangML/sensor_readings_24.csv', encoding='utf-8'))
for row in csv_reader:
    temp = []
    for i in range(24):
        temp.append(float(row[i]))
    X.append(temp)
    Y.append(row[-1])
# print(X[0])

values_counts = Counter(Y)
print("正负样本类别统计：",values_counts)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)


clf = SVC(gamma='auto')
clf.fit(X_train, y_train)
print("支持向量：", clf.support_vectors_)
SVs = clf.support_vectors_

# 预测支持向量
SVs_predit = clf.predict(SVs)
# 训练随机森林
RF = RandomForestClassifier()
RF.fit(SVs,SVs_predit)

y_predit = RF.predict(X_test)
print("再RF上的分类性能！：\n")
print("准确率：", accuracy_score(y_predit, y_test))
# print("精确率：", precision_score(y_predit, y_test))
# print("召回率：",recall_score(y_predit, y_test))
for i in range(len(RF.estimators_)):
    tree.export_graphviz(RF.estimators_[i] , '%d.dot'%i)
