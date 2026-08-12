# A number is divisible by 3, 5, both, or neither
x=15
if(x%3==0 and x%5==0):
    print("x is div by 3 and 5")
elif(x%3==0):
    print("x is div by 3")
elif(x%5==0):
    print("x is div by 5")
else:
    print("Neither div by 3 & 5")



#Div by 5- print fizz, or else print buzz
x=7
if(x%5==0):
    print("fizz")
else:
    print("buzz")

#Number is positive
x=5
if(x>0):
    print("Positive Number")
else:
    print("Not a positive number")

#Eligible to vote or not
v=15
if(v>18):
    print("Eligible to vote")

#Number greater than 100
g=500
if(g>100):
    print("g is greater than 100")

#Divisible by 5
d= 6
if(d%5==0):
    print("Divisible by 5")


#Student has passed
sp= 45
if(sp>40):
    print("Student has passed")


#Number is even or odd
x= 0
if(x==0):
    print("Neither Even nor odd")
elif(x%2==0):
    print("Even")
else:
    print("odd")


#Larger of two numbers
s=10
l=100
if(s==l):
    print("Both are larger")
elif(s>l):
    print("s is larger")
else:
    print("l is larger")

#Adult or minor
a=29
if(a>=18):
    print("Adult")
else:
    print("Minor")


#Positive or negative
n=0
if(n==0):
    print("Neither positive nor negative")
elif(n>0):
    print("Positive")
else:
    print("Negative")

#Password check
password = "python123"
enteredPassword = "s"
if (password==enteredPassword):
    print("Password matched")
else:
    print("Password not matched")

#Assign grades based on marks
mark= 114
if(mark>=90 and mark<=100):
    print("Grade A")
elif(mark>=75 and mark<=89):
    print("Grade B")
elif(mark>=50 and mark<=74):
    print("Grade C")
elif(mark<50):
    print("Fail")

input = "Monday"
if(input=="Monday" or input=="Tuesday" or input=="wednesday" or input=="thursday" or input=="friday"):
    print("weekday")
else:
    print("weekend")


#Check temp
climate= 20
if(climate>35):
    print("Hot")
elif(climate>=20 and climate<=35):
    print("Pleasant")
elif(climate<20):
    print("Cold")


#Determine tickect price
age= 30
if(age>60):
    print("Ticket Price =Rs 70")
elif(age>=12 and age<=60):
    print("Ticket Price =Rs 100")
elif(age<12):
    print("Ticket Price =Rs 50")

#Check username and password
username = "sal"
password ="s"
enteruserName = "ss"
enteredPassword = "va"
if(enteruserName==username and enteredPassword==password):
    print("Login successfully")
else:
    print("Login failed")


#find largest of three
a = 10
b=39
c=7
if(a==b and b==c and a==c):
    print("All are equal")
elif(a>b and a>c):
    print("a is largest")
elif(b>a and b>c):
    print("b is largest")
elif(c>a and c>b):
    print("c is largest")


#Check character is vowel or consonant
character = "f"
if(character=="a" or character=="e" or character=="i" or character=="o" or character=="u"):
    print("Vowel")
else:
    print("consonant")



#BMI classification
weight= 80000
height= 80
BMI = weight/height**2
print(BMI)
if(BMI<18.5):
    print("Underweight")
elif(BMI<25):
    print("Normal")
elif(BMI<30):
    print("Overweight")
else:
    print("Obese")





