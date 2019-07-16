import numpy as np
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint

unit_cost = [0, 4, 1, 
             1, 6, 3, 
             3, 7, 6]

def cost(x):
    return sum(np.multiply(x, unit_cost))

# obj_fun = lambda x: sum(np.multiply(x, unit_cost))
# constraints = []
loc1 = 300
A1 = np.array([1,1,1,
               0,0,0,
               0,0,0])
# constraints.append(LinearConstraint(0, A1.T, loc1))
loc2 = 600
A2 = np.array([0,0,0,
               1,1,1,
               0,0,0])
# constraints.append(LinearConstraint(0, A2.T, loc2))
loc3 = 500
A3 = np.array([0,0,0,
               0,0,0,
               1,1,1])
# constraints.append(LinearConstraint(0, A3.T, loc3))
loc4 = 600
A4 = np.array([1,0,0,
               1,0,0,
               1,0,0])
# constraints.append(LinearConstraint(loc4, A4.T, np.inf))
loc5 = 300
A5 = np.array([0,1,0,
               0,1,0,
               0,1,0])
# constraints.append(LinearConstraint(loc5, A5.T, np.inf))
loc6 = 500
A6 = np.array([0,0,1,
               0,0,1,
               0,0,1])
# constraints.append(LinearConstraint(loc6, A6.T, np.inf))
bnds = [(0, None) for i in range(9)]
constraints = [
               {'type': 'ineq', 'fun':lambda x: loc1 - A1.dot(x) },
               {'type': 'ineq', 'fun':lambda x: loc2 - A2.dot(x) },
               {'type': 'ineq', 'fun':lambda x: loc3 - A3.dot(x) },
               {'type': 'ineq', 'fun':lambda x: A4.dot(x) - loc4 },
               {'type': 'ineq', 'fun':lambda x: A5.dot(x) - loc5 },
               {'type': 'ineq', 'fun':lambda x: A6.dot(x) - loc6 },
               ]

supply_decision = [100, 100, 100, 
                   200 ,200, 200, 
                   300, 0 ,200]


total_cost = cost(supply_decision)
print(total_cost)

# res = minimize(cost, x0=supply_decision, bounds=bnds, constraints=constraints)
print(res)  
supply_decision = res['x']

total_cost = cost(supply_decision)
print(total_cost)
