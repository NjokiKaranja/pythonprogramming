# (a) Print the total items in the list
my_new_array = []

number = input(('Enter your integers: '))
integer_list = number.split(',')

# traverse the integer list
for x in integer_list:
    my_new_array.append(int(x))

# print("The populated array is now: ", my_new_array)
print("The total items in the list is: ", len(my_new_array))

# (b) Print the last item in the list
print("The last item in the array is: ", my_new_array[len(my_new_array)-1])

# (c) Print the list in reverse order
# reversed_arr = my_new_array[::-1]
# print("The new reversed array is: ", reversed_arr)

# (d): Print Yes if the list contains a 5 and No otherwise
# 1. Traverse the list to see if there is a 5
count = 0

for y in my_new_array:
    print(y)

    # 2. Check if a 5 exists and print Yes if so else print No
    if y == 5:
        print("Yes")

    # (e): Print the number of fives in the list
        count += 1
    
    else:
        print("No")
        # break

print("Number 5 appears: " + str(count) + " time(s)")

# 1. Remove the first and the last items from the list, and 
# sliced_arr =my_new_array[1:-1]
# # print(sliced_arr)

# # 2. sort the remaining items
# sliced_arr.sort()

# # 3. print the result
# print(sliced_arr)






# nums=[]
# list_length = 4
# for i in range(list_length)
# nums.append(number)


# for num in nums:
#     print

    




# count=0
# for num in nums:
#     if num % 2 = 0:
#         count = count + 1

# print(count)

from random import randint
nums=[]
for x in range(20):
    number=randint(1,100)
    nums.append(number)

for x in nums:
    print(x)
