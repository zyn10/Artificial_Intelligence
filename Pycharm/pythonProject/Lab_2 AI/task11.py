marks = {
         'AI':74,
         'CN':76,
         'DS':42,
         'PS':54
         }
sum=0
for i in marks.values():
    sum=sum+i
print("Sum of Marks = ",sum)

print("Subject\t Marks")
for attr, value in marks.items():
    print('  ',attr,'   ',value)

max=0
counter=0
for attr, value in marks.items():
    if max < value: #checking on the basis of marks
        max=value
        objMarks=attr,value
        counter=counter+1
    if counter>4:
        print("Max Marks\t= ", objMarks)
    else:
        counter = counter + 1
min=max
counter=0
for attr, value in marks.items():
    if min > value: #checking on the basis of marks
        min=value
        objMarks=attr,value
        counter=counter+1
    if counter>4:
        print("Min Marks\t= ", objMarks)
    else:
        counter = counter + 1






# Taken help from here
# https://stackoverflow.com/questions/25150955/python-iterating-through-object-attributes