Name : Madhan Thangavel
ID : B00814916
CS - 575-20 Assignment 1

Programming language used : Python

****************************************************************************************************************************************************
Note:

The program is a given as a python file which can be executed in any python environment (Spyder, Jupyter, PyCharm, etc).
The input file contains the test case which is imported by the program by itself.
The output file is written after the program is run.

****************************************************************************************************************************************************
Implemented Algorithm:

* This program takes an array from a text file, implemented using file handling in python.
* The program then reads the array, adds two 'Keys' or elements of the array and campares the sum with every other Key (or item) in the array.
* If the function finds the sum of any two keys equal to any item in the array, it returns the value.
* The output is stored in the an output file showing the two keys.

TIME COMPLEXITY:

-> I used simple for-loop to itrrate the values and its worst case time complexity will be is O(n pow 2 ).As the time taken for the nth value 
   and n-1th value to compute the difference will be the worst possible case. 


****************************************************************************************************************************************************
CODE:

import itertools
from threading import Thread

### Reading the input file
with open('Input.txt') as file:
    data = file.readlines()[0].strip('\n')
    array_test = filter(None, data.split(" "))
    array = list(map(int, array_test)) 

### Writing the output file
file = open("Output.txt", "w")

def resultMapper(list,t,item):
    array_index = [i for i, x in enumerate(list) if x == item]
    if len(array_index) > 0:
        for index in array_index:
                file.write("Difference between "+str(t[0])+" and "+str(t[1]) +" is :"+str(item)+", ")
                file.write("Result:"+str(item)+" exists in the Input.txt\n\n")

temp = []
for x in itertools.permutations(array,2):
    temp.append(sorted(x))

##To removes all the duplicates in the array
k = sorted(temp)
sorted_array = [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i-1]] 

##To ittrate the values in input.txt
for value in sorted_array:
    value.sort(reverse=True) 
    sub_value = value[0] - value[1]
    t = Thread(target=resultMapper, args=(array,value,sub_value,))
    t.start()

print("output is saved in Output.txt")
file.close()

***************************************************************************************************************************************************
CODE RUN:

output is saved in Output.txt

// how it shows in the text file

Example :

Input.txt ---- 11 13 2 15 19

Output.txt ---- Difference between 13 and 2 is 11, Result:11 exists in Input.txt

//
*************************************************************************************************************************************************** 