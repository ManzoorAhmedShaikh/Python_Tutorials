#Exercise # 4 (BASIC)

'''
Q1) Write a program in which you ask the user for the percentage, and
based on that, it should print the Grade.
'''

# percentage = float(input("Enter any percentage: "))
#
# if percentage >= 90:
#     print("Its A-1 Grade")
# elif percentage >= 80 and percentage < 90:
#     print("Its A Grade")
# elif percentage >= 70 and percentage < 80:
#     print("Its B Grade")
# else:
#     print("Fail")

'''
Q8) Write a program that ask the time 
(Morning, Afternoon or Evening), based on that different color 
should print on output (Green, Yellow, Red)
'''

timezone = input("Enter the timezone currently: ")

if timezone == "Morning":
    print("GREEN")
elif timezone == "Afternoon":
    print("YELLOW")
elif timezone == "Evening":
    print("RED")
else:
    print("")