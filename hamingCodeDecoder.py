#decode hamming codes

def locateError(array,checkC13,checkC23,checkR13,checkR23):
    
    if checkC13 == False and checkC23 == False:
        errorLocationC = 0
    elif checkC13 == True and checkC23 == False:
        errorLocationC = 1
    elif checkC13 == False and checkC23 == True:
        errorLocationC = 2
    else:
        errorLocationC = 3
    
    
    if checkR13 == False and checkC23 == False:
        errorLocationR = 0
    elif checkR13 == True and checkC23 == False:
        errorLocationR = 1
    elif checkR13 == False and checkC23 == True:
        errorLocationR = 2
    else:
        errorLocationR = 3
    
    
    
    if array[errorLocationR][errorLocationC] == 1:
        array[errorLocationR][errorLocationC] = 0
    else:
        array[errorLocationR][errorLocationC] = 1
    
    return(array)
    
    
    
    

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

def funCheckColumn13(array):
    array1 = []
    array3 = []
    
    for i in array:
        array1.append(i[1])
        array3.append(i[3])
    array1Check = arrayErrorCheck(array1)
    array3Check = arrayErrorCheck(array3)
    
    if array1Check == False and array3Check == False:
        return(False)
    else:
        return(True)
    

def funCheckColumn23(array):
    array2 = []
    array3 = []
    
    for i in array:
        array2.append(i[2])
        array3.append(i[3])
    array2Check = arrayErrorCheck(array2)
    array3Check = arrayErrorCheck(array3)
    
    if array2Check == False and array3Check == False:
        return(False)
    else:
        return(True)
    

def funCheckRow13(array):
    array1 = array[1]
    array2 = array[3]
    
    array1Check = arrayErrorCheck(array1)
    array2Check = arrayErrorCheck(array2)
    
    if array1Check == False and array2Check == False:
        return(False)
    else:
        return(True)

def funCheckRow23(array):
    array2 = array[2]
    array3 = array[3]
    
    array2Check = arrayErrorCheck(array2)
    array3Check = arrayErrorCheck(array3)
    
    if array2Check == False and array3Check == False:
        return(False)
    else:
        return(True)
    
    
def main():

    array = [
        [0,0,0,0],
        [0,0,1,0],
        [0,0,0,0],
        [0,0,0,0]
        ]
    hasErrors = arrayErrorCheck(array)
    print("array:",hasErrors)
    
    checkColumn13 = funCheckColumn13(array)
    print("col13:",checkColumn13)
    checkColumn23 = funCheckColumn23(array)
    print("col23:",checkColumn23)
    checkRow13 = funCheckRow13(array)
    print("row13:",checkRow13)
    checkRow23 = funCheckRow23(array)
    print("row23:",checkRow23)

    if hasErrors == True:
        fixedArray = locateError(array,checkColumn13,checkColumn23,checkRow13,checkRow23)
        for i in fixedArray:
            print(i)
    else:
        print("Array has no errors")
    
main()
