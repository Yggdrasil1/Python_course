# fill the python code

# 1. assign an integer to the variable x
x=-13
# 2. assign the content of x to the variable y
y=x
# 3. increase the content of x by 13
x+=13
# 4. decrease the content of y by 3
y-=3
# 5. assign an empty list to the variable z
z=[]
# 6. put x and y in this list
z.append(x)
z.append(y)
# 7. run this file in Python3 and make sure no error occurs

# 8. push this file in your repository

if __name__ == '__main__':
    assert type(x) is int, 'x is not an integer anymore'
    assert type(y) is int, 'y is not an integer anymore'
    assert type(z) == list, 'z is not a list'
    assert len(z) <= 2, 'list length is too long'
    assert len(z) >= 2, 'list length is too short'
    assert type(z[0]) == int, 'first element in the list is no integer'
    assert type(z[1]) == int, 'second element in the list is no integer'
    print('Congratulations, homework successfully solved!')
