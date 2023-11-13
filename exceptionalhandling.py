
a = input("Enter your Number")

try:
  for i in range(1,11):
    print(f"{a} x {i} = {int(a)*int(i)}")

except:
  print("Invalid Input")