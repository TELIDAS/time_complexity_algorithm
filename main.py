import time
import big_o


class Algorithm:
    ARRAY = [1, 2, 4, 5, 7, 8, 9, 10]
    UNSORTED_ARRAY = [10, 9, 8, 7, 5, 4, 2, 1]

    # method for unsorted list
    def get_missing_numbers_of_unsorted_list(self, arr: list) -> None:
        scope = range(min(arr), max(arr) + 1)
        unsorted = sorted(list(set(scope) - set(arr)))
        print(unsorted)

    # method for sorted list
    def get_missing_numbers_of_sorted_list(self, arr: list) -> None:
        scope = range(min(arr), max(arr) + 1)
        sorted_list = list(set(scope) - set(arr))
        print(sorted_list)


if __name__ == '__main__':
    alg = Algorithm()
    start_unsorted = time.time()
    alg.get_missing_numbers_of_unsorted_list(alg.UNSORTED_ARRAY)
    time_of_first_func = time.time() - start_unsorted
    print(f"Execution time of unsorted list: {time_of_first_func}")

    start_sorted = time.time()
    alg.get_missing_numbers_of_sorted_list(alg.ARRAY)
    time_of_second_func = time.time() - start_sorted
    print(f"Execution time of sorted list: {time_of_second_func}")

    """ Big O notation time complexity """
    # positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
    # best, others = big_o.big_o(alg.get_missing_numbers_of_sorted_list, positive_int_generator, n_repeats=100)
    # print(best)
