import random
import time

from task1.make_queries import make_queries
from task1.LRUCache.LRUCache import LRUCache
from task1.functions.functions_cache import update_with_cache,range_sum_with_cache
from task1.functions.functions_no_cache import update_no_cache,range_sum_no_cache

def run_test():
    N = 100_000
    Q = 50_000
    CACHE_CAPACITY = 1000

    array_base = [random.randint(1, 100) for _ in range(N)]
    queries = make_queries(N, Q)

    #No cache
    array_no_cache = array_base.copy()
    start = time.perf_counter()
    for q in queries:
        if q[0] == "Range":
            range_sum_no_cache(array_no_cache, q[1], q[2])
        else:
            update_no_cache(array_no_cache, q[1], q[2])
    time_no_cache = time.perf_counter() - start

    #With cache
    array_with_cache = array_base.copy()
    cache = LRUCache(CACHE_CAPACITY)
    start = time.perf_counter()
    for q in queries:
        if q[0] == "Range":
            range_sum_with_cache(array_with_cache, q[1], q[2], cache)
        else:
            update_with_cache(array_with_cache, q[1], q[2], cache)
    time_with_cache = time.perf_counter() - start


    speedup = time_no_cache / time_with_cache if time_with_cache > 0 else 0

    print(f"Без кешу :  {time_no_cache:.2f} c")
    print(
        f"LRU-кеш  :   {time_with_cache:.2f} c  (прискорення ×{speedup:.1f})")


if __name__ == "__main__":
    run_test()
