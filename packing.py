def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum


# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))


# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
    print(a, b, c)

#ANOTHER PROGRAM WHICH REFER BOTH PACKING AND UNPACKING
# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
    # Convert args tuple to a list so we can modify it
    args = list(args)

    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'

    # UNPACKING args and calling fun1()
    fun1(*args)


# Driver code
fun2('Hello', 'beautiful', 'world!')