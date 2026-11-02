'''Find the missing and duplicate sensor id: Sensor ids should be the integer from 1 to N.
   One id is misssing and another id occurs twice. Given exactly N readings, identify
   the missing and duplicate id'''

ids = map(int, input("Enter the sensor ids from 1 to N: ").split())
ids = list(ids)
for i in range(1, max(ids)+1):
    if i not in ids:
        missing = i 
    if ids.count(i)>1:
        duplicate = i
print("Duplicate is:", duplicate)
print("Missing is:", missing)