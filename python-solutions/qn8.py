def round_to_nearest_integer(num):
    return int(num + 0.5) if num >= 0 else int(num - 0.5)

num = 5.67
rounded_num = round_to_nearest_integer(num)
print(rounded_num)  

num = 4.34
rounded_num = round_to_nearest_integer(num)
print(rounded_num)  