def perfect_num(n):
    return sum(int(digit) for digit in str(n)) == 10

def the_k_perfect_num(k):
    count = 0
    n = 19
    
    while True:
        if perfect_num(n):
            count += 1
            if count == k:
                return n
        n += 9  

k = int(input("nhap so thu tu k: "))
result = the_k_perfect_num(k)
print(f"so hoan hao thu {k} la {result} ")
