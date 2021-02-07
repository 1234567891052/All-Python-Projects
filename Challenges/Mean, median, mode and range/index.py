import statistics

def mean(arr):
    print('Mean: ' + str(sum(arr)/len(arr)))

def median(arr):
    if len(arr) % 2 == 0 :
        middle = [arr[int(len(arr)/2)], arr[int(len(arr)/2 - 1)]]
        print('Median: ' + str((middle[0] + middle[1])/2))
    else :
        print('Median: ' + str(arr[int((len(arr) + 1) / 2 - 1)]))

def m(arr):
    print(statistics.mode(arr))

def update(arr):
    arr.sort()
    mean(arr)
    median(arr)
    m(arr)

update([1, 1, 2, 2, 3])