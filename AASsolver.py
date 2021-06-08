import math
import MethodData

def solverangle(angleA, sideA, sideB, angleB, sideC, angleC, xDP):

        xDP = xDP
        if angleA > 0 and angleB > 0:
            angleC = 180 - (angleA+angleB)
        elif angleA > 0 and angleC > 0:
            angleB = 180 - (angleA+angleB)
        elif angleB > 0 and angleC > 0:
            angleA = 180 - (angleC+angleB)
        
        if (angleA <= 0) or (angleB <= 0) or (angleC <= 0):
            matherror()
        elif (angleA + angleB + angleC) != 180:
            matherror()
        else:
            sidesolver(angleA, sideA, sideB, angleB, sideC, angleC, xDP)

def sidesolver(angleA, sideA, sideB, angleB, sideC, angleC, xDP):
    try:
        angleA_radians = math.radians(angleA)
        angleB_radians = math.radians(angleB)
        angleC_radians = math.radians(angleC)
        if sideA > 0:
            sideB = ((sideA*math.sin(angleB_radians))/(math.sin(angleA_radians)))
            sideC = math.sqrt((sideA*sideA)+(sideB*sideB) - 2*sideA*sideB*(math.cos(angleC_radians)))
        elif sideB > 0:
            sideA = ((sideB*math.sin(angleA_radians))/math.sin(angleB_radians))
            sideC = math.sqrt((sideA*sideA)+(sideB*sideB) - 2*sideA*sideB*(math.cos(angleC_radians)))
        elif sideC > 0:
            sideB = ((sideC*math.sin(angleB_radians))/math.sin(angleC_radians))
            sideA = math.sqrt((sideB*sideB)+(sideC*sideC)-2*sideB*sideC*(math.cos(angleA_radians)))

        if (angleA == 60) or (angleB == 60) or (angleC == 60):
            triangle = "Equilateral"
        elif (angleA == 90) or (angleB == 90) or (angleC == 90):
            triangle = "Right Angled"
        elif (sideA != sideB) and (sideA != sideC) and (sideB != sideC):
            triangle = "Scalene"
        else:
            triangle = "Isosceles"

        resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP, triangle)
    except ValueError:
        matherror()

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