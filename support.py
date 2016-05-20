#!/usr/bin/python
#Title: Support file to generate states and RL testing
#Date:20/5/2016
#Author:Adithya Selvaprithiviraj

from itertools import product
import json

all_states=list(product("XO ",repeat=9))

valid_states=[]

for i in all_states:
    if (not (i.count("X")>i.count("O")+1)):
        if (not (i.count("O")>i.count("X")+1)):
            valid_states.append(i)

# print len(valid_states)
# for i in valid_states:
#     print i


s_valid_states=[]

for i in valid_states:
    dummy=""
    for j in i:
        dummy += j

    s_valid_states.append(dummy)



def pos_nextstate(state):
    print state
    tempstate=list(state)
    temp_list=[]
    temp_list.append([])
    temp_list.append([])
    for i in range(9):
        if state[i]==" ":
            if state.count("O")<=state.count("X"):
                tempstate[i]="O"
                temp_list[0].append((''.join(tempstate),i,0))
            if state.count("X")<=state.count("O"):
                tempstate[i]="X"
                temp_list[1].append((''.join(tempstate),i,0))
            
        tempstate=list(state)

    return temp_list
            

def save_init_file(s_valid_states):
    test_dict={}
    for i in s_valid_states:
        test_dict[i]={"xnextstate":[],"onextstate":[],"qval":0}

    with open('data.json', 'w') as fp:
        json.dump(test_dict, fp)

with open('data.json', 'r') as fp:
    data_dict = json.load(fp)



