while True:
    try:
        height = float(input("Enter your height (in meters): "))
        weight = float(input("Enter your weight (in kg): "))
        break
    except ValueError:
        print("Please enter numbers only for height and weight.\n")

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
