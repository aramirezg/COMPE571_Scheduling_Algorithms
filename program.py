import sys
##
##file= open('input1.txt','r')
##fileOut = open('output1.txt', 'w')
##
##fileOut.write('hello test')
##
##fileLines = file.readlines()
##for lines in fileLines:
##        output = lines
##        print(lines, end= "")
##
##
##file.close()


    


def string2Int(stringArray):
    list1 = stringArray
    list2 = []

    for i in range(len(list1)):
        t = int(list1[i])
        list2.append(t)
    print("Converted string array to integer array")
    return list2


#LCM method to determine the LCM for the range of time for the scheduling
def LCM(numArray):
    
    numArray.sort()
        
    combo = numArray[0] * numArray[1] * numArray[2] * numArray[3]

    for x in range(numArray[3], combo + 1, numArray[3]):
        if x % numArray[0] == 0 and x % numArray[1] == 0 and x % numArray[2] == 0:
            return x
    
#RM check
def RM_Util(*args):
    hArray = []
    t1Array = []
    t2Array = []
    t3Array = []
    t4Array = []
    t5Array = []
    lcmArray = []
    
    hArray = args[0]
    t1Array = args[1]
    t2Array = args[2]
    t3Array = args[3]
    t4Array = args[4]
    t5Array = args[5]

    t1Deadline_Ex = []
    t2Deadline_Ex = []
    t3Deadline_Ex = []
    t4Deadline_Ex = []
    t5Deadline_Ex = []

    
    t1Deadline_Ex = [int(t1Array[1]), int(t1Array[2])]
    t2Deadline_Ex = [int(t2Array[1]), int(t2Array[2])]
    t3Deadline_Ex = [int(t3Array[1]), int(t3Array[2])]
    t4Deadline_Ex = [int(t4Array[1]), int(t4Array[2])]
    t5Deadline_Ex = [int(t5Array[1]), int(t5Array[2])]

    totalUtil = (t1Deadline_Ex[1]/t1Deadline_Ex[0]) +(t2Deadline_Ex[1]/t2Deadline_Ex[0]) +(t3Deadline_Ex[1]/t3Deadline_Ex[0]) +(t4Deadline_Ex[1]/t4Deadline_Ex[0]) + (t5Deadline_Ex[1]/t5Deadline_Ex[0])
    #totalUtil = 0.7
    mu = int(hArray[0])*(2**(1/int(hArray[0]))-1)

    if totalUtil > mu:
        return 1
    else:
        return 0
def RM(*args):

    print("Starting RM")
    hArray = []
    t1Array = []
    t2Array = []
    t3Array = []
    t4Array = []
    t5Array = []
    lcmArray = []
    
    hArray = args[0]
    t1Array = args[1]
    t2Array = args[2]
    t3Array = args[3]
    t4Array = args[4]
    t5Array = args[5]

    lcmArray = [t1Array[1],t2Array[1],t3Array[1],t4Array[1],t5Array[1]]


    t1Deadline_Ex = []
    t2Deadline_Ex = []
    t3Deadline_Ex = []
    t4Deadline_Ex = []
    t5Deadline_Ex = []
    
    t1Deadline_Ex = [t1Array[0], int(t1Array[1]), int(t1Array[2])]
    t2Deadline_Ex = [t2Array[0], int(t2Array[1]), int(t2Array[2])]
    t3Deadline_Ex = [t3Array[0], int(t3Array[1]), int(t3Array[2])]
    t4Deadline_Ex = [t4Array[0], int(t4Array[1]), int(t4Array[2])]
    t5Deadline_Ex = [t5Array[0], int(t5Array[1]), int(t5Array[2])]


##    totalPeriod = 1000
##    for i in range(1,totalPeriod+1):
##        print(i)
##
##        if(t1Deadline_Ex[1]<)
    
    

def EDF_Util(*args):
    
    hArray = []
    t1Array = []
    t2Array = []
    t3Array = []
    t4Array = []
    t5Array = []
    lcmArray = []
    
    hArray = args[0]
    t1Array = args[1]
    t2Array = args[2]
    t3Array = args[3]
    t4Array = args[4]
    t5Array = args[5]

    t1Deadline_Ex = []
    t2Deadline_Ex = []
    t3Deadline_Ex = []
    t4Deadline_Ex = []
    t5Deadline_Ex = []

    
    t1Deadline_Ex = [int(t1Array[1]), int(t1Array[2])]
    t2Deadline_Ex = [int(t2Array[1]), int(t2Array[2])]
    t3Deadline_Ex = [int(t3Array[1]), int(t3Array[2])]
    t4Deadline_Ex = [int(t4Array[1]), int(t4Array[2])]
    t5Deadline_Ex = [int(t5Array[1]), int(t5Array[2])]

    totalUtil = (t1Deadline_Ex[1]/t1Deadline_Ex[0]) +(t2Deadline_Ex[1]/t2Deadline_Ex[0]) +(t3Deadline_Ex[1]/t3Deadline_Ex[0]) +(t4Deadline_Ex[1]/t4Deadline_Ex[0]) + (t5Deadline_Ex[1]/t5Deadline_Ex[0])
    #totalUtil = 0.7
    mu = 1

    if totalUtil > mu:
        return 1
    else:
        return 0

#EDF method operates with Deadlines and Times(MAX FREQ 3rd column in input file)
def EDF(*args):
    print("Starting EDF")
    hArray = []
    t1Array = []
    t2Array = []
    t3Array = []
    t4Array = []
    t5Array = []
    lcmArray = []
    
    hArray = args[0]
    t1Array = args[1]
    t2Array = args[2]
    t3Array = args[3]
    t4Array = args[4]
    t5Array = args[5]

    lcmArray = [t1Array[1],t2Array[1],t3Array[1],t4Array[1],t5Array[1]]


    
    
    
    print("YES")
    
    lcmInts = string2Int(lcmArray)
    print("The LCM is: " + str(LCM(lcmInts)))

    #Assign priority accodring to dealines/periods
    #low number deadlines > high deadlines
    

    

    



if __name__ == '__main__':

    #using sys lib to create an argument list from command line
    ##
    ##This section is used to read arguments from command line
    ####Comment section out to run in IDLE
    ####Uncomment section to run from Command Line
    ##Sample Command: $ python ./program.py input1.txt EDF

    argList = sys.argv

    inputFile = argList[1]
    algoSelect = argList[2]
    #algoEE = argList[3]

    print("Reading " + inputFile+ "\n")
    print("The user has selected the " + algoSelect + " Scheduling Algorithm")
    ##END SECTION
    
    
    with open(inputFile , 'r') as file:               #input file is open in read mode
            with open('output1.txt', 'w') as fileOut:   #output file is created to be written

                    tasks=[]    #array to store each of the lines in input file

                    for lines in file:  #for loop read lines in file only containing numbers
                        #results = re.findall(r"[-+]?\d*\.\d+|\d+", lines)
                        tasks.append(lines)

                    headerArray = []
                    w1Array = []
                    w2Array = []
                    w3Array = []
                    w4Array = []
                    w5Array = []

                    headerArray = tasks[0].split()
                    w1Array = tasks[1].split()
                    w2Array = tasks[2].split()
                    w3Array = tasks[3].split()
                    w4Array = tasks[4].split()
                    w5Array = tasks[5].split()

                    #arrays to keep converter string arrays
                    hIntArray = []
                    

                    print("Header Array")
                    print(headerArray)

                   #method string2Int makes integer array
                    hIntArray = string2Int(headerArray)
                    print(hIntArray)
                    for h in range(7):
                        print(hIntArray[h])

                    print("Task 1 Array")
                    print(w1Array)
                    for w1 in range(6):
                        print(w1Array[w1])

                    print("Task 2 Array")
                    print(w2Array)
                    for w2 in range(6):
                        print(w2Array[w2])

                    print("Task 3 Array")
                    print(w3Array)
                    for w3 in range(6):
                        print(w3Array[w3])

                    print("Task 4 Array")
                    print(w4Array)
                    for w4 in range(6):
                        print(w4Array[w4])

                    print("Task 5 Array")
                    print(w5Array)
                    for w5 in range(6):
                        print(w5Array[w5])
                        
                    #Sorting the Deadlines by Ascending Order for priority
                    #Done regardless of EDF or RM
                    t1Deadline_Ex = []
                    t2Deadline_Ex = []
                    t3Deadline_Ex = []
                    t4Deadline_Ex = []
                    t5Deadline_Ex = []
                    
                    t1Deadline_Ex = [w1Array[0], int(w1Array[1]), int(w1Array[2])]
                    t2Deadline_Ex = [w2Array[0], int(w2Array[1]), int(w2Array[2])]
                    t3Deadline_Ex = [w3Array[0], int(w3Array[1]), int(w3Array[2])]
                    t4Deadline_Ex = [w4Array[0], int(w4Array[1]), int(w4Array[2])]
                    t5Deadline_Ex = [w5Array[0], int(w5Array[1]), int(w5Array[2])]
                                  
                    print(t1Deadline_Ex)
                    print(t2Deadline_Ex)
                    print(t3Deadline_Ex)

                        
                    for i in range(hIntArray[0]):
                    
                        for j in range(0, hIntArray[0] - i - 1):
                            t = []
                            if t2Deadline_Ex[1] < t1Deadline_Ex[1]:
                                t = t1Deadline_Ex     
                                t1Deadline_Ex = t2Deadline_Ex
                                t2Deadline_Ex = t

                            elif t3Deadline_Ex[1] < t2Deadline_Ex[1]:
                                t = t2Deadline_Ex
                                t2Deadline_Ex = t3Deadline_Ex
                                t3Deadline_Ex = t

                            elif t4Deadline_Ex[1] < t3Deadline_Ex[1]:
                                t = t3Deadline_Ex
                                t3Deadline_Ex = t4Deadline_Ex
                                t4Deadline_Ex = t

                            elif t5Deadline_Ex[1] < t4Deadline_Ex[1]:
                                t = t4Deadline_Ex
                                t4Deadline_Ex = t5Deadline_Ex
                                t5Deadline_Ex = t
                            
                            
                    ##Sorting END

                    
                    if algoSelect == 'EDF':
                        #if algoEE == None:
                        ##Ideas
                        ##Pass arrays over and loop them in algo function
                        ##Write to output in algo function
                        check = EDF_Util(headerArray,w1Array,w2Array,w3Array,w4Array,w5Array)

                        if not check:
                            print("EDF selected")
                            EDF(headerArray,t1Deadline_Ex, t2Deadline_Ex, t3Deadline_Ex, t4Deadline_Ex, t5Deadline_Ex)
                            
                            
                        else:
                            print("No Feasible Schedule")
                        
##                        elif algoEE == 'EE':
##                            print("EDF EE selected")
                    
                    if algoSelect == 'RM':
                        #Call RM algo
                        check = RM_Util(headerArray,w1Array,w2Array,w3Array,w4Array,w5Array)
                        if not check:
                            print("RM selected")
                            RM(headerArray,t1Deadline_Ex, t2Deadline_Ex, t3Deadline_Ex, t4Deadline_Ex, t5Deadline_Ex)
                            
                        else:
                            print("No Feasible Schedule")
##
##                    if algoSelect == 'EDF' and algoEE == 'EE':
##                        print("EDF EE selected")
##
##                    if algoSelect == 'RM' and algoEE == 'EE':
##                        print("RM EE selected")


                    
