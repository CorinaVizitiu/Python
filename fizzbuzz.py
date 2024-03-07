

for nr in range(1,101):
  if nr % 3 ==0 and nr % 5 == 0 :
   print("FizzBuzz")
  elif nr % 5 == 0:
   print("Buzz")
  elif nr % 3 == 0:
   print("Fizz")
  else:
   print(nr)
  