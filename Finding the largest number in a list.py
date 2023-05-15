largestSoFar = 2
print("Smallest number is", largestSoFar)
for the_num in [2,6,3,9,41,67,8] :
    if the_num > largestSoFar:
         largestSoFar=the_num
    print(largestSoFar, the_num)   
print("Largest number is", largestSoFar)