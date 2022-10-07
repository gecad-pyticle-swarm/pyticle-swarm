# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:35:46 2021

@author: Bruno Veiga
"""
from pyticleswarm import run_pso
import numpy as np
#import benchmark_functions as bf

# Example 1

# Define fitness function
def func(x):
    # hypersphere function
    f = np.sum(x**2)

    return f
# or a benchmark can also be used
#func = bf.Hypersphere(n_dimensions=2)

# Create variables
n_vars= 2
low_bounds = -5.12
up_bounds = 5.12
# or for the benchmark function
# n_vars=func.n_dimensions()
# m = func.suggested_bounds()
# low_bounds = m[0]
# up_bounds = m[1]

""" 
Stantard parameters values:

initial_solution        = []    Matrix or array containing the initial solutions or solution
generate_int_pop        = 1     Type of initial population generation
brm_function            = 4     Function to handle boundary constraint violation
penalty                 = 10    Brick wall penalty value or adaptive penalty offset
n_jobs                  = -2    Number of concurrently running jobs
direct_repair           = None  The direct repair function
perc_repair             = 0     Value between 0 and 1 that determines the percentage of iterations starting from the end where a repair function is applied
wmax                    = 0.5   The maximum value of the inertia weight
wmin                    = 0.1   The minimum value of the itertia weight
c1min                   = 0     Minimum value of the acceleration coefficient c1
c1max                   = 0.4   Maximum value of the acceleration coefficient c1
c2min                   = 0.1   Minimum value of the acceleration coefficient c2
c2max                   = 2     Maximum value of the acceleration coefficient c1 
n_iterations            = 100   The total number of iterations
n_particles             = 10    The total number of particles
n_trials                = 30    The total number of trials
show_fitness_graphic    = False Boolean that indicates if the fitness graphic is to be shown or not
show_particle_graphics  = False Boolean that indicates if the particles graphics are to be shown or not (Only works with solutions of 2 dimensions)
"""
# Run PSO
res = run_pso(n_vars, fitness_function=func, low_bounds=low_bounds, up_bounds= up_bounds, c1min = 0.4, c1max = 0.6, c2min = 0.4, generate_int_pop=1,penalty=1000000,
            c2max = 0.6, wmax = 0.6, wmin = 0.4, n_iterations=100,n_particles=100, brm_function=4, show_fitness_grapic=True,n_jobs=-2, )

# Print results
"""
Results:

res.fitness_value is a float correspending to the best fitness value with size = 1 
res.it_fitness_value is a array with all the fitness values of the best execution with size = n_iterations
res.solution is the solution correspoding to best fitness value with size = n_vars
res.tot_exec_time is the total of time of execution of the algorithm with size = 1 
res.avg_exec_time is the average of time of execution of the algorithm with size = 1
"""

