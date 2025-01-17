import math
import MethodData

def anglesolver(angleA, angleB, angleC, sideA, sideB, sideC, xDP):
    numerator = (sideB*sideB+sideC*sideC-sideA*sideA)
    denominator = (2*sideB*sideC)
    angleA_radians = math.acos(numerator/denominator)
    angleA = math.degrees(angleA_radians)
    angleB_radians = math.asin(math.sin(angleA_radians)*sideB/sideA)
    angleB = math.degrees(angleB_radians)
    angleC = 180 - (angleA+angleB)
    if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
        matherror()
    elif (angleA + angleB + angleC) != 180:
        matherror()
    else:
        if (angleA == 60) or (angleB == 60) or (angleC == 60):
            triangle = "Equilateral"
        elif (angleA == 90) or (angleB == 90) or (angleC == 90):
            triangle = "Right Angled"
        elif (sideA != sideB) and (sideA != sideC) and (sideB != sideC):
            triangle = "Scalene"
        else:
            triangle = "Isosceles"
    resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP, triangle)

def retryer():
    retry = input("Would you like to retry? (Y/N): ")
    if retry == "Y" or retry == "y":
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
        xDP_str = input("To what decimal place would you like your answers to be given in?: ")
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
        print("ERROR: Invalid input(s)")
        print("--------------------------------------------------")
        retryer()

def resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP, triangle):
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
    print("Your triangle is", triangle)
    print("--------------------------------------------------")
    retryer()

def matherror():
    print("ERROR: A triangle with these values cannot exist")
    print("--------------------------------------------------")
    retryer()