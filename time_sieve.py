import time
from typing import List, Set
from flavius import sieve_flavius


def get_time_flavius(flav_numb: List | Set) -> float:
    """
    Here we investigate the diff between lists and sets
    """
    print(f"Flavius numbers as a {str(type(flav_numb)).split()[1][:-1]}")
    start = time.time()
    count = 0
    for i in range(num+1):
        if i in flav_numb:
            count += 1
    end = time.time()
    time1 = end - start
    print(f"count = {count}, time of execution = {time1:0.5f} seconds")
    return time1

if __name__ == '__main__':
    num = 100000
    list_flavius = sieve_flavius(num)
    print(f"If num={num}, sets ran about \
{round(get_time_flavius(list_flavius)/get_time_flavius(set(list_flavius)))} \
times faster than lists!")
