import numpy as np
import matplotlib.pyplot as plt


def normal_random(mean=1,std=0.5):
    r = -1
    while (r<0.8*mean or r>3*mean):
        r = np.random.normal(mean, std, 1)
    return r[0]

def binomal_random():
    li = np.random.binomial(1, 0.7, 10000)
    li.sort()
    return li

# plot a list of numbers
def draw(li_num):
    plt.hist(li_num, bins=50)
    plt.show()

normal_list = []

for i in range (10000):
    normal_list.append(normal_random(5))

# draw normal_list
draw(normal_list)