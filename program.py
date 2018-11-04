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


#EDF method operates with Deadlines and Times(MAX FREQ 3rd column in input file)
def EDF():
    print("Testing like ASAP")


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

                    print("Header Array")
                    print(headerArray)
                    for h in range(7):
                        print(headerArray[h])

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

                    if algoSelect == 'EDF':
                        ##Ideas
                        ##Pass arrays over and loop them in algo function
                        ##Write to output in algo function
                        EDF()
                    
                    


                    h_first, h_second, h_third, h_fourth, h_fifth, h_sixth, h_seven = tasks[0].split()

                    w1_first, w1_second, w1_third, w1_fourth, w1_fifth, w1_sixth = tasks[1].split()

                    w2_first, w2_second, w2_third, w2_fourth, w2_fifth, w2_sixth = tasks[2].split()

                    w3_first, w3_second, w3_third, w3_fourth, w3_fifth, w3_sixth = tasks[3].split()

                    w4_first, w4_second, w4_third, w4_fourth, w4_fifth, w4_sixth = tasks[4].split()

                    w5_first, w5_second, w5_third, w5_fourth, w5_fifth, w5_sixth = tasks[5].split()
                    
                    fileOut.write(h_first)
                    fileOut.write(' ')
                    fileOut.write(h_second)
                    fileOut.write(' ')
                    fileOut.write(h_third)
                    fileOut.write(' ')
                    fileOut.write(h_fourth)
                    fileOut.write(' ')
                    fileOut.write(h_fifth)
                    fileOut.write(' ')
                    fileOut.write(h_sixth)
                    fileOut.write(' ')
                    fileOut.write(h_seven)

                    lcmArray = []
                    lcmArray.append(w1_second)
                    lcmArray.append(w2_second)
                    lcmArray.append(w3_second)
                    lcmArray.append(w4_second)
                    lcmArray.append(w5_second)

                    print(lcmArray)

                    #grabbing the first three columns of w1,w2,w3,w4, and w5 and placinf them into a string
                    #these will be handy to send to EDF and RM methods
                    #tasks run at max freq
                    w1ThreeCol = []
                    w2ThreeCol = []
                    w3ThreeCol = []
                    w4ThreeCol = []
                    w5ThreeCol = []

                    w1ThreeCol.append(w1_first)
                    w1ThreeCol.append(w1_second)
                    w1ThreeCol.append(w1_third)

                    w2ThreeCol.append(w2_first)
                    w2ThreeCol.append(w2_second)
                    w2ThreeCol.append(w2_third)

                    w3ThreeCol.append(w3_first)
                    w3ThreeCol.append(w3_second)
                    w3ThreeCol.append(w3_third)

                    w4ThreeCol.append(w4_first)
                    w4ThreeCol.append(w4_second)
                    w4ThreeCol.append(w4_third)

                    w5ThreeCol.append(w5_first)
                    w5ThreeCol.append(w5_second)
                    w5ThreeCol.append(w5_third)
