import time
def sum_of_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
        end_time = time.time()
        return s,end_time - start_time
n=5
print("Time required to calculate sum of 1 to",n,"is",sum_of_numbers(5))
