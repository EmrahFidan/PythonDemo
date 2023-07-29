# Body Mass Index 

def calculate_body_mass_index(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))

bmi = calculate_body_mass_index(height, weight)
print("Body Mass Index (BMI):", bmi)
print()

category = get_bmi_category(bmi)
print("BMI Category:", category)
