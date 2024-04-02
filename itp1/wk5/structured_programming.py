def call(n):
    """
    Print all the numbers from 1 to n that are 
    either divisible by 3 or contain the digit 3
    """
    for i in range(1, n+1):
        x = i
        prin = False

        # divisible by 3
        if x % 3 == 0:
            prin = True
        else:
            # loop until x is greater than 0
            while x > 0:
                # last digit is 3
                if x % 10 == 3:
                    prin = True
                    break
                # remove the last digit
                x /= 10
        
        if prin:
            print("", i, end="")
    print()

# usage
for i in range(20, 60, 10):
    call(i)