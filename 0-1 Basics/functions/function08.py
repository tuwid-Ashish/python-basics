# def generator(limit):
#     even_count = 0
#     for i in range(2,limit+1):
#         if i%2 == 0:
#             even_count += 1
    
#     return even_count

# print(generator(10)) # 4

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for n in even_generator(12):
    print(n)        