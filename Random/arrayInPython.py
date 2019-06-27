#A simple program that plays around with array in Python

def printArr(myList): #Print whole array
    for x in myList:
        print(x,"",end='')

myList = ["|BEGIN|","|Bougdanov|",'a',3.142,"END\n"]
myList.append("Reversal-Bull-Flag") #Work like a push_back
printArr(myList)

myList.reverse() #Reverse the order of the array
printArr(myList)

myList.pop(2) #this remove the index element array pop
printArr(myList)

dopeList = [1,2,3,['a','b','c',[6,6,6]]] #Array in Python can be instantiated as shown
print("\n"+ str(dopeList[3][3][1]))