#What i do
def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'
    
#Best way to do
def bool_to_word(bool):
    return "Yes" if bool else "No"
