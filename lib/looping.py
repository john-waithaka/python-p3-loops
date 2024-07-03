#!/usr/bin/env python3

# def happy_new_year():
#     # code goes here!
#     pass

# def square_integers(int_list):
#     # code goes here!
#     pass

# def fizzbuzz():
#     # code goes here!
#     pass


#test 1 passed
# /*
#   Write a method `happy_new_year` that outputs numbers starting at 10 and
#    counting down to 1. After reaching 1, print out "Happy New Year!"
# */
# function happyNewYear() {
#   let counter = 10;
#   while (counter > 0) {
#     console.log(counter);
#     counter--;
#   }
#   console.log("Happy New Year!");
# }



def happy_new_year():
  """Counts down from 10 to 1 and prints "Happy New Year!" at the end."""
  for counter in range(10, 0, -1):
    print(counter)
  print("Happy New Year!")

# OR
# def happy_new_year():
#     countdown = 10
#     while countdown in range(10, 0, -1):
#         print(countdown)
#         countdown -= 1
#  print("Happy New Year!")



# test 2 failed
# /* 
#   Write a method `fizzbuzz_printer` that prints the numbers from 1 to 100. For
#   multiples of three, print "Fizz" instead of the number and for the multiples
#   of five print "Buzz". For numbers which are multiples of both three and five,
#   print "FizzBuzz".
# */
# function fizzbuzzPrinter() {
#   for (let num = 1; num <= 100; num++) {
#     console.log(fizzbuzz(num));
#   }
# }

# function fizzbuzz(num) {
#   if (num % 3 === 0 && num % 5 === 0) {
#     return "FizzBuzz";
#   } else if (num % 3 === 0) {
#     return "Fizz";
#   } else if (num % 5 === 0) {
#     return "Buzz";
#   } else {
#     return num;
#   }
# }

# def fizzbuzz():
#     # code goes here!
#     pass


# def fizzbuzz(num):
#   if num % 3 == 0 and num % 5 == 0:
#     return "FizzBuzz"
#   elif num % 3 == 0:
#     return "Fizz"
#   elif num % 5 == 0:
#     return "Buzz"
#   else:
#     return num

# def fizzbuzz_printer():
#   """Prints FizzBuzz sequence for numbers from 1 to 100."""

#   for num in range(1, 101):
#     print(fizzbuzz(num))


def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

# #test 3 reverse string

# /*
#   Write a method `reverse_string` that takes one argument, a string, and reverses
#   it. Don't use the built-in `.reverse` method. Instead, loop through the
#   characters in the input string and reverse it.
# */
# function reverseString(str) {
#   let reversedStr = "";
#   for (let i = 0; i < str.length; i++) {
#     reversedStr = str[i] + reversedStr;
#   }
#   return reversedStr;
# }



def reverse_string(str):
  """Reverses the given string without using the built-in .reverse() method.

  Args:
      str: The string to reverse.

  Returns:
      The reversed string.
  """

  reversed_str = ""
  for char in str:
    reversed_str = char + reversed_str  # Prepend each character
  return reversed_str



#test 4 square integers
# /*
# Write a function `square_integers()` that takes one argument, a list of
# integers and returns the list of squared elements.
# */
# function square_integers(int_list){
#   return int_list.map((num) => Math.pow(num, 2) )
# }


def square_integers(int_list):
  """Squares all elements in the given list of integers and returns a new list with the squares.

  Args:
      int_list: A list of integers.

  Returns:
      A new list containing the squares of the elements in the input list.
  """

  return [num**2 for num in int_list]  # List comprehension with map equivalent

# or 
# def square_integers(int_list):
#     return [i ** 2 for i in int_list]
