import math
import MethodData

def anglesolver(angleA, angleB, angleC, sideA, sideB, sideC, xDP):
    angleA_radians = math.acos((sideB*sideB)+(sideC*sideC)-(sideA*sideA)/(2*sideB*sideC))
    angleA = math.degrees(angleA_radians)
    angleB_radians = math.asin(math.sin(angleA_radians)*sideB/sideA)
    angleB = math.degrees(angleB_radians)
    angleC = 180 - (angleA+angleB)
    if (angleA + angleB + angleC) != 180:
        print("ERROR: A triangle with your given values cannot exist.")
        print("--------------------------------------------------")
        retryer()
    else:
        resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)

def retryer():
    retry = input("Would you like to retry? (Y/N) ")
    if retry == "Y" or retry == "y":
        print("--------------------------------------------------")
        xDP_str = input("To what decimal place would you like your answers to be given in? ")
        print("--------------------------------------------------")
        print("""                 A
                /\ 
               /  \ 
            c /    \ b
             /      \ 
            /________\ 
           B    a     C  """)
        print("Please input 3 values, one of which must be a side")
        print("--------------------------------------------------")
        angleA_str = input("What is your 'A' angle value? (If you don't know just skip): ")
        angleB_str = input("What is your 'B' angle value? (If you don't know just skip): ")
        angleC_str = input("What is your 'C' angle value? (If you don't know just skip): ")
        print("--------------------------------------------------")
        sideA_str = input("What is your 'a' side value? (If you don't know just skip): ")
        sideB_str = input("What is your 'b' side value? (If you don't know just skip): ")
        sideC_str = input("What is your 'c' side value? (If you don't know just skip): ")
        print("--------------------------------------------------")
        MethodData.methoddatawriter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP_str)
    elif retry == "N" or retry == "n":
        exit()
    else:
        print("--------------------------------------------------")
        print("Invalid input")
        print("--------------------------------------------------")
        retryer()

def resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP):
    print("""             A
            /\ 
           /  \ 
        c /    \ b
         /      \ 
        /________\ 
       B    a     C  """)

    print("Side a =", round(sideA, xDP))
    print("Side b =", round(sideB, xDP))
    print("Side c =", round(sideC, xDP))
    print("Angle A =", round(angleA, xDP),"°")
    print("Angle B =", round(angleB, xDP),"°")
    print("Angle C =", round(angleC, xDP),"°")
    print("If these values do not match the triangle you have in front of you, your triangle is incorrect")
    print("--------------------------------------------------")
    retryer()

def matherror():
    print("ERROR: A triangle with these values cannot exist")
    print("--------------------------------------------------")
    retryer()