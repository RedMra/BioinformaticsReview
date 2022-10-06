def fibonacci_loop_pythonic(months, offspring):
    parrent, child = 1, 1
    for itr in range(months - 1):
        child,parrent =parrent,parrent + (child * offspring)
    return child


print (fibonacci_loop_pythonic(29, 5))

"""O - small (children) rabbit. They have to mature and reproduce in the next cycle only
0 - mature (parents) rabbit. they con reproduce and move to the next cycle
"""