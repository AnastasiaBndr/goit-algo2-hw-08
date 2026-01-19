from task1.LRUCache import LRUCache

from task1.LRUCache import LRUCache


def range_sum_with_cache(array, left, right, cache: LRUCache):
    key = (left, right)

    cached = cache.get(key)
    if cached != -1:
        return cached

    result = sum(array[left:right + 1])
    cache.put(key, result)
    return result


def update_with_cache(array, index, value, cache: LRUCache):
    array[index] = value

    keys_to_delete = []

    for left, right in cache.cache.keys():
        if left <= index <= right:
            keys_to_delete.append((left, right))

    for key in keys_to_delete:
        node = cache.cache.pop(key)
        cache.list.remove(node)
