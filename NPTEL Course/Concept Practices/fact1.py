"""
def maker(n):
    def action(x):
        return x ** n
    return action
"""
def maker(n):
    return lambda x: x ** n

h = maker(2)
print(h)


print(h(3))
print(h(4))
