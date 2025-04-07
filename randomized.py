import random

def merge_sort():
    pass

def permute_by_sorting(a):
    n = len(a)
    new_a = [0 for _ in range(n)]
    for i in range(n):
        new_a[i] = random(1, n*n*n)
    merge_sort(new_a)
    pass

def randomize_in_place(a):
    n = len(a)
    for i in range(n):
        swap(a[i], a[random(i, n)])

def swap(a, b):
    pass

