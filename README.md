# Package description

A wrapper for c++ to solve the Traveling Salesman Problem

## Installation
`pip install tsp-c`

## Available methods
* Greedy
* Simulated Annealing (SA)
* Particle Swarm Optimization (PSO)
* Ant Colony Optimization (ACO)
* Two-opt Heuristic

## Available functions
	solve_greedy(distance_matrix)
	solve_SA(distance_matrix)
	set_param_SA(C0, Cmin, L0, alpha)
	solve_PSO(distance_matrix)
	set_param_ACO(hconst, alpha, beta, evprate, intsty, nAnt, nItr)
	solve_ACO(distance_matrix)
	solve_two_opt(distance_matrix)
	set_param_PSO(w, c1, c2, maxV, muProb, nPar, nItr)

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
* C0 = Initial temperature (default = 20.0)
* Cmin = Final temperature (default = 0.1)
* L0 = Number of iterations in each temperature (default = 10000)
* alpha = cooling rate (default = 0.9)

For example:

	
	tsp.set_param_SA(10.0, 0.01, 10000, 0.95)
	
	
To set the parameters of the ACO method, use:

	
	tsp.set_param_ACO(hconst, alpha, beta, evprate, intsty, nAnt, nItr)
	

where
* hconst = Heuristic Constant (default = 50.0)
* alpha = Pheromone influence (default = 3, min = 0.0001, max = 10.0)
* beta = Heuristic influence (default = 5, min = 0.0001, max = 10.0)
* evprate = Evaporation Rate (default = 0.05)
* intsty = Pheromone intensity (default = 0.1)
* nAnt = Number of ants (default = 50)
* nItr = Number of iterations (default = 100)

For example:

	
	tsp.set_param_ACO(100.0, 5, 4, 0.1, 0.15, 200, 200)
	

To set the parameters of the PSO method, use:

	
	tsp.set_param_PSO(w, c1, c2, maxV, muProb, nPar, nItr)
	

where
* w = Inertia weight of the particle (default = 1.0)
* c1 = acceleration coefficient for the local best position (default = 2.0)
* c2 = acceleration coefficient for the global best position (default = 2.0)
* maxV = Maximum velocity of the particles (default = 2.0)
* muProb = mutation probability that change the position of a particle (default = 0.05)
* nPar = Number of particles (default = 100)
* nItr = Number of iterations (default = 5000)

For example:

	
	tsp.set_param_PSO(0.8, 1.5, 1.5, 5, 0.1, 200, 1000)
	
	
## Requirement
python >=3.6

## Operating System
Linux

## References
* Janjarassuk, Udom. (2011). A comparison of heuristic approaches to the travelling salesman problem. ICIC Express Letters. 5. 279-283. 