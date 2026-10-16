
# C2: Parallel Resistance

def parallel_resistance(resistors):
    reciprocal_sum = 0
    for resistance in resistors:
        reciprocal_sum += 1 / resistance
    return 1 / reciprocal_sum
 
 
print("parallel_resistance([10, 10]) ->", round(parallel_resistance([10, 10]), 2))
print("parallel_resistance([100, 200, 300]) ->", round(parallel_resistance([100, 200, 300]), 2))
