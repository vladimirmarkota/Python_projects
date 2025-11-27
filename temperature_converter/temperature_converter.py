temp = float(input("Input temperature: "))
scale = input("Input temperature scale (C, F, K): ").upper()

#cink = C in K etc.
if scale == "C":
    cink = float(temp + 273.15)
    cinf = float(temp*(9/5) + 32)
    print(f"{temp}{scale} in Kelvins: {cink}")
    print(f"{temp}{scale} in Fahrenheit: {cinf}")
elif scale == "F":
    finc = round(float((temp - 32)*(5/9)),2)
    fink = round(float((temp - 32)*(5/9) + 273.15),2)
    print(f"{temp}{scale} in Celsius: {finc}")
    print(f"{temp}{scale} in Kelvins: {fink}")
elif scale == "K":
    kinc = round(float(temp - 273.15),2)
    kinf = round(float((temp - 273.15)*(9//5) + 32),2)
    print(f"{temp}{scale} in Celsius: {kinc}")
    print(f"{temp}{scale} in Fahrenheit: {kinf}")
else: print("Input valid temperature scale!")

