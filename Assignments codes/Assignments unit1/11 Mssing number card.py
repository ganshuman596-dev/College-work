'''There was a set of cards with numbers from 1 to N. One of the cards is now lost. 
Determine the number on that lost card given the numbers for the remaining cards. 
Given a number N, followed by N - 1 integers - representing the numbers on the remaining 
cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.'''

n = int(input("Enter N: "))
nums = map(int, input("Enter the numbers on available cards: ").split())

actual_sum = n*(n+1)/2
getting_sum = sum(list(nums))
missing = actual_sum-getting_sum

print(f'The missing card has number {int(missing)} on it')