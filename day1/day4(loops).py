from itertools import count

name = ["Rubik" , "Rion" , "Ylli" , "Diell"]
for name in name:
    print(name)

#     test1 = "hello"
#     for test in test1:
#         print(test)
#
# test2 = "hello world"
#
#
# for character in test2:
#     if character == "isalpha()":
#         print(character)
#

#
# numbers = [12, 32, 33, 34, 25]
#
# maximum = numbers[0]
#
# for num in numbers:
#     num > maximum
#     maximum = num
#     print("THE MAX VALUE IS ", maximum)
#
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# numbers = [1,2,3,4,5]
# target = 4
# for number in numbers:
#     print(number)
#     if number == target:
#         print(" Target found ")
#         break
#
# score = [50,68,42,57,78,35,62,92]
# total = 0
# count = 0
#
# for score in score:
#   if score < 50:
#       continue
#       total += score
#       count += 1
# average = total / count if count > 0 else 0
# print("Average score above 50 us", average)
# while True:
#   user_input = input("Enter a possitive number: ")
#
#   if user_input.isnumeric():
#       num = int(user_input)
#
#       if num > 0:
#           break
#
#   print("Error")
# print("you entered a positiv number", number)
total = 0

for number in range(1,11):
    if number % 2 == 0:
        total += number
print(total)