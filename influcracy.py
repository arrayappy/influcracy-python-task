#importing csv data and converting it into list data
import csv

with open('zgod.csv', newline='') as f:
    reader = csv.reader(f)
    zgod = list(reader)

zgodlist=[]
for i in range(len(zgod)):
	zgodlist.append(zgod[i][0])

with open('hastar.csv', newline='') as f:
    reader = csv.reader(f)
    hastar = list(reader)

hastarlist=[]
for i in range(len(hastar)):
	hastarlist.append(hastar[i][0])

# approach 1 [my optimal approach]
# In this approach, I've sorted two lists and using alphabetical checking
# i'm moving forward each pointers of each lists and got the common items
result=[]
zgodlist.sort()
hastarlist.sort()
i=0
j=0
while(i<len(zgodlist) and j<len(hastarlist)):
    if(zgodlist[i]<hastarlist[j]):
        i+=1
    elif(zgodlist[i]>hastarlist[j]):
        j+=1
    else:
        result.append(zgodlist[i])
        i+=1
        j+=1
print(result)

# approach 2 
# In this approach, I converted lists into sets and using & we can get common elements
print(set(zgodlist)&set(hastarlist))

# approach 3
# In this approach, we can simply get common elements by using intersection of sets
print(set(zgodlist).intersection(hastarlist))
