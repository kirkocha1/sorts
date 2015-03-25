import random


def partition(a, l, r):
    if type(a) != type([]):
        raise TypeError

    pivot = a[l]
    i = l
    j = r

    while (i < j):

        if a[i] <= pivot:
            i += 1
            continue

        if a[j] > pivot:
            j -= 1
            continue

        a[i], a[j] = a[j], a[i]

    if a[l] > a[j]:
        a[l], a[j] = a[j], pivot
    else:
        a[l], a[i-1] = a[i-1], pivot

    return j


def quicksort(a, l, r):
        if r > len(a)-1:
            raise ValueError
        if (a == []):
            raise ValueError
        if (a == list()):
            raise ValueError
        if (l < 0) or (r < 0):
            return print ('wrong index')

        if (l < r):
            q = partition(a, l, r)
            quicksort(a, l, q - 1)
            quicksort(a, q, r)
            return a


def main():
    i = 0
    mass = []
    while (i <= 8):
        mass.append(random.randint(1,600))
        i+=1
    print(mass)
    print(quicksort(mass, 0, len(mass) - 1))


if __name__=='__main__':
    main()
