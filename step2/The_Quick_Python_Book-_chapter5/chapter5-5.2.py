'''Using what you know about the len()
function and list slices, how would you combine the two to get the second half
of a list when you don’t know what size it is? Experiment in the Python shell
to confirm that your solution works.'''

a = [1,2,3,4,5,6,7,8,9]
b = ['a','b','c','d','e','f','g','h']

def second_half(var):
    n = len(var)
    if n%2 == 0 :
        beg = int(len(var)/2)
    else:
        beg = int(len(var)/2)+1
    answer = var[beg:]
    return answer

print(second_half(a))     # will print [6, 7, 8, 9]
print(second_half(b))     # will print ['e', 'f', 'g', 'h']
