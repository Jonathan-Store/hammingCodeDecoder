#decode hamming codes

import tkinter as tk

def locateError(array,checkC13,checkC23,checkR13,checkR23):
    
    #update index for where error is
    
    if checkC13 == False and checkC23 == False:
        errorLocationC = 0
    elif checkC13 == True and checkC23 == False:
        errorLocationC = 1
    elif checkC13 == False and checkC23 == True:
        errorLocationC = 2
    else:
        errorLocationC = 3
    
    
    if checkR13 == False and checkR23 == False:
        errorLocationR = 0
    elif checkR13 == True and checkR23 == False:
        errorLocationR = 1
    elif checkR13 == False and checkR23 == True:
        errorLocationR = 2
    else:
        errorLocationR = 3
    
    
    #fix errors
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
    #create a single array containing all values from the columns 1,3 and see if there are errors
    array1 = []
    array3 = []
    
    for i in array:
        array1.append(i[1])
        array3.append(i[3])
    combinedArray = [array1,array3]
    
    
    checkArray = arrayErrorCheck(combinedArray)
    
    if checkArray == False:
        return(False)
    else:
        return(True)
    

def funCheckColumn23(array):
    #create a single array containing all values from the columns 2,3 and see if there are errors
    array2 = []
    array3 = []
    
    for i in array:
        array2.append(i[2])
        array3.append(i[3])
    
    combinedArray = [array2,array3]
    
    
    checkArray = arrayErrorCheck(combinedArray)
    
    if checkArray == False:
        return(False)
    else:
        return(True)
    

def funCheckRow13(array):
    #create a single array containing all values from the rows 1,3 and see if there are errors
    array1 = array[1]
    array3 = array[3]
    
    combinedArray = [array1,array3]
    
    combinedCheck = arrayErrorCheck(combinedArray)
    
    if combinedCheck == False:
        return(False)
    else:
        return(True)

def funCheckRow23(array):
    #create a single array containing all values from the rows 2,3 and see if there are errors
    array2 = array[2]
    array3 = array[3]
    
    combinedArray = [array2,array3]
    
    combinedCheck = arrayErrorCheck(combinedArray)
    
    if combinedCheck == False:
        return(False)
    else:
        return(True)
    
    
def main():
    #create array and pass it to required locations

    def changeButton(button):
        print("yes")
        if button.cget('text') == 0:
            button.config(text = 1)
        else:
            button.config(text = 0)
    
    window = tk.Tk()
    
    button0 = tk.Button(width = 3, height = 3,text = 0)
    button0.grid(row=1,column=1)
    button0.configure(command = changeButton(button0))
    button1 = tk.Button(width = 3, height = 3,text = 0).grid(row=1,column=2)
    button2 = tk.Button(width = 3, height = 3,text = 0).grid(row=1,column=3)
    button3 = tk.Button(width = 3, height = 3,text = 0).grid(row=1,column=4)
    
    button4 = tk.Button(width = 3, height = 3,text = 0).grid(row=2,column=1)
    button5 = tk.Button(width = 3, height = 3,text = 0).grid(row=2,column=2)
    button6 = tk.Button(width = 3, height = 3,text = 0).grid(row=2,column=3)
    button7 = tk.Button(width = 3, height = 3,text = 0).grid(row=2,column=4)
    
    button8 = tk.Button(width = 3, height = 3,text = 0).grid(row=3,column=1)
    button9 = tk.Button(width = 3, height = 3,text = 0).grid(row=3,column=2)
    button10 = tk.Button(width = 3, height = 3,text = 0).grid(row=3,column=3)
    button11 = tk.Button(width = 3, height = 3,text = 0).grid(row=3,column=4)
    
    button12 = tk.Button(width = 3, height = 3,text = 0).grid(row=4,column=1)
    button13 = tk.Button(width = 3, height = 3,text = 0).grid(row=4,column=2)
    button14 = tk.Button(width = 3, height = 3,text = 0).grid(row=4,column=3)
    button15 = tk.Button(width = 3, height = 3,text = 0).grid(row=4,column=4)
    
    

    array = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
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
    
    window.mainloop()
    
main()
