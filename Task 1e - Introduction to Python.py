#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499

#Task 1e - A program to count the occurrence of the letters in strings

#Ask user for string and 3 letters
string = input("Please enter a string: ") 
letters = input("Please enter 3 letters: ").upper()

#Convert letters to make nonsensitive case
letter_set = set(letters)

#Count occurrence of each letter in string
letter_counts = {} 
for letter in letter_set: letter_counts[letter] = string.upper().count(letter)

#display each letter counts
print("Letter counts in string:") 
for letter, count in letter_counts.items(): 
    print(f"{letter}: {count}")