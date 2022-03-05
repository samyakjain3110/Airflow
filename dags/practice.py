dict = {"a":1,"b":2,"c":3}
temp_dict = {}
for key in dict:
    print(key)
    print(dict[key])
    temp_dict[dict[key]] = key
print(temp_dict)