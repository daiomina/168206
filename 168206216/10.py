# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 00:45:31 2018

@author: diaomina

#考试题  说真话的是D，罪犯是A

A：我没有偷钻石。
B：D就是罪犯。
C：B是盗窃这块钻石的罪犯。
D：B有意诬陷我。
假定只有一个人说的是真话，编程序判断谁偷走了钻石。

"""

def find(result_list, true_man):
    for x in range(len(result_list)):     #遍历所有情况
        if ( (result_list[x]!="A") + (result_list[x]=="D") + (result_list[x]=="B") + (result_list[x]!="D") == true_man ):
            print("罪犯是：%s" %result_list[x])



                
true_man = 1    #说真话的人数
result_list = ["A", "B", "C", "D"]    #罪犯是谁的4种情况

find(result_list, true_man)