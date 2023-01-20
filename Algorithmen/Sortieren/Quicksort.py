def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


################
# Testcode

def testcode1():

    arr = [2, 4, 63, 34, 7, 34, 6, 32, 1, 6, 89]

    print(f"Unsortiert:\t{arr}")
    print(f"Sortiert:\t{quick_sort(arr)}")


def testcode2():
    with open("Algorithmen/Sortieren/peformancetests/IntSet.txt", 'r') as f:
        strarr = f.readlines()

    arr = [int(x) for x in strarr]

    quick_sort(arr)


testcode2()