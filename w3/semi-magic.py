import pdb
from csp import *
from random import shuffle

def solve_semi_magic(algorithm=backtracking_search, **args):
    """ From CSP class in csp.py
        vars        A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
                    """
    # Use the variable names in the figure
    csp_vars = ['V%d'%d for d in range(1,10)]
    shuffle(csp_vars)

    #########################################
    # Fill in these definitions

    csp_domains = {}
    for var in csp_vars:
        csp_domains[var] = [1,2,3]

    csp_neighbors = {
    'V1':['V2', 'V3', 'V4', 'V7', 'V5', 'V9'],
    'V2': ['V1', 'V3', 'V5', 'V8'],
    'V3': ['V1', 'V2', 'V6', 'V9'],
    'V4': ['V1', 'V7', 'V5', 'V6'],
    'V5': ['V1', 'V9', 'V2', 'V8', 'V4', 'V6'],
    'V6': ['V4', 'V5', 'V3', 'V9'],
    'V7': ['V1', 'V4', 'V8', 'V9'],
    'V8': ['V2', 'V5', 'V7', 'V9'],
    'V9': ['V1', 'V5', 'V3', 'V6', 'V7', 'V8']
    }

    def csp_constraints(A, a, B, b):
        return a != b

    #########################################

    csp = CSP(csp_vars, csp_domains, csp_neighbors,
              csp_constraints)

    # run the specified algorithm to get an answer (or None)
    ans = algorithm(csp, **args)
    
    print('number of assignments', csp.nassigns)
    assign = csp.infer_assignment()
    assignment_list = []
    if assign:
        for x in sorted(assign.items()):
            assignment_list.append(x)
    print(assignment_list)
    return csp



if __name__ == "__main__":

    # Q1
    print("\nPure Backtracking")
    solve_semi_magic()

    # Q2
    print("\nBacktracking with Minimum Remaining Values")
    solve_semi_magic(select_unassigned_variable=mrv)
    print("\nBacktracking with Least Constraining Value")
    solve_semi_magic(order_domain_values=lcv)
    print("\nBacktracking with MRV and LCV")
    solve_semi_magic(select_unassigned_variable=mrv, order_domain_values=lcv)
    print("\nBacktracking with Forward Checking")
    solve_semi_magic(inference=forward_checking)
    print("\nBacktracking with AC-3")
    solve_semi_magic(inference=mac)
    print("\nBacktracking with MRV, LCV and AC-3")
    solve_semi_magic(select_unassigned_variable=mrv, order_domain_values=lcv, inference=mac)




