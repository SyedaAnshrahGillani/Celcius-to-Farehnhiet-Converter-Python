# Celcius / Farehnhiet coverter

a=input("Enter 1 to convert C TO F and 2 to convert F to C: ")

def C_F(celcius):
    #c*9/5+32=f
    f=cd*(9/5)+32
    print("The value in Farehnhiet is: ",f)
def F_C(farhenhiet):
    #32*f-32*5/9=c
    c=fd*32-32*(5/9)
    
    print("The value in Celcius is: ",c)
if(a=="1"):
   cd=int(input("Enter value in celcius: "))
   C_F(cd)

elif(a=="2"):
    fd=int(input("Enter value in Farehnhiet: "))
    F_C(fd)
else:
    print("Invalid Input!")
