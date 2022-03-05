# Package description

A wrapper for c++ to solve the Traveling Salesman Problem

## Installation
`pip install tsp-c`

## Examples
To solve the problem with the Greedy method:

	
	import tsp_c as tsp

	distance_matrix = [
		[0.0, 290.7, 254.9, 172.9],
		[263.6, 0.0, 508.3, 185.0],
		[258.2, 497.1, 0.0, 405.6],
		[136.8, 190.7, 394.8, 0.0]
	]

	sol, distance = tsp.solve_greedy(distance_matrix)
	print("\nSolution from Greedy:")
	print(distance, " ", sol)
	

The solution will be   `(1, 3, 0, 2)` with total distance 1073.8000000000002.

To solve the problem with the Simulated Annealing method, change the code to:

	
	sol, distance = tsp.solve_SA(distance_matrix)
	

To set the parameters of the Simulated Annealing method, use:

	
	tsp.set_param_SA(C0, Cmin, L0, alpha)
	

where
* C0 = Initial temperature
* Cmin = Final temperature
* L0 = Number of iterations in each temperature
* alpha = cooling rate

For example:

	
	tsp.set_param_SA(10.0, 0.01, 10000, 0.95)
	

## Requirement
python >=3.6

## Operating System
Linux
