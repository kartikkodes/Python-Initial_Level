def return_number(statemnet1):
    result = []
    for i in statemnet1.split():
        if i.isdigit():
            result.append(i) 
    return result    

str1 = 'red 12 black 45 green'
print(return_number(str1))
