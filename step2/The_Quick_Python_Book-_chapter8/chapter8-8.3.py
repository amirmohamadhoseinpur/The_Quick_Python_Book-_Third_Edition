'''Suppose that you have a list x = [1,
3, 5, 0, -1, 3, -2], and you need to remove all negative numbers from
that list. Write the code to do this.
How would you count the total number of negative numbers in a list
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]?
What code would you use to print very low if the value of x is below -5, low
if it’s from -5 up to 0, neutral if it’s equal to 0, high if it’s greater than 0 up
to 5, and very high if it’s greater than 5?'''

x = [1, 3, 5, 0, -1, 3, -2]
for i in x:
    if i<0:
        x.remove(i)
print(x)

y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
count = 0
for i in y:
    for j in i:
        if j<0 :
            count+=1
print(count)

x = input("Enter a number please:")
if x < -5:
    print('very low')
elif x < 0:
    print('low')
elif x == 0:
    print('neutral')
elif x>0 and x<=5:
    print('high')
else:
    print('very high')