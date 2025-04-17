# How i did
def solution(number):
    numbers = 0
    i = 0
    while i <= number:
        if i / 3 == int(i / 3) or i / 5 == int(i/5) :
            numbers += i
            i +=1
        else:
            i +=1
    return numbers

# best way to do

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)