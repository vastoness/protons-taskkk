num = int(input("Enter the fibonacci number : "))

if num < 0:
  print("number must be bigger than zero")
else:
  a, b = 0, 1
  for i in range(num):  
    a, b = b, a + b

  print(f"The {num}th Fibonacci number is: {a}")