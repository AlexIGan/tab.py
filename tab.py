my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
print(my_list)

while index < len(my_list):
    i = my_list[index]
    index = index + 1
    if i ==0:
        continue
    elif i <0:
        break
    elif index == len(my_list):
        print(i)
    else:
        print(i)
