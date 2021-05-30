# my_number = 1

# while (my_number <= 100):
#   print(my_number)
#   # increase my_number by 1
#   my_number += 1

# for i in range(0, 20):
#   for j in range(0, 30):
#     print('*', end='');
#   print()
    



# if (my_number == 0):
#   print("HI!")

index = 1

while (index <= 100):
    
  if index % 3 == 0 and index % 5 == 0:
    print("FizzBuzz")
  elif index % 3 == 0: 
    print("Fizz") 
  elif index % 5 == 0: 
    print("Buzz")
  else:
    print(index)
  
  index += 1