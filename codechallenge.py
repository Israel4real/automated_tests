def notIndexOf(givenString, value):
    for i in range(len(value)-1):
        if givenString[i] == value[i] and givenString[i] != ' ':
            givenString = givenString[1:]
            print(givenString)
            notIndexOf(givenString, value)
        else:
            pass
    
    return position
            
            
        