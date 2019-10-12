print("Input your height in inches and feet")
h_ft = int(input("\nEnter Height in feet:"))
h_inch = int(input("\nEnter height in inches:"))
i = 2.54 #cm in inch
f = 30.48 #cm in feet
inch_cm = h_inch * i
feet_cm = h_ft * f
height = round(inch_cm + feet_cm)
print("\nHeight is",height,"cm")
