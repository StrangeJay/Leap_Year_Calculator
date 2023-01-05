# Take input for the year to be checked 
year = int(input("Which year do you want to check? "))

# To find the leap year. A year is a leap year, if it's evenly divisible by 4. 
# Except it's also evenly divisible by 100, in which case it's no longer a leap year
#(if it's not evenly divisible by 100, it's still a leap year). 
# Unless the number after being evenly divisible by 100, is also evenly divisible by 400. If it is, then it's still a leap year, if it's not, then it's not a leap year. 
if year % 4 == 0 and year % 100 != 0:
    print("Leap year.")
elif year % 4 != 0:
    print("Not leap year.")    
elif year % 4 == 0 and year % 100 == 0 and year % 400 !=0:
    print("Not leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
    print("Leap Year.")
