Change Log
=============

[1.0.8]- 01/11/2022
-------------------

- [ADDED] Users may now indicate only a fixed value for w,c1 and c2.
- [ADDED] New initial solution method: Mean value between boundaries
- [CHANGED] Default penalty value is now 1000000
- [CHANGED] Default w value is now 0.7
- [CHANGED] Default c1 and c2 value is now 1.0

[1.0.7]- 14/01/2022
-------------------

- [FIX] Small correction done for when the perc_repair = 1
- [FIX] Corrected penalty value after a direct repair function when the brm_function is 1 or 2.

[1.0.6]- 12/01/2022
-------------------

- [FIX] Corrected cases where the solution was not updated after the direct repair function
- [CHANGE] Changed the percentage repair variable influence to be in line with its description

[1.0.5]- 10/01/2022
-------------------

- [ADDED] Users may now indicate the number of jobs for multiprocessing
- [ADDED] The results of the PSO now show the total and the average execution times of the algorithm
- [CHANGED] Multiprocessing of the trials of the PSO no longer requires "if __name__ == '__main__':" in the main module to work
- [CHANGED] New dependency added: joblib

[1.0.4]- 07/01/2022
-------------------

- [FIX] Corrected boundary control function: random reinitialization
- [FIX] Corrected boundary control function: adaptive penalty
- [CHANGED] Changed documentation regarding the boundary control function parameter

[1.0.3]- 22/12/2021
-------------------

- [ADDED] Multiprocessing to trials of the PSO
- [CHANGED] Corrected small details in documentation
- [CHANGED] Velocity update functions
- [CHANGED] Results are now presented in scientific notation for very small values

[1.0.2]- 20/12/2021
-------------------

- [CHANGED] Name of some variables according to literature
- [CHANGED] Presentation of the results of the PSO
- [FIX] Corrected some names presented in the documentation
 
[1.0.1]- 20/12/2021
-------------------

- Initial release