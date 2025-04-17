# My code
def printer_error(s):
    error = 'nopqrstuvwxyz'
    count_error = 0
    for letter in s:
        if letter in error:
            count_error += 1

    return f'{count_error}/{len(s)}'

#Best Pratice
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

# With library
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

