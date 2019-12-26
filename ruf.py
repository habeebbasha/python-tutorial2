#ELIMINATING VOWELS IN  STRING
string="habeeb"
vowels="aAeEiIoOuU"
str=[i for i in string if i not in vowels]
str=''.join(str)
print(str)
#fabonacci series
def fab(num):
    f1=0
    f2=1
    if num==1:
        print(f1)
    else:
        print(f1)
        print(f2)
        for i in range(2,num):
            fabo=f1+f2
            f1=f2
            f2=fabo
            print(fabo)
fab(5)
#PRIME NUMBERS
def prime(num):
    if num>1:
        for i in range(2,num//2):
            if num%i==0:
                print(num, "is not a prime")
                break
        else:
            print(num,"is prime number")
    else:
        print(num,"is not a prime")
prime(7)












