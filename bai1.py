def sum_string(s):
    total = 0
    num = ""
    
    for char in s:
        if char.isdigit() or (char == '-' and num == ""):
            num += char
        elif num:
            total += int(num)
            num = ""
    
    if num:
        total += int(num)
    
    return total


mystring = input("nhap chuoi: ")

total = sum_string(mystring)

print("tong cua cac so trong chuoi ky tu la :" , total)
