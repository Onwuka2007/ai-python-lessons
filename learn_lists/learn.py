# name = input('What is your name? ')
# print(f'Hello, {name.strip()}!')

# x = int(input('Enter a number: '))
# y = int(input('Enter another number: '))

# foramts the sum of x and y to 2 decimal places and adds commas for thousands (:, and .2f)
# print(f'The sum of {x} and {y} is {x + y:,.2f}.')

# Functions
# def main():
#     x = int(input('Enter a number: '))
#     print('x squared is', square(x))
    
# def square(n):
#     return n * n

# main()

# Conditionals
# x = int(input('What is x? '))
# y = int(input('What is y? '))

# if x < y:
#     print('x is less than y')
# elif x > y:
#     print('x is greater than y')
# else:
#     print('x and y are equal')


# def main():
#     x = int(input('What is x? '))
#     # if is_even(x):
#     #     print('x is even')
#     # else:
#     #     print('x is odd')
#     print('x is even' if is_even(x) else 'x is odd')
        
# def is_even(n):
#     return n % 2 == 0

# main()

# Using match
# name = input("What is your name? ").strip()

# match name:
#     case "Harry" | 'Hermione' | "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case "Luna":
#         print("Ravenclaw")
#     case "Cedric":
#         print("Hufflepuff")
#     case _:
#         print("Who?")

# loops
i = 0

# while i < 3:
#     print('meow')
#     i += 1


# for _ in range(3):
#     print('meow\n', end='' * 3)
        
# Purposeful infinite loop (until user enters a positive integer)
# while True:
#     n = int(input('What is n? '))
#     if n > 0:
#         break
#     else:
#         print('n must be a positive integer.')
#         continue
    
# for _ in range(n):
#     print('meow')


# Working with Lists
# students = ['Hermione', 'Harry', 'Ron']

# # for i, student in enumerate(students):
# #     print(f"{i + 1}. {student}")

# for i in range(len(students)):
#     print(f"{i + 1}. {students[i]}")

# dicts
# student = {
#     'name': 'Hermione Granger',
#     'house': 'Gryffindor',
#     'patronus': 'Otter'
# }

# print(student['name'])

# A list of dictionaries
# students = [
#     {'name': 'Hermione Granger', 'house': 'Gryffindor', 'patronus': 'Otter'},
#     {'name': 'Harry Potter', 'house': 'Gryffindor', 'patronus': 'Stag'},
#     {'name': 'Ron Weasley', 'house': 'Gryffindor', 'patronus': 'Jack Russell Terrier'},
#     {'name': 'Draco Malfoy', 'house': 'Slytherin', 'patronus': None}
# ]

# for student in students:
#     name = student['name']
#     house = student['house']
#     patronus = student['patronus']
#     print(f"{name} is in {house} and their patronus is {patronus if patronus else 'No patronus'}.")

# mario
# for _ in range(3):
#     print('#')


# def main():
#     size = int(input('What size square? '))
#     print_square(size)

# def print_square(size):
#     for _ in range(size):
#         print('#' * size)

# main()

#  Execption Handling
# def main():
#     x, attempts = getInt('What is x? ')
#     # print(f'Success after {if attempts > 0: attempts= attempts+1} attempts is {x}')
#     print(f"Success after {attempts + 1 if attempts == 0 else attempts} {'attempt' if attempts == 1 or attempts == 0 else 'attempts'}!")
    
# def getInt(prompt: str): 
#     attempts = 0
#     while True:
#         try: 
#             x = int(input(prompt))
#         except ValueError:
#             attempts += 1
#             print(f'Attempt {attempts} is not an integer')
#         else:
#             return x, attempts

# main()

# 
# import random, statistics, sys

# coins = random.choice(["heads", "tails"])
# print(coins)

# number = random.randint(1, 20)
# print(number)

# get_av = statistics.mean([100, 90])
# print(get_av)

# if len(sys.argv) < 2:
#     sys.exit('Too few argument')

# for arg in sys.argv[1:len(sys.argv)]:
#     print('My first name is', arg)

# Packages
# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow('hello', sys.argv[1])

# APIs
# import requests
# import sys
# import json

# if len(sys.argv) != 2:
#     sys.exit()
    
# response = requests.get('https://itunes.apple.com/search?entity=song&limit=3&term=' + sys.argv[1])

# # to beautify
# # print(json.dumps(response.json(), indent=3))

# o = response.json()
# for i, result in enumerate(o['results']):
#     print(f"{i+1}. \n Track: {result['trackName']}")


# Using __name__ for import (from text_utils.py)
# from text_utils import slugify
# from text_utils import  truncate_text

# def main():
#     blog_title = "Transitioning from JavaScript to Python is Fun"
    
#     short_title = truncate_text(blog_title, 25)
#     url_slug = slugify(blog_title)
    
#     print(f"Original: {blog_title}")
#     print(f"Truncated: {short_title}")
#     print(f"Slug: {url_slug}")

# main()

# Unit testing this for squares..
# def main():
#     x = int(input('Enter a number: '))
#     sq = calc_square(x)
#     print(f'The square is {sq}')
    
# def calc_square(num):
#     return num * num

# if __name__ == '__main__':
#     main()

# Unit testing this for strings
def main():
    n = input('Enter your name: ')
    print(hello(n))    
    
def hello(name='world'):
    return f'Hello {name}'
    
if __name__ == '__main__':
    main()