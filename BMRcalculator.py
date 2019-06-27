#References:
# 1) https://programmingwithmosh.com/python/python-3-cheat-sheet/
# 2) https://www.calculator.net/calorie-calculator.html

def askHeight():
    return float(input("Your height in CM:"))
def askWeight():
    return float(input("Your weight in KG:"))
def askAge():
    return float(input("Your age:"))
def returnBMR():
    return (6.25*askHeight())+(10*askWeight())-(5*askAge())
#Printer
def calRes(BMR):
    print("Maintain weight: " + str(BMR) + " Calories/day")
    print("\n----------------------Weight Loss----------------------")
    print("Mild weight loss (-0.25KG/week): " + str(BMR-250) + " Calories/day")
    print("Weight loss (-0.5KG/week): " + str(BMR-500) + " Calories/day")
    print("Extreme Weight loss (-1KG/week): " + str(BMR-1000) + " Calories/day")
    print("\n----------------------Weight Gain----------------------")
    print("Mild weight gain (+0.25KG/week): " + str(BMR+250) + " Calories/day")
    print("Weight gain (+0.5KG/week): " + str(BMR+500) + " Calories/day")
    print("Extreme Weight gain (+1KG/week): " + str(BMR+1000) + " Calories/day\n")

#Main
BMR = 0 #To declared as global variable

print("********************************")
print("*                              *")
print("*  Welcome to Calorie Counter  *")
print("*                              *")
print("********************************")
print("\nThe results of this calculator are only estimated. Use at your own risk!\n")

print("\n1 - Sedentary: Little to no exercise")
print("2 - Light: Exercise 1-3 times/week")
print("3 - Moderate: Exercise 4-5 times/week")
print("4 - Active: Daily Exercise or intense Exercise 3-4 times/week")
print("5 - Very Active: Intense Exercise 6-7 times/week")
print("6 - Extra Active: Very intense daily exercise, physical job")
activeRate = int(input("Activity (1-6):"))

gender = input("Please input your Gender (M - Male, F - Female):").upper()
if gender == 'M': #Male BMR Calculation
    BMR = returnBMR() + 5 
elif gender == 'F': #Female BMR Calculation
    BMR = returnBMR() - 161.0

print("\nYour Basal Metabolic Rate is:" + str(BMR) + " Calories/day")

if activeRate == 1: #Sedentary: Little to no exercise -- *1.2
    BMR = BMR * 1.2
elif activeRate == 2: #Light: Exercise 1-3 times/week -- *1.375
    BMR = BMR * 1.375
elif activeRate == 3: #Moderate: Exercise 4-5 times/week -- *1.465
    BMR = BMR * 1.465
elif activeRate == 4: #Active: Daily Exercise or intense Exercise 3-4 Times/week -- *1.55
    BMR = BMR * 1.55
elif activeRate == 5: #Very Active: Intense Exercise 6-7 times/week -- *1.72491694
    BMR = BMR * 1.72491694
elif activeRate == 6:#Extra Active: Very intense daily exercise, physical job -- *1.9
    BMR = BMR * 1.9

BMR = round(BMR)
calRes(BMR)