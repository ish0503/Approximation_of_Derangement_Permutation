import numpy as np

def Judge(shuffle_arr,arr):
    for v in range(len(shuffle_arr)):
            if shuffle_arr[v-1] == arr[v-1]:
                return "fail"
                # fail += 1
                # break
            if v == len(shuffle_arr) - 1:
                return "success"
                # success += 1

def culculation(attempt, num):
    arr = np.arange(num)
    shuffle_arr = np.arange(num)
    success = 0
    fail = 0
    for i in range(attempt):
        np.random.shuffle(shuffle_arr)
        if Judge(shuffle_arr, arr) == "fail":
            fail += 1
        elif Judge(shuffle_arr, arr) == "success":
            success += 1
    
    return success / (success + fail)

import matplotlib.pyplot as plt
import math
num = 3 # 서로 바꾸는 개수
rate = 0
for i in range(1, 500):
    attempts = i * 10
    print(i,"번째 시도")
    rate = culculation(attempts, num)
    plt.scatter(attempts, rate)
plt.xlabel('attempts')
plt.ylabel('rate')
plt.yticks(np.arange(0,1,0.1))
plt.title('Culculation of Derangement Permutation, Shuffle: ' + str(num) + " About " + str(round(rate*math.factorial(num), 3)))
plt.show()