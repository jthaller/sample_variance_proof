#I recently learned that when calculating the sample variance, people
#divide by n-1 instead of n, where n is the sample size. This is to correction
#for the liklihood that your sample will underestimate variance.
#After looking at the analytic proof, I decided to quickly write something to
#check if this is true by creating a big data set with random numbers.

#what I actually found was that the variance for the sample tended to be way
#higher than the variance of the population. Sometimes they were similar, but
#never was the sample variance << population vairace.

import random
from numpy import zeros
import numpy as np

# int_max = the max number in the random generator
# int_step = step size in random generator
# N = sample size (number of columns)
# samp_splits = number of rows. I calculate the variance for each samp_split
int_max,int_step,N,samp_splits = 2000,17,10000,50
full_array =  fill_array(int_max,int_step,N,samp_splits)

def fill_array(int_max,int_step,N,samp_splits):
    table = zeros([samp_splits,N])
    for i in range(0,N):
        for j in range (0,samp_splits):
            table[j][i] = random.randrange(1,int_max,int_step)
    return table

print(full_array)


def get_sample_variance(single_array):
    n = len(single_array)
    mean = np.mean(single_array)
    print('mean: ' + str(mean))
    sum_dif = 0
    for i in range(0,len(single_array)):
        sum_dif = (single_array[i] - mean)**2
    print('divided by n: {}\ndivided by n-1: {}' .format(sum_dif/n, sum_dif/((n-1))) )
    normal = sum_dif/n
    correction = sum_dif/(n-1)
    return  normal,correction


def get_population_variance(full_array):
    splits = len(full_array)
    samp_size = len(full_array[1,:])
    sum = 0
    N = splits * samp_size
    sum = sum + np.sum(full_array)
    mean = sum/N
    print("mean: % f" %(mean))
    for i in range(splits):
        for j in range(samp_size):
            sum_dif = (full_array[i][j] - mean)**2
    print("True variance: % f" %(sum_dif/N))


#print the variance if divided by n or n-1 for each sample 
for i in range(0,len(full_array[:,1])):
    get_sample_variance(full_array[i])
    print("----------------------------------")

get_population_variance(full_array)
