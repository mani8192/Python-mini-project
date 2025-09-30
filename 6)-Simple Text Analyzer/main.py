# small Project: Simple Text Analyze--



# 0-take a string from user.
user_string = input("Enter a string :-")

# 1-Count total characters in the string.
total_char = len(user_string)
print(total_char)

# 2-Count total words.
count_word = len(user_string.split())
print(count_word)

# 3-Count vowels
count_vowel = ('a','e','i','o','u')
vowel = 0
for tex in user_string:
    if tex in  count_vowel:
        vowel += 1
        
print('vowel in user-string' , vowel)
        
# 4-Reverse the string.
string_reverse =  user_string[::-1]
print(string_reverse)

# 5-Convert string to uppercase or lowercase.
# lower
str_lower = user_string.lower()
print(str_lower)

# upper
str_upper = user_string.upper()
print(str_upper)
