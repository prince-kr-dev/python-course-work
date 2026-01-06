'''
# Map

l = [2,4,5,8]

square = lambda x : x*x

sqrdList = map(square, l)

print(list(sqrdList))
'''

'''
# Filter
nums = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, nums)
print(list(result))
'''


from functools import reduce

l = [3,6,7,3]

result = reduce(lambda a,b : a+b , l)

print(result)