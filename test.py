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

    hArray = args[0]
    t1Deadline_Ex = args[1]
    t2Deadline_Ex = args[2]
    t3Deadline_Ex = args[3]

    totalUtil = (int(t1Deadline_Ex[2])/int(t1Deadline_Ex[1])) + (int(t2Deadline_Ex[2])/int(t2Deadline_Ex[1])) + (int(t3Deadline_Ex[2])/int(t3Deadline_Ex[1]))
    print(totalUtil)
    mu = int(hArray[0])*(2**(1/int(hArray[0]))-1)
    print(mu)

    if totalUtil > mu:
        return 1
    else:
        return 0

def RM(*args):
    fileOutput = 'output.txt'
    with open(fileOutput, 'w') as fileOut:   #output file is created to be written
        print("Starting RM")
        Frequency = "1188"
        hArray = args[0]
        t1Deadline_Ex = args[1]
        t2Deadline_Ex = args[2]
        t3Deadline_Ex = args[3]

        #lcmArray = [t1Deadline_Ex[1], t2Deadline_Ex[1], t3Deadline_Ex[1]]
        #lcmInts = string2Int(lcmArray)
        #print("The LCM is: " + str(LCM(lcmInts)))

        t1Runtime = 0
        newt1Deadline_Ex = t1Deadline_Ex[1]

        t2Runtime = 0
        newt2Deadline_Ex = t2Deadline_Ex[1]

        t3Runtime = 0
        newt3Deadline_Ex = t3Deadline_Ex[1]

    ##35 times within 300 time units

        totalPeriod = 36
        done = 0
        print("newt1Deadline_Ex:", newt1Deadline_Ex)
        
        for i in range(1,totalPeriod+1):

            print("")
            print("Total Execution Time:", i)
            
            if(t1Runtime < t1Deadline_Ex[2] and i < newt1Deadline_Ex): #if runtime < execution time and i < deadline
                t1Runtime = t1Runtime + 1
                print(t1Deadline_Ex[0]," RunTime:", t1Runtime)                    
               
            elif(t2Runtime < t2Deadline_Ex[2] and i < newt2Deadline_Ex): #if runtime < execution time and i < deadline
                t2Runtime = t2Runtime + 1
                print(t2Deadline_Ex[0]," RunTime:", t2Runtime)
                    
            elif(t3Runtime < t3Deadline_Ex[2] and i < newt3Deadline_Ex): #if runtime < execution time and i < deadline
                t3Runtime = t3Runtime + 1
                print(t3Deadline_Ex[0], " RunTime:", t3Runtime)

            else:
                print("Idle")
                

            if(i == newt1Deadline_Ex): #if i == deadline, calculate new deadline and reset runtime
                newt1Deadline_Ex = newt1Deadline_Ex + t1Deadline_Ex[1]
                print("new", t1Deadline_Ex[0],"Deadline:", newt1Deadline_Ex)
                t1Runtime = 0

            if(i == newt2Deadline_Ex): #if i == deadline, calculate new deadline and reset runtime
                newt2Deadline_Ex = newt2Deadline_Ex + t2Deadline_Ex[1]
                print("new", t2Deadline_Ex[0],"Deadline:", newt2Deadline_Ex)
                t2Runtime = 0

            if(i == newt3Deadline_Ex): #if i == deadline, calculate new deadline and reset runtime
                newt3Deadline_Ex = newt3Deadline_Ex + t3Deadline_Ex[1]
                print("new",t3Deadline_Ex[0],"Deadline:", newt3Deadline_Ex)
                t3Runtime = 0

def EDF_Util(*args):
    
    hArray = args[0]
    t1Deadline_Ex = args[1]
    t2Deadline_Ex = args[2]
    t3Deadline_Ex = args[3]

    totalUtil = (int(t1Deadline_Ex[2])/int(t1Deadline_Ex[1])) + (int(t2Deadline_Ex[2])/int(t2Deadline_Ex[1])) + (int(t3Deadline_Ex[2])/int(t3Deadline_Ex[1]))
    print(totalUtil)
    mu = 1
    print(mu)

    if totalUtil > mu:
        return 1
    else:
        return 0

#EDF method operates with Deadlines and Times(MAX FREQ 3rd column in input file)
def EDF(*args):
    fileOutput = 'output.txt'
    with open(fileOutput, 'w') as fileOut:   #output file is created to be written
        print("Starting EDF")
        Frequency = "1188"
        hArray = args[0]
        t1Deadline_Ex = args[1]
        t2Deadline_Ex = args[2]
        t3Deadline_Ex = args[3]

        t1Runtime = 0
        newt1Deadline_Ex = t1Deadline_Ex[1]

        t2Runtime = 0
        newt2Deadline_Ex = t2Deadline_Ex[1]

        t3Runtime = 0
        newt3Deadline_Ex = t3Deadline_Ex[1]

    ##35 times within 300 time units

        totalPeriod = 36
        done = 0
        print("newt1Deadline_Ex:", newt1Deadline_Ex)
        
        for i in range(1,totalPeriod+1):
            
            print("")
            print("Total Execution Time:", i)

            #find out the remaining time units until deadline
            t1EDF_rem = newt1Deadline_Ex - i
            t2EDF_rem = newt2Deadline_Ex - i
            t3EDF_rem = newt3Deadline_Ex - i

            #when the runtime equals execution time, add the deadline to the remaining time 
            if(t1Runtime == t1Deadline_Ex[2]):
                t1EDF_rem = t1EDF_rem + t1Deadline_Ex[1]
            if(t2Runtime == t2Deadline_Ex[2]):
                t2EDF_rem = t2EDF_rem + t2Deadline_Ex[1]
            if(t3Runtime == t3Deadline_Ex[2]):
                t3EDF_rem = t3EDF_rem + t3Deadline_Ex[1]

            print("t1 remainder:", t1EDF_rem)
            print("t2 remainder:", t2EDF_rem)
            print("t3 remainder:", t3EDF_rem)

            #determine whether a task has an earlier deadline than another task
            t1EDF_rem_compare = t1EDF_rem <= t2EDF_rem or t1EDF_rem <= t3EDF_rem
            t2EDF_rem_compare = t2EDF_rem <= t1EDF_rem or t2EDF_rem <= t3EDF_rem
            t3EDF_rem_compare = t3EDF_rem <= t1EDF_rem or t3EDF_rem <= t2EDF_rem

            
            if(t1EDF_rem_compare and t1Runtime != t1Deadline_Ex[2]):
                if(t1Runtime < t1Deadline_Ex[2] and i < newt1Deadline_Ex): #if runtime < execution time and i < deadline
                    t1Runtime = t1Runtime + 1
                    print(t1Deadline_Ex[0]," RunTime:", t1Runtime)
            elif(t2EDF_rem_compare and t2Runtime != t2Deadline_Ex[2]):
                if(t2Runtime < t2Deadline_Ex[2] and i < newt2Deadline_Ex): #if runtime < execution time and i < deadline
                    t2Runtime = t2Runtime + 1
                    print(t2Deadline_Ex[0]," RunTime:", t2Runtime)
            elif(t3EDF_rem_compare and t3Runtime != t3Deadline_Ex[2]):
                if(t3Runtime < t3Deadline_Ex[2] and i < newt3Deadline_Ex): #if runtime < execution time and i < deadline
                    t3Runtime = t3Runtime + 1
                    print(t3Deadline_Ex[0], " RunTime:", t3Runtime)
            else:
                print("Idle")
            
            
            #update deadline
            if(i == newt1Deadline_Ex): #if i == deadline, calculate new deadline and reset runtime
                newt1Deadline_Ex = newt1Deadline_Ex + t1Deadline_Ex[1]
                print("new", t1Deadline_Ex[0],"Deadline:", newt1Deadline_Ex)
                t1Runtime = 0

            if(i == newt2Deadline_Ex): #if i == deadline, calculate new deadline and reset runtime
                newt2Deadline_Ex = newt2Deadline_Ex + t2Deadline_Ex[1]
                print("new", t2Deadline_Ex[0],"Deadline:", newt2Deadline_Ex)
                t2Runtime = 0

            if(i == newt3Deadline_Ex): #if i == deadline, calculate new deadline and reset runtime
                newt3Deadline_Ex = newt3Deadline_Ex + t3Deadline_Ex[1]
                print("new",t3Deadline_Ex[0],"Deadline:", newt3Deadline_Ex)
                t3Runtime = 0




if __name__ == '__main__':

    #using sys lib to create an argument list from command line
    ##
    ##This section is used to read arguments from command line
    ####Comment section out to run in IDLE
    ####Uncomment section to run from Command Line
    ##Sample Command: $ python ./program.py input1.txt EDF

    argList = sys.argv
    
    if argList[1:]:
        inputFile = argList[1]
        print('argument1:', inputFile)
        
        if argList[2:]:
            algoSelect = argList[2]
            print('argument2:', algoSelect)

            if argList[3:]:
                algoEE = argList[3]
                print('argument3:', algoEE)

    print('')

    print("Reading " + inputFile+ "\n")
    print("The user has selected the " + algoSelect + " Scheduling Algorithm")
    ##END SECTION
    
    
    with open(inputFile , 'r') as file:               #input file is open in read mode
            

        tasks=[]    #array to store each of the lines in input file

        for lines in file:  #for loop read lines in file only containing numbers
            #results = re.findall(r"[-+]?\d*\.\d+|\d+", lines)
            tasks.append(lines)

        headerArray = tasks[0].split()
        w1Array = tasks[1].split()
        w2Array = tasks[2].split()
        w3Array = tasks[3].split()

        print('')

        #arrays to keep converter string arrays
        hIntArray = []
        print("Header Array")
        print(headerArray)

        #method string2Int makes integer array
        hIntArray = string2Int(headerArray)
        print(hIntArray)

        print('')

        print("Task 1 Array")
        print(w1Array)

        print("Task 2 Array")
        print(w2Array)

        print("Task 3 Array")
        print(w3Array)


        print('')
            
        #Sorting the Deadlines by Ascending Order for priority
        #Done regardless of EDF or RM                    
        t1Deadline_Ex = [w1Array[0], int(w1Array[1]), int(w1Array[2])]
        t2Deadline_Ex = [w2Array[0], int(w2Array[1]), int(w2Array[2])]
        t3Deadline_Ex = [w3Array[0], int(w3Array[1]), int(w3Array[2])]

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


        print("Sorted Arrays")
        print(t1Deadline_Ex)
        print(t2Deadline_Ex)
        print(t3Deadline_Ex)

        print('')
                                
        ##Sorting END   

        #scheduling algorithms                    
        if algoSelect == 'EDF':
            if argList[3:] and algoEE == 'EE':
                print('HEE HEE')

            ##Ideas
            ##Pass arrays over and loop them in algo function
            ##Write to output in algo function
            print("EDF selected")
            check_Util = EDF_Util(headerArray,t1Deadline_Ex, t2Deadline_Ex, t3Deadline_Ex)
            if not check_Util:
                EDF(headerArray,t1Deadline_Ex, t2Deadline_Ex, t3Deadline_Ex)
            else:
                print("Utilization inequality does not hold")
                print("No Feasible Schedule")

        if algoSelect == 'RM':
            if argList[3:] and algoEE == 'EE':
                print('HEE HEE')

            #Call RM algo
            print("RM selected")
            RM(headerArray,t1Deadline_Ex, t2Deadline_Ex, t3Deadline_Ex)
            
            '''
            check_Util = RM_Util(headerArray,t1Deadline_Ex, t2Deadline_Ex, t3Deadline_Ex)
            if not check_Util:
                RM(headerArray,t1Deadline_Ex, t2Deadline_Ex, t3Deadline_Ex)
            else:
                print("Utilization inequality does not hold")
                print("No Feasible Schedule")
            '''





