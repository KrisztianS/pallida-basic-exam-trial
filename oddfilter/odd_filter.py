# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

numbers_to_filter = [1, 2, 3, 4, 5]
odd_numbers = []

def odd_filter(numbers_to_filter):
    for number in numbers_to_filter:
        if number % 2 > 0:
            odd_numbers.append(number)
    return(odd_numbers)
              
print(odd_filter(numbers_to_filter))