__author__ = 'hyw356'

import numpy
from math import exp, pi, sqrt, sin
from untitled.michaelwicz_function import Michaelwicz_function


def alpha_new(alpha, NGen):
    # % alpha_n=alpha_0(1-delta)^NGen=10^(-4);
    # % alpha_0=0.9
    d = 1 - (10 ** (-4) / 0.9) ** (1 / NGen);
    alpha = (1 - d) * alpha
    return alpha


def second(no_fireflies, maxGeneration, dimension):
    # General parameters

    # n=50 #number of fireflies
    # dim=30 #dim
    # lb=-50
    # ub=50
    # MaxGeneration=500

    # FFA parameters
    alpha = 0.2  # Randomness 0--1 (highly random)
    beta0 = 1  # minimum value of beta
    gamma = 1  # Absorption coefficient

    # objective function valu parameters
    Ub = 4
    Lb = 0
    delta = 0.05 * (Ub - Lb)
    objective_function = Michaelwicz_function()

    fireflies = numpy.zeros(no_fireflies)
    Light_intensity = numpy.zeros(no_fireflies)

    # random locations for fireflies
    fireflies_location = numpy.random.uniform(0, 1, (no_fireflies, dimension)) * (Ub - Lb) + Lb

    for G in range(0,maxGeneration):

         alpha = alpha_new(alpha,maxGeneration)

         for i in range (0,no_fireflies):
             fireflies[i] = objective_function.compute(fireflies_location[i,:],dimension)
             Light_intensity[i] = fireflies[i]


         # Ranking fireflies by their light intensity
         Light_intensity = numpy.sort(fireflies)
         light_intensity_sorted_index = numpy.argsort(fireflies)
         fireflies_location = fireflies_location[light_intensity_sorted_index,:]

         # Make a copy of the fireflies_ location & light_intensity
         light_intensity_copy = Light_intensity
         fireflies_location_copy = fireflies_location

         # Find the current best location and itensity
         light_intensity_best = Light_intensity[0]
         fireflies_location_best = fireflies_location[0,:]


         #Move all fireflies to the better locations

         for i in range (0,no_fireflies):
             for j in range (0,no_fireflies):
                 if Light_intensity[i] > light_intensity_copy[j]:
                     distance_betweet_Fi_Fj= numpy.sqrt(numpy.sum((fireflies_location[i,:]-fireflies_location[j,:])**2))
                     beta = beta0 * exp(-gamma*distance_betweet_Fi_Fj**2)
                     e = delta * numpy.random.uniform(-1,+1,dimension)

                     a = numpy.random.uniform(0,1,(dimension,dimension))
                     b = fireflies_location[j,:] - fireflies_location[i,:]
                     fireflies_location = fireflies_location[i,:] + beta * numpy.multiply(a,b) + alpha * e

                     #check the poundries
                     fireflies_location = numpy.clip(fireflies_location, Lb, Ub)

                     Light_intensity = objective_function.compute(fireflies_location[i,:],dimension)


         print("best value:",light_intensity_best)
         print("best location",fireflies_location_best)
#if __name__ == '__main__':








