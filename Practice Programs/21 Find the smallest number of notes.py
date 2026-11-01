'''Find the smallest number of notes: Accept an amount and determine the minimum number of
   currency notes required using denominations.(500, 200, 100, 50, 20, 10, 5, 1)'''

amt = int(input("Enter the amount: "))
notes = [500, 200, 100, 50, 20, 10, 5, 1]
for note in notes:
    if amt>=note:
        n = amt//note
        amt = amt - (n*note)
        print(f'{n} {"note" if n==1 else "notes"} of ₹{note}')
