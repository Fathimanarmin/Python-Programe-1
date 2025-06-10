
def checknumber(num):
    print(f"The number {num} is {'positive' if num > 0 else 'negative' if num < 0 else 'invalid input'}.")
n=int(input('enter the number :'))                 
checknumber(n)



#even or odd

def check_even_odd(num):
    print(f"The number {num} is {'even' if num % 2 == 0 else 'odd'}.")
n=int(input('enter the number :'))  
check_even_odd(n)


# largest number

def find_largest_number(numbers):
    return max(numbers)
print(find_largest_number([10, 20,30,40]))

# second smallest unique value

def second_smallest_unique(number):
    unique_value=sorted(set(number))
    if len(unique_value)<2:
        return None
    return(unique_value[1])
print(second_smallest_unique([10,20,30,40]))