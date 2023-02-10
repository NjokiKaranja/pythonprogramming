#my first python list
numbers=[45,56,67,78,89,54,]
# names=["Njoki","Lucy","Rachel"]
# # for x in range(len(numbers)):
# #     print(numbers[x])


# #LIST MEMBERS
# #INDEX-gets the index of an element to the end of a list
# #print(numbers.index(78))
# #print(names.index("Lucy"))

# #APPPEND-adds an element to the end of a list

# #before appending
# for x in range(len(numbers)):
#     print(numbers[x])


# numbers.append(90)

# #after appending
# for x in range(len(numbers)):
#     print(numbers[x])


#count-returns the number of times an element occurs in a List
#print(numbers.count(67))


#POP-removes an element at a given index and returns that element
#print(numbers.pop(2))


#INSERTS-inserts element x at an index y
# numbers.insert(2,100)

# for x in range(len(numbers)):
#     print(numbers[x])

#REMOVE-removes the first occurencs of an element 

# numbers.remove(67)


# #SORT-arranges the list in ascending order
# for x in range(len(numbers)):
#     print(numbers[x])

# #sort the list
# numbers.sort()

#add a anew line for formatted output
# print("\n")


# for x in range(len(numbers)):
#      print(numbers[x])


#TIPS AND TRICKS 


#creating list
# nums=[] #empty list
# for x in range(10):
#     nums.append(x)

# for x in range(len(numbers)):
#     print(nums[x])


even_nums=[]
for num in range(20):
    if (num % 2==0):
        even_nums.append(num)
 #print the list
for x in range(len(even_nums)):
    print(even_nums[x])
