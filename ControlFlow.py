# print(1)
# print(2)
# print(3)

# age=int(input("Enter Your Age: "))

# #age>=18
# if age>=18:
#     print("You can vote")

# # age<18
# else:
#     print("You cannot")

# a=-10

# if a<5:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("---------")
# else:
#     print("From else block")

# print("Done")


# a=10

# if a>10:
#     print("From if block")
# elif a<10:
#     print("From elif1 block")
# elif a!=10:
#     print("From elif2 block")
# else:
#     print("From else block")

# mark = int(input("Enter your mark: "))
 
# if mark < 0 or mark > 100:
#     print("Invalid mark")
# elif mark >= 90:
#     print("Grade: O")
# elif mark >= 80:
#     print("Grade: A+")
# elif mark >= 70:
#     print("Grade: A")
# elif mark >= 60:
#     print("Grade: B")
# elif mark >= 50:
#     print("Grade: C")
# else:
#     print("Grade: Fail")

# a=10

# if a<=10:
#     if a>10:
#         print("Done")
#     print("Done")

# inp=int(input("Enter Your Number: "))

# if inp>10:
#     if inp>15:
#         print("Very Large")
#     else:
#         print("Large")
# else:
#     if inp<5:
#         print("Very Small")
#     else:
#         print("Small")

bankType="current"
balance=1001

# eligible --> current >1000
# not eligible

# if bankType=="current":
#     if balance>1000:
#         print("Eligible")
#     else:
#         print("Not Eligible")
# else:
#     print("Not Eligible")

if bankType=="current" and balance>1000:
    print("Eligible")
else:
    print("Not Eligible")


