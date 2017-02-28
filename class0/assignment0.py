# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:04:33 2017

@author: elara
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#(a)
def gen_data(n):
    x = np.sort(np.array([np.random.uniform(0,1,n)]))
    y = 0.5 + 0.4 * np.sin(2 * np.pi * x) + np.random.normal(0,0.05,n)
    return np.append(x, y, axis =0)
#(b)


train = []
test = []


def qb(n, max_d):
    global train_mse, test_mse
    train = gen_data(n) # 生成训练集
    #plt.plot(train[0],train[1],'ro-')
    test = gen_data(n) # 生成测试集
    #plt.plot(test[0],test[1],'ro-')
    p = [[]]*(max_d+1)
    train_mse = pd.Series([])
    test_mse = pd.Series([])
    for d in range(max_d+1):
        p[d] = np.polyfit(train[0], train[1], d)
        train_pred = np.polyval(p[d] ,train[0]) # 训练集预测
        train_mse[d] = np.mean((train[1] - train_pred)**2) # 训练集mse
        test_pred = np.polyval(p[d] ,test[0]) # 测试集预测
        test_mse[d] = np.mean((test[1] - test_pred)**2) # 训练集mse
        train_d = np.argmin(train_mse) # 训练集mse最小阶数            
    lx = np.linspace(0,1,100)
    ly = np.polyval(p[train_d] ,lx)
    print("when n =",n,"the best order for train set is:",train_d)
    plt.plot(train[0], train[1], 'ro', lx, ly,'g-')
    

qb(9,9)
plt.plot(range(10), train_mse, 'ro-', range(10), test_mse, 'bo-')
qb(15,9)
plt.plot(range(10), train_mse, 'ro-', range(10), test_mse, 'bo-')
qb(100,9)
plt.plot(range(10), train_mse, 'ro-', range(10), test_mse, 'bo-')

#(c)


