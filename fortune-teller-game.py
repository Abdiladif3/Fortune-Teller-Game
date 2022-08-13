print("Hi! Welcome to the fortune teller game.\n")
while True:
  print('---------------------------------------------------- \n')
  prediction = input('What is your prediction? \n')
  
  while True:
    color = input('Choose a color. green, blue, orange, red: \n').lower()
    color_options = ['green', 'blue', 'orange', 'red']
    if color in color_options:
      print("You chose: ")
      print('-'.join(color[i] for i in range(0, len(color))))
      print(f"This color has {len(color)} letters, so let's")
      print(f"move the fortune teller {len(color)} times. \n")
      break
    else:
      print("Please choose a color from the given options.")
      continue
  
  
  color_length = len(color)
  
  final_digit = 0
  
  even_digit_options = [1, 2, 5, 6]
  odd_digit_options = [3, 4, 7, 8]
  
  
  # COLOR LETTER LENGTH EVEN
  if color_length % 2 == 0: 
    while True:
      choice_1_1 = int(input("Choose a number. 1, 2, 5, 6: \n"))
      if choice_1_1 in even_digit_options:
        # CHOICE 1.1:
        if choice_1_1 % 2 == 0:    
          while True:
            choice_2_1 = int(input("Choose another number. 1, 2, 5, 6: \n"))
            if choice_2_1 in even_digit_options:
              # CHOICE 2.1:
              if choice_2_1 % 2 == 0:
                while True:
                  choice_3_1 = int(input("Choose the last number. 1, 2, 5, 6: \n"))
                  if choice_3_1 in even_digit_options:
                    # CHOICE 3.1:
                    final_digit += choice_3_1
                    break
                  else:
                    print("Please choose a digit from the given options.")
                    continue      
              else:
                while True:
                  choice_3_2 = int(input("Choose the last number. 3, 4, 7, 8: \n"))
                  if choice_3_2 in odd_digit_options:
                    # CHOICE 3.2:
                    final_digit += choice_3_2
                    break
                  else:
                    print("Please choose a digit from the given options.")
                    continue
              break
            else:
              print("Please choose a digit from the given options.")
              continue
        else:
          while True:
            choice_2_2 = int(input("Choose another number. 3, 4, 7, 8: \n"))
            if choice_2_2 in odd_digit_options:
              # CHOICE 2.2:
              if choice_2_2 % 2 == 0:
                while True:
                  choice_3_3 = int(input("Choose the last number. 3, 4, 7, 8: \n"))
                  if choice_3_3 in odd_digit_options:
                    # CHOICE 3.3:
                    final_digit += choice_3_3
                    break
                  else:
                    print("Please choose a digit from the given options.")
                    continue
              else:
                while True:
                  choice_3_4 = int(input("Choose the last number. 1, 2, 5, 6: \n"))
                  if choice_3_4 in even_digit_options:
                    # CHOICE 3.4:
                    final_digit += choice_3_4
                    break
                  else:
                    print("Please choose a digit from the given options.")
                    continue
              break
            else:
              print("Please choose a digit from the given options.")
              continue 
        break
      else:
        print("Please choose a digit from the given options.")
        continue
  # COLOR LETTER LENGTH ODD
  else:
    while True:
      choice_1_2 = int(input("Choose a number. 3, 4, 7, 8: \n"))
      if choice_1_2 in odd_digit_options:
        # CHOICE 1.2:
        if choice_1_2 % 2 == 0:    
          while True:
            choice_2_3 = int(input("Choose another number. 3, 4, 7, 8: \n"))
            if choice_2_3 in odd_digit_options:
              # CHOICE 2.3:
              if choice_2_3 % 2 == 0:
                while True:
                  choice_3_5 = int(input("Choose the last number. 3, 4, 7, 8: \n"))
                  if choice_3_5 in odd_digit_options:
                    # CHOICE 3.5:
                    final_digit += choice_3_5
                    break
                  else:
                    print("Please choose a digit from the given options.")
                    continue
              else:
                while True:
                  choice_3_6 = int(input("Choose the last number. 1, 2, 5, 6: \n"))
                  if choice_3_6 in even_digit_options:
                    # CHOICE 3.6:
                    final_digit += choice_3_6
                    break
                  else:
                    print("Please choose a digit from the given options.")
                    continue
              break
        else:
          while True:
            choice_2_4 = int(input("Choose another number. 1, 2, 5, 6: \n"))
            if choice_2_4 in even_digit_options:
              # CHOICE 2.4:
              if choice_2_4 % 2 == 0:
                while True:
                  choice_3_7 = int(input("Choose the last number. 1, 2, 5, 6: \n"))
                  if choice_3_7 in even_digit_options:
                    # CHOICE 3.7:
                    final_digit += choice_3_7
                    break
                  else:
                    print("Please choose a digit from the given options.")
                    continue     
              else:
                while True:
                  choice_3_8 = int(input("Choose the last number. 3, 4, 7, 8: \n"))
                  if choice_3_8 in odd_digit_options:
                    # CHOICE 3.8:
                    final_digit += choice_3_8
                    break
                  else:
                    print("Please choose a digit from the given options.")
                    continue
              break
            else:
              print("Please choose a digit from the given options.")
              continue 
        break
      else:
        print("Please choose a digit from the given options.")
        continue
  
  
  final = ['Definitely', 'Possibly', 'No way', 'Yup', 'Sorry, no luck', 'Yeah you know it', 'In your dreams', 'Probably not']
  
  answer = (final[final_digit - 1])
  
  print(f"Your final prediction is '{prediction}' and the answer to that is...")
  print(f"...{answer}!\n")

  continuation = input("Do you want to keep playing? Type Yes or 'y' if you do, or type anything else if you want to quit: \n")
  continuation = continuation.lower()
  if continuation in ['yes', 'y']:
    continue
  else:
    print("Thank you for playing the fortune teller game! ")
    break
