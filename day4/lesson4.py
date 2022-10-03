# name1 = input("enter name1: ")
# name2 = input("enter name: ")
# vowels_in_name1 = 0
# vowels_in_name2 = 0

# symbol in "aeiou"

# my_name = "luka"
# for char in my_name:
#     print(char) 
# for i in range(10):
#     print(str(i)  + "ა")

# name1 = input("enter name1: ")
# name2 = input("enter name: ")
# symbol in "aeiou"

# amount_of_vowels_in_name1 = 0
# amount_of_vowels_in_name2 = 0

# for char in name1:
#      if char in "aeiou":
#         amount_of_vowels_in_name1 += 1
        
# for char in name2:
#     if char in "aeiou":
#         amount_of_vowels_in_name2 += 1

#         if amount_of_vowels_in_name1 > amount_of_vowels_in_name2:
#             print("the amount of vowels in name1 is more and it comtains {} vowels".format(amount_of_vowels_in_name1))
# if amount_of_vowels_in_name1 < amount_of_vowels_in_name2:
#      print("the amount of vowels in name2 is more and it contains {} vowels".format(amount_of_vowels_in_name2))
# else:
#     print("they have equal amount of vowels")

name1 = input("enter name1: ")
name2 = input("enter name2: ")


amount_of_consonants_in_name1 = 0
amount_of_consonants_in_name2 = 0
for char in name1:
    if char not in "aeiou":
        amount_of_consonants_in_name1 += 1

for char in name2:
    if char not in "aeiou":
         amount_of_consonants_in_name2 += 1

         if amount_of_consonants_in_name1 > amount_of_consonants_in_name2:
            print("the amount of consonants in name1 is more and it comtains {} consonants".format(amount_of_consonants_in_name1))
if amount_of_consonants_in_name1 < amount_of_consonants_in_name2:
     print("the amount of consonants in name2 is more and it contains {} consonants".format(amount_of_consonants_in_name2))
else:
    print("they have equal amount of consonants")
    