# coding:utf-8

print "123"

l1 = range(1, 101)
print sum(l1)


def get_sum(x, y):
    return x + y


print reduce(get_sum, l1)
