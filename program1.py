
def checknumber(num):
    print(f"The number {num} is {'positive' if num > 0 else 'negative' if num < 0 else 'invalid input'}.")
n=int(input('enter the number :'))                 
checknumber(n)



#even or odd

def check_even_odd(num):
    print(f"The number {num} is {'even' if num % 2 == 0 else 'odd'}.")
n=int(input('enter the number :'))  
check_even_odd(n)
