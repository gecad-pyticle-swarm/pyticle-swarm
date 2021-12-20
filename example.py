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

initial_solution        = []
brm_function            = 4
direct_repair           = None
perc_repair             = 0
wmax                    = 0.5
wmin                    = 0.1
c1min                   = 0
c1max                   = 0.4
c2min                   = 0.1
c2max                   = 2
n_iterations            = 100
n_particles             = 10
n_runs                  = 30
show_fitness_graphic    = False
show_particle_graphics  = False
"""

# Run PSO
res = run_pso(n_vars, fitness_function=func, low_bounds=low_bounds, up_bounds= up_bounds, c1min = 0.4, c1max = 1, c2min = 0.3, 
            c2max = 0.4, wmax = 0.3, wmin = 0.1, brm_function=1, show_fitness_grapic=True)

# Print results
"""
Results:

res.fitness_value is a float correspending to the best fitness value with size = 1 
res.it_fitness_value is a array with all the fitness values of the best execution with size = n_iterations
res.solution is the solution correspoding to best fitness value with size = n_vars
res.exec_times is the time of execution of the algorithm for best execution with size = 1 
"""
print("Best fitness value: " + str(res.fitness_value))
print("Solution: " + str(res.solution))
print("Execution time: " + str(res.exec_times))
