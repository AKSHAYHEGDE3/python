def reverse_number(z):
    rev = 0
    while z > 0:
        rev = rev*10
        rev = rev + z % 10
        z = z // 10
    return rev
def nxt_num(x):
    x = x + 1
    while (x != reverse_number(x)):
        x = x +  1
    return x
while True:
    n=int(input("enter the no:"))
    print(f"the nxt palindrome no of {n} is {nxt_num(n)}")
    s=input("press y to continue:")
    if s != "y":
        break



    




