import numpy as np
import matplotlib.pyplot as plt
def cMode():
    print("Calculate Mode")
    prob = ""
    while prob != "q":
        try:
            print("Problem:")
            prob = input()
            print(eval(bytes([ord(p) for p in prob])))
        except:
            if prob != "q":
                print("Input Invalid")
def gMode():
    print("Graphing Mode")
    eq,r1,r2 = "",0,0
    while eq != "q":
        try:
            print("Equation")
            eq = input()
            if eq == "q":
                break
            print("Enter x range:")
            r1 = input()
            if r1 == "q":
                break
            else:
                r1 = int(r1)
                print("Enter y range:")
            print("Enter range 2")
            r2=input()
            if r2 == "q":
                break
            else:
                r2 = int(r2)
            x = np.array(range(int(r1),int(r2)))
            y = eval(bytes([ord(p) for p in eq]))
            plt.plot(x,y)
            plt.show()
        except:
            if eq != "q":
                print("Invalid Input")
        mode = ""

        while mode != "q":
            print(""" 
            1.n (Standard Calculator)
            2. g (GDC) 
            3. h (Help
            4. q (Quit)
            """)
            mode = input.lower()
            if mode == "n":
                cMode()
            if mode == "g":
                gMode()
            if mode == "h":
                print("""
                1. Brackets cannot be used in multiplcation
                Use 'np.' prior to any graphing function
                """)
                print("")

