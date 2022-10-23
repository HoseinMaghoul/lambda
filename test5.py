


list_ = [1, 2, 3, 4, 5, 6, 7]


def add(l):
    return l ** 2






def map_(fun, l):
    return [fun(e) for e in l]



print(map_(add, list_))
    
print(list(map(add, list_)))


def is_even(l):
    return l % 2 == 0

print(list(filter(is_even, list_)))



#--------------------------------------------------------------------------------------

# kar ba lambda piyade sazi mafahim bala b sorate tak khati ba lambda


print(list(map(lambda num: num ** 2, list_)))
print(list(filter(lambda num: num % 2 == 0, list_)))



v1 = [1, 3, 5, 7]
v2 = [0, 2, 4, 8]

print(sum(list(map(lambda x,y: x * y, v1, v2))))

#-----------------------------------------------------------------

d = {"hosein": 20, "hadi":9.5, "bri":17}


print(sorted(d, key=lambda k:d[k], reverse=True))


# -------------------------------------------------------------------------

print([x ** 2 for x in range(0,9)if x % 2 ==0]) # list compristion

print(list(filter(lambda x: x % 2 ==0, map(lambda x: x ** 2 ,range(10)))))

