#code to find the largest number
largestSoFar = 2
print("Smallest number is", largestSoFar)
for the_num in [2,6,3,9,41,67,8] :
    if the_num > largestSoFar:
         largestSoFar=the_num
    print(largestSoFar, the_num)   
print("Largest number is", largestSoFar)

#A program to  reverse a given number
number= int(input("enter a number to be reversed: "))
reversed = 0
while(number>0):
    digit= number % 10
    reverse = (reversed * 10) + digit
    number = number // 10
print("The reversed number is:", reverse)
number= int(input("enter a number to be reversed: "))
reversed = 0
while(number>0):
    digit= number % 10
    reverse = (reversed * 10) + digit
    number = number // 10
print("The reversed number is:", reverse)
