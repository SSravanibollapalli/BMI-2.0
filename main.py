height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

int_weight = int(weight)
int_height = float(height)
bmi = ((int_weight) / (int_height ** 2))

rounded_bmi = round(bmi)
if bmi < 18.5:
    print(f"Your BMI is {rounded_bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {rounded_bmi}, you are obese.")
else:
    print(f"Your BMI is {rounded_bmi}, you are clinically obese.")

