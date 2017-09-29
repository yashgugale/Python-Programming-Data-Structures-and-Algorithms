x = 100

def f1():
    x = 200
    print("x is used locally as well. The local value of x is: ", x)
    print("local namespace: ",locals())
f1()

print("\nThe global value of x does not change. It is 100. Check : ",x)
print("global namespace: ", globals())
