x = 10
for i in range(0,10):
    print("loop executed for foll times: ",i)
    if i == 5:
        break
else:
    x = 11
print(x)
print("If x is = 11, then full loop was iterated and else changes the value of x:",x,"otherwise the for loop broke in between")
