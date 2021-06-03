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
            print("ERROR: A triangle with your given values cannot exist.")
            print("--------------------------------------------------")
            retryer()
        elif (angleA + angleB + angleC) != 180:
            print("ERROR: A triangle with your given values cannot exist.")
            print("--------------------------------------------------")
            retryer()
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
            resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
        elif sideB > 0:
            sideA = ((sideB*math.sin(angleA_radians))/math.sin(angleB_radians))
            sideC = math.sqrt((sideA*sideA)+(sideB*sideB) - 2*sideA*sideB*(math.cos(angleC_radians)))
            resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
        elif sideC > 0:
            sideB = ((sideC*math.sin(angleB_radians))/math.sin(angleC_radians))
            sideA = math.sqrt((sideB*sideB)+(sideC*sideC)-2*sideB*sideC*(math.cos(angleA_radians)))
            resultreturner(angleA, sideA, sideB, angleB, sideC, angleC , xDP)
    except ValueError:
        print("ERROR: A triangle with your given values cannot exist.")
        print("--------------------------------------------------")
        retryer()

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