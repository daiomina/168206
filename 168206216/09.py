# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:34:24 2018

@author: 李金印

上机题目
"""


def find_path(start, end, paths) :
    if start == end :
        return "start=end"
    else :
        visited = []    #存放路径的队列
        visited.append(start)
        tmp = 0 #记录步骤数
        paths.append(end)
        for word in visited :   #遍历队列中每个单词
            for i in range(len(word)) : #遍历单词中每个字母
                for j in range(97, 123) : #遍历26个字母
                    word = word[:i] + chr(j) + word[i+1:] #替换字母
                    new_word = word    # new_word = 替换一个字母后的新单词
                    #print(new_word)
                    word = visited[-1]                    
                    if new_word in paths and new_word not in visited :  #新单词在队列中存在且不在路径队列中时
                        visited.append(new_word)    #将新单词存入路径队列
                        tmp += 1
                        #print (visited)
                    if new_word == end :
                        print ("转换完成，共需要 %d 步,过程如下" %tmp)
                        return visited

            
start = "hit"
end = "cog"
adict = ["hot", "dot", "dog", "lot", "log"]

print (find_path(start, end, adict))


