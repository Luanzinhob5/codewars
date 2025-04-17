#The way i did
def positive_sum(arr):
    positivos = 0
    for i, number in enumerate(arr):
        if arr[i] < 0:
            positivos += arr[i]
    return positivos

#Best Way
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
