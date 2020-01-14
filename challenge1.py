"""
The fibonnacci sequence is created by starting with the sequence {0,1},
then adding the previous 2 terms to get the next term:

f1: 0
f2: 1
f3: 0+1 = 1
f4: 1+1 = 2
f5: 1+2 = 3
f6: 2+3 = 5
f7: 3+5 = 8

Solve the following problems:

1) What is the first fibonacci number that is evenly divisble by 117?
2) What is the sum of the first five even fibonacci numbers

"""

a = 0
b = 1
count = 0
s = 0
for i in range(1,1000):
    a,b = b, a+b
    if b % 2 == 0:
        print(b)
        count = count + 1
        s = s + b
    if count == 5:
        break

print("s: ",s)