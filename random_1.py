import numpy as np
import matplotlib.pyplot as plt

def normal_random():
    li = np.random.normal(0, 1, 10000)
    li.sort()
    return li

def binomal_random():
    li = np.random.binomial(1, 0.7, 10000)
    li.sort()
    return li

# plot a list of numbers
def draw(li_num):
    plt.hist(li_num, bins=10)
    plt.show()

draw(binomal_random())
