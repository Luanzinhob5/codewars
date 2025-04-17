# My code
def get_count(sentence):
    vowels = 'aeiou'
    sentence.lower
    total = 0
    for letter in sentence:
        if letter in vowels:
            total += 1
    return total



# Best Pratice
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")