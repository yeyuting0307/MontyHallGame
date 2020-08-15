#!/usr/bin/env python
# coding: utf-8

# In[106]:


import random as rand
change_win = []
not_change_win = []

simulation_time = 1000000
for i in range(simulation_time):
    # 三道門，ans代表中獎門，user_select代表玩家選的門
    three_doors = {1,2,3}
    ans = set(rand.sample(three_doors, 1))
    user_select = set(rand.sample(three_doors, 1))


    # 主持人打開一道非中獎門，剩下兩道門
    doors_can_open = three_doors - ans - user_select
    door_opened =set(rand.sample(doors_can_open, 1))
    left_two_doors = three_doors - door_opened
    left_two_doors

    # 選擇換門
    # print('First choice:', user_select) #一開始所選
    change_select = left_two_doors - user_select
    # print('After change:', change_select) #換門之後的選擇
    # print('Ans:', ans)

    #換門中獎

    change_win.append(change_select == ans)

    #不換門中獎
    not_change_win.append(user_select == ans)
    
print('In', simulation_time, 'simulations')
print('Change door then win:', sum(change_win))
print('Not change door then win:', sum(not_change_win))

