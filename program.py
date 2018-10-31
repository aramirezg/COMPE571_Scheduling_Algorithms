import re
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


with open('input1.txt', 'r') as file:               #input file is open in read mode
        with open('output1.txt', 'w') as fileOut:   #output file is created to be written

                tasks=[]    #array to store each of the lines in input file

                for lines in file:  #for loop read lines in file only containing numbers
                    results = re.findall(r"[-+]?\d*\.\d+|\d+", lines)
                    tasks.append(results)

                for i in range(5): #prints each line from file as a list of elements 
                    print(tasks[i])

                for s in tasks: #loop prints out second element in each list from tasks[] array

                    oneK = s[1]
                    print(oneK)

                    


                               

                
##                fileLines = file.readlines()
##                for lines in fileLines:
##                    results = re.findall(r"[-+]?\d*\.\d+|\d+", lines)            
##                    #print(lines, end="*")
##                    
##                    print(results, end="*")
##                    fileOut.write(lines)
                    

                



##with open('input1.txt', 'r') as file:
##
##    for i in range(12):
##        file_content = file.readlines()
##        print(file_content)
