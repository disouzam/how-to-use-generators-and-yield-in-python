"""
Docstring for 06-profiling-generator-performance

Quote from Real Python article:

Here, you can see that summing across all values in the list comprehension took about 
a third of the time as summing across the generator. 

If speed is an issue and memory isn’t, then a list comprehension is likely a better tool for the job.

https://realpython.com/introduction-to-python-generators/#profiling-generator-performance
"""

import cProfile
cProfile.run('sum([i * 2 for i in range(10000)])')


cProfile.run('sum((i * 2 for i in range(10000)))')
