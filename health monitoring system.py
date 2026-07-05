print("====health monitoring system====")

name = input("enter name: ")
age = int(input("enter age: "))
height = float(input("enter height (in meters):"))
weight = float(input("enter weight (in kgs):"))
heart_rate = int(input("enter heart rate (bpm):"))
temperature = float(input("enter body temperature(°C):"))

#bmi calculation
bmi = weight / (height*height)

print("\n----health report----")
print("name:",name)
print("age:",age)
print("height:","m")
print("weight:", weight, "kg")
print("heart rate:", heart_rate,"bpm")
print("temperature:",temperature,"(°C):")
print("bmi:",round(bmi,2))

#bmi status
if bmi<18.5:
    print("bmi status: underweight")
elif bmi<25:
    print("bmi status:normal")
elif bmi < 30:
    print("bmi status:overweight")
else:
    print("bmi status: obese")

    # heart rate status
    if heart_rate <60:
        print("heart rate: low")
    elif heart_rate <=100:
        print("heart rate: normal")
    else:
        print("heart rate : high")

        # temperature status
        if temperature <36.1:
            print("temperature: low")
        elif temperature <=37.2:
            print("temperature:normal")
        else:
            print("temperature : high (possible fever)")

            print("\nstay healthy and drink water consistently!")