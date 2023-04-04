import random


def randomArr():
    return [random.randint(1, 20) for _ in range(20)]


def sort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sort1(arr):
    size = len(arr)
    for i in range(size - 1):
        index = i
        for j in range(i + 1, size):
            if arr[index] > arr[j]:
                index = j
        if index != i:
            arr[index], arr[i] = arr[i], arr[index]


def sort2(arr):
    size = len(arr)
    for i in range(1, size):
        index = i
        while index - 1 >= 0 and arr[index-1] > arr[index]:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1


if __name__ == '__main__':
    data = randomArr()
    print(data)
    sort2(data)
    print(data)
