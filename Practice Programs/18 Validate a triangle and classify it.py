'''Validate a triangle and classify it: Accept three angles. Check whether they form a valid 
   triangle or not. If valid, classify it as acute angled, obtuse angled or right angled triangle.'''

a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))

if a>0 and b>0 and c>0 and a+b+c==180:
    print("The angles form a valid triangle")
    if a==90 or b==90 or c==90:
        print("The triangle is right-angled triangle")
    elif a>90 or b>90 or c>90:
        print("The triangle is obtuse-angled triangle")
    else:
        print("The triangle is acute-angled triangle")
else:
    print("The angles didn't form a valid triangle!")