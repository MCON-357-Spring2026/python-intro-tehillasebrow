"""
TODO:
1. Print numbers from 1 to 10
2. Print even numbers from 1 to 20
3. Calculate the sum of numbers from 1 to 100
4. Print the multiplication table of 5

"""
print("Print numbers from 1 to 10")
for i in range(10):
    print(i+1)

print(" Print even numbers from 1 to 20")
num = 1
while num <= 20:
    if num % 2 == 0:
        print("Even number:", num)
    num += 1
print("Calculate the sum of numbers from 1 to 100")
nums=0
for i in range(1,101):
    nums+=i
print(nums)
print("Print the multiplication table of 5")
mult=0
while mult<(5*12):
    mult+=5
    print(mult)
