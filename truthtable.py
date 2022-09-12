from tabulate import tabulate

#parameters
print("please provide an option 1) print output, 2)print proof of output, 3) print complete truth table")
input1 = input()
opPrint = int(input1)
print("please provide size of adder")
input2 = input()
addSize = int(input2)
stringSize = '0' + str(addSize) + 'b'
stringSizeTable = '0' + str(2 * addSize) + 'b'


#truth table for a 4 bit sign magnitude adder
inputa = 0
inputb = 0
temp =0
newSum = 0
j = 0
listSum = []
listTabulated = []

#function to append correct sign and magnitude 

def appendNummag (sum,temp1,signindex,a,b,oriNum,listTemp):

    if temp1 == 0:
            listTemp.append((a,b,oriNum[0],oriNum[addSize],temp1, '0' + sum[1:]))
            
    else:
            listTemp.append((a,b,oriNum[0], oriNum[addSize], temp1,(oriNum[signindex]+ sum[1:])))

#print option

def printOption (op,listTemp):
#print only output of truth table
    if op == 1:
        print("Output")
        for y in range(len(listTemp)):
            print(listTemp[y][5])


#print proof of truth table
    elif op == 2:

        print(tabulate(listSum, headers = ["a","b","signa","signb","sum","result"]))

#print complete truth table
    elif op == 3:

        print("Input    ","Output")
        for y in range(len(listTemp)):
            print(listTabulated[y][0],listTabulated[y][1],listTemp[y][5])


    

for x in range(2** (2*addSize)):

    j = format(x,stringSizeTable)
    listTabulated.append((j[0:addSize],j[addSize:]))
    inputa = int(j[1:addSize],2)
    inputb = int(j[addSize+1:],2)

    #part to deal with the same sign positive or negative
    if j[0] == j[addSize]:
        temp = (inputa + inputb)
        newSum = format(temp,stringSize)
    #to deal with overflow we only take the last three bits of a 4 bit number
        appendNummag(newSum,temp,0,inputa, inputb,j,listSum)
    #part to deal with different sign 
    else:

        if (inputa > inputb):

            temp = (inputa - inputb)
            newSum = format(temp,stringSize)
            appendNummag(newSum,temp,0, inputa, inputb,j,listSum)
                        
        else:

            temp = (inputb - inputa)
            newSum = format(temp,stringSize)
            appendNummag(newSum,temp,addSize, inputa, inputb,j,listSum)
            


printOption(opPrint,listSum)

        