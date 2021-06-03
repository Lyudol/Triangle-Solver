import AASsolver
import SSAsolver1
import SSAsolver2
import AllSideSolver

def methoddatawriter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP_str):
    if angleA_str == "":
        angleA_str = "0"
    else:
        angleA_str = angleA_str

    if angleB_str == "":
        angleB_str = "0"
    else:
        angleB_str = angleB_str

    if angleC_str == "":
        angleC_str = "0"
    else:
        angleC_str = angleC_str

    if sideA_str == "":
        sideA_str = "0"
    else:
        sideA_str = sideA_str

    if sideB_str == "":
        sideB_str = "0"
    else:
        sideB_str = sideB_str

    if sideC_str == "":
        sideC_str = "0"
    else:
        sideC_str = sideC_str

    if xDP_str == "":
        xDP_str == "0"
    else:
        xDP_str = xDP_str 
    
    converter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP_str)

def converter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP_str):
    try:
        angleA = float(angleA_str)
        angleB = float(angleB_str)
        angleC = float(angleC_str)
        sideA = float(sideA_str)
        sideB = float(sideB_str)
        sideC = float(sideC_str)
        xDP = int(xDP_str)
        finder(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
    except ValueError:
        global picker
        def picker():
            try:
                print("""                         A
                        /\ 
                       /  \ 
                    c /    \ b
                     /      \ 
                    /________\ 
                   B    a     C  """)
                            
                print("Please input 3 values, one of which must be a side")
                print("--------------------------------------------------")
                xDP = int(input("To what decimal place would you like your answers to be given in? "))
                print("--------------------------------------------------")
                angleA_str = input("What is your 'A' angle value? (If you don't know just skip): ")
                angleB_str = input("What is your 'B' angle value? (If you don't know just skip): ")
                angleC_str = input("What is your 'C' angle value? (If you don't know just skip): ")
                print("--------------------------------------------------")
                sideA_str = input("What is your 'a' side value? (If you don't know just skip): ")
                sideB_str = input("What is your 'b' side value? (If you don't know just skip): ")
                sideC_str = input("What is your 'c' side value? (If you don't know just skip): ")
                print("--------------------------------------------------")
                methoddatawriter(angleA_str, angleB_str, angleC_str, sideA_str, sideB_str, sideC_str, xDP)
            except ValueError:
                print("--------------------------------------------------")
                print("ERROR: One or more of your inputs was invalid. Please make sure you input a number. No special characters or letters.")
                print("--------------------------------------------------")
                picker()
        print("ERROR: One or more of your inputs was invalid. Please make sure you input a number. No special characters or letters.")
        print("--------------------------------------------------")
        picker()



def finder(angleA, angleB, angleC, sideA, sideB, sideC, xDP):
    if ((angleA > 0 and angleB > 0) or (angleA > 0 and angleC > 0) or (angleB > 0 and angleC > 0)) and ((sideA > 0) or (sideB > 0) or (sideC > 0)):
        AASsolver.solverangle(angleA, sideA, sideB, angleB, sideC, angleC, xDP)
    elif ((angleA > 0 and sideC > 0 and sideB > 0) or (angleB > 0 and sideA > 0 and sideC > 0) or (angleC > 0 and sideB > 0 and sideA > 0)):
        SSAsolver2.CosRuleSide(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
    elif ((angleA > 0 and sideA > 0 and sideC > 0) or (angleB > 0 and sideA > 0 and sideB > 0) or (angleC > 0 and sideB > 0 and sideC > 0)):
        SSAsolver1.SineRuleAng(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
    elif ((angleA > 0 and sideA > 0 and sideB > 0) or (angleB > 0 and sideB > 0 and sideC > 0) or (angleC > 0 and sideA > 0 and sideC > 0)):
        SSAsolver1.SineRuleAng(angleA, angleB, angleC, sideA, sideB, sideC, xDP)
    elif sideA > 0 and sideB > 0 and sideC > 0:
        AllSideSolver.anglesolver(angleA, angleB, angleC, sideA, sideB, sideC, xDP) 
    else:
        print("ERROR: Please input at least 3 values, one of which must be a side")
        print("--------------------------------------------------")
        AASsolver.retry()