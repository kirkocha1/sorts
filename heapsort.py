__author__ = 'kochanik'
import random


def parent(i):
    return i % 2


def left_child(i):
    return i * 2 + 1


def right_child(i):
    return i * 2 + 2


def heapify(a, pos, length):
    max_index = pos
    if max_index == 0:
        l=1
        r=2
    else:
        l = left_child(pos)
        r = right_child(pos)

    if (l <= length) and (a[max_index] < a[l]):
        max_index = l

    if (r <= length) and (a[max_index] < a[r]):
        max_index = r

    if max_index != pos:
        a[pos], a[max_index] = a[max_index], a[pos]
        heapify(a, max_index, length)


def buildheap(a, length):
    pos = length
    per = pos % 2
    if per == 0:
        pos = int(pos/2) - 1
    else:
        pos = int(pos/2)

    while pos >= 0:
        heapify(a, pos, length)
        pos -= 1


def heapsort(a):
    length = len(a)-1
    buildheap(a,length)
    while(length > 0):
        a[0], a[length] = a[length], a[0]
        length -= 1
        heapify(a, 0, length)
    return a


def main():
    i = 0
    mass = []
    while (i <= 32):
        mass.append(random.randint(1,600))
        i+=1
    print(mass)
    print(heapsort(mass))


if __name__=='__main__':
    main()









