#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        target = limit - weights[i]

        complement = hash_table_retrieve(ht, target)

        if complement is not None:
            return (complement, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
