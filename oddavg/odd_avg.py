# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(numbers):
    try:
        odd_numbers = []
        sum_odds = 0
    
        for number in numbers:
            if number %2 != 0:
                odd_numbers.append(number)
    
        for number in odd_numbers:
            sum_odds += number
        return sum_odds / len(odd_numbers)
        
    except ZeroDivisionError:
        return 0
                    
print(odd_average([1, 2, 3, 4, 5, 8, 4, 3, 9]))