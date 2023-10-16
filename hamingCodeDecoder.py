#decode hamming codes

def arrayErrorCheck(array):
    total1s = 0
    for i in array:
        try: #Try if 2d array (full array)
            for j in i:
                if j == 1:
                    total1s = total1s+1
        except: #Except, will try for a 1D array
            if i == 1:
                total1s = total1s+1
    if total1s % 2 == 0: #Has no errors if %2 = 0, ∴ return false
        return False
    else:
        return True

def checkColumn13(array):
    array1 = []
    array3 = []
    
    for i in array:
        array1.append(i[1])
        array3.append(i[3])
    array1Check = arrayErrorCheck(array1)
    array3Check = arrayErrorCheck(array3)
    
    return(array1Check, array3Check)

def main():

    array = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
        ]
    hasErrors = arrayErrorCheck(array)
    print(hasErrors)
    
    check13 = checkColumn13(array)
    print(check13)
    
main()
