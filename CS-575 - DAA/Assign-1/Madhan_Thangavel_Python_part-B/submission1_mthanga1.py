import itertools
from threading import Thread

### Reading the input file
with open('InputFile.txt') as file:
    data = file.readlines()[0].strip('\n')
    array_test = filter(None, data.split(" "))
    array = list(map(int, array_test)) 

### Writing the output file
file = open("OutputFile.txt", "w")

## Function which computes and stores the result in OutputFile.txt
def resultMapper(list,t,item):
    array_index = [i for i, x in enumerate(list) if x == item]
    if len(array_index) > 0:
        for index in array_index:
                file.write("Difference between "+str(t[0])+" and "+str(t[1]) +" is :"+str(item)+", ")
                file.write("Result:"+str(item)+" exists in the InputFile.txt\n\n")

temp = []
for x in itertools.permutations(array,2):
    temp.append(sorted(x))

##To removes all the duplicates in the array
k = sorted(temp)
sorted_array = [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i-1]] 

##To ittrate the values in InputFile.txt
for value in sorted_array:
    value.sort(reverse=True) 
    sub_value = value[0] - value[1]
    t = Thread(target=resultMapper, args=(array,value,sub_value,))
    t.start()

print("output is saved in OutputFile.txt")
file.close()