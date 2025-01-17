# Write a Python program to count the number of positive numbers in a list.

num = [1,-2,3,-4,5,-6,7,-8,9,-10]

positive_num_count = 0
for i in num:
    print(i)
    if i > 0:
        positive_num_count += 1
        
print("Positive number found:{}{}".format(positive_num_count, 23))
print("https:/{}/python/ref_string_format.asp".format(23))
# print(f"Positive number found: {positive_num_count}")
# console.log(`Positive number found: ${positive_num_count}`)