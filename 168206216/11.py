# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:53:54 2018

@author: diaomina

写一个简单算法分析，两页实验报告纸，题目如下：
A: 我没有偷钻石。
B: D就是罪犯。
C: B是盗窃这块钻石的罪犯。
D: B有意诬陷我。
分析有两个人说真话的情况，不要管谁偷了钻石。

"""

def find(result_list, true_man):
    for x in range(len(result_list)):     #遍历所有情况
        if ((result_list[x]!="A") + (result_list[x]=="D") + (result_list[x]=="B") + (result_list[x]!="D")  == true_man):
            n1 = (result_list[x]!="A")  
            n2 = (result_list[x]=="D")
            n3 = (result_list[x]=="B")
            n4 = (result_list[x]!="D")
            n = [n1, n2, n3, n4]
            for y in range(len(n)):
                if (n[y] == 1):
                    print("%s " % result_list[y],end="")    #说真话的人
            print("说真话时：")
            print("罪犯是： %s" %result_list[x])


                
true_man = 2    #说真话的人数
result_list = ["A", "B", "C", "D"]    #罪犯是谁的4种情况

find(result_list, true_man)