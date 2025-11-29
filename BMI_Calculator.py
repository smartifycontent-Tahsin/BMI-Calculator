try:
    weight= float(input("Enter your weight(in kg): "))
    height= float(input("Enter your height(in m): "))
    bmi= round(weight/(height**2),1)
    if bmi<18.5:
        catagory= "underweight"
    elif 18.5<=bmi<25:
        catagory= "normal"
    elif 25<=bmi<30:
        catagory= "overweight"
    else:
        catagory= "obese"
    print(f"Your BMI is {bmi}. That means you are {catagory}")
except:
    print("Enter a valid number")
