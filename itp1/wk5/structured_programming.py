"""
Takes an interget 'n' input from the command line
Prints all the numbers from 1 to n that are 
either divisible by 3 or contain the digit 3
"""
n = int(input())
for i in range(1, n+1):
    x = i
    prin = False

    # divisible by 3
    if x % 3 == 0:
        prin = True
    else:
        # loop while x is greater than 0
        while x > 0:
            # last digit is 3
            if x % 10 == 3:
                prin = True
                break
            # remove the last digit
            x //= 10
    
    if prin:
        print(" " + str(i), end="")
print()
