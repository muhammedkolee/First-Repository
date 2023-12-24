def calculate(height, weight):   
    return (weight/(height**2))

height = float(input("Your height: "))
weight = float(input("Your weight: "))

if(height > 5):
    height /= 100

value = calculate(height, weight)

if(value < 18.5):
    print(f"You are underweight.\nYour BMI:{value}")

elif(18.5 <= value < 25):
    print(f"You are healthy weight.\nYour BMI:{value}")

elif(25 <= value < 30):
    print(f"You are overweight.\nYour BMI:{value}")

elif(30 <= value):
    print(f"You are obese.\nYour BMI:{value}")

else:
    print("İncorrect information entry, try again.")