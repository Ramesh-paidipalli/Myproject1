

# l = [1,2,3,4,5,6]
#
# print(list(map(lambda x:x*x,l)))

# test_list = [{"dat": 2, "best" : 4},
# {"dat": 2, "is" : 3, "best" : 4},
# {"rat": 2}]
#
# for i in test_list:
#     l=len(i)
#     print(max((i)))
def div_dec(func):
    def inner(a,b):
        if b<0 and a<0:
            return -(-b),-(-a)
        else:
            return -b,-a
            return func(a,b)
    return inner

@div_dec
def div_num(a,b):
    return a,b

print(div_num(-5,-3))


