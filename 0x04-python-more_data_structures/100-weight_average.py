#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_scores = 0
    sum_weight = 0
    for scores, weight in my_list:
        sum_scores += scores * weight
        sum_weight += weight
        return sum_scores / sum_weight
