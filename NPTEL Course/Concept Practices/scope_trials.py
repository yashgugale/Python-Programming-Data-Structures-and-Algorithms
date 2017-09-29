x = 100
print("Global value of x: ",x)
def f1():
    x = 20
    print("The value of x in f1(): ",x)
    def f2():
        print("The value of x in f2(): ",x)
        def f3():
            global x
            x = 500
            print("The value of x in f3(): ", x)
            def f4():
                print("The value of x in f4(): ", x)
                def f5():
                    global x
                    x = 300
                    print("The value of x in f5(): ", x)
                f5()
            f4()
        f3()
    f2()
    print("The value of x after all function calls, in f1(), is: ", x)
f1()
print("Final global value of x: ", x)

# this shows that until x is made global, all the functions will use the prior value
# of x. When declared global, then onwards, the new assigned value will be used.

# When 'global x' is used, only the manipulation from that function will happen to the 
# global copy and the other functions will have to again use 'global' to manipulate the
# global x again? - Yes.

# Logic Follow-up:
""" -Initially x = 100.
    -Then in f1(), it is made 20. Her, x is a local variable, so x = 20 is limited only
     till f1() ie it has a local scope wrt to f1().
    -Now, f2() is just printing x. But according to LEGB, it will search in the enclosing
     scope as it does not find it in its local scope. Hence, value of x = 20
    -Further, f3() makes 'global x' declaration. Hence, it is now manipulating the global
     copy of x. Hence, f3() prints x = 500. f4() also prints x = 500 by LEGB rule as x is
     500 in f3() ie its enclosing scope.
    -Now, f5() makes 'global x' and assigns x to 300. Therefore, now global x = 300
    -Last statement of f1() uses local copy of x, hence, prints x = 20
    -Finally, the last statement of the program prints x = 300 as it is displaying the
     global x which was changed to 300 by function f5()

"""
