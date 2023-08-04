# The program below will receive a number between 0
# and 999,999,999,999,999,999 and write it in words.
import string
special_char = string.punctuation
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
all_chars = special_char
letters = lower_case + upper_case
all_chars = all_chars.replace(".","")
letters = letters.replace("o","")
letters = letters.replace("I","")
letters = letters.replace("l","")
letters = letters.replace("O","")

class DigitsToWords():

  def __init__(self,number):
    self.number = number

  def numbers_to_words(self):
        
    # The if block below terminates the programme if nothing is received.
    if not self.number:
      print("You've not entered anything, run the program again")
      exit()
    # The for loop below removes all 
    # special characters from the number received.
    for x in all_chars:
      if x in self.number:
        self.number = self.number.replace(x,"")
    # The for loop below terminates the programme 
    # if the number received contains any letter except: o, O, I, l.
    for y in letters:  
      if y in self.number:
        print("You've not entered any number, run the program again")
        exit()
    # The if blocks below replace letters o, O, I, l 
    # with numbers 0, 0, 1, 1, respectively.
    if "o" in self.number:
      self.number = self.number.replace("o","0")
      print("Every letter o in the number has been "
            "replaced with 0! Please be sure about that!")
    
    if "O" in self.number:
      self.number = self.number.replace("O","0")
      print("Every letter O in the number has been "
            "replaced with 0! Please be sure about that!")
    
    if "I" in self.number:
      self.number = self.number.replace("I","1")
      print("Every letter I in the number has been "
            "replaced with 1! Please be sure about that!")
    
    if "l" in self.number:
      self.number = self.number.replace("l","1")
      print("Every letter l in the number has been "
            "replaced with 1! Please be sure about that!")
    # The line below revoves any spaces with in the number. 
    self.number = self.number.replace(" ","")
    
    # The dictionaries below declare the numeric value
    # of numbers in words. The idea is to have all numbers 
    # from 0-999 with their corresponding words in one
    # dictionary and then use the dictionary to label
    # all other numbers in the world!
    ones = {0:"zero", 1:"one", 2:"two", 3:"three",
            4:"four", 5:"five", 6:"six", 7:"seven",
            8:"eight", 9:"nine", 10:"ten"}
    
    teens = {11:"eleven", 12:"twelve", 13:"thirteen",
             14:"forteen", 15:"fifteen", 16:"sixteen",
             17:"seventeen", 18:"eighteen", 19:"nineteen"}
    
    tens = {10:"ten", 20:"twenty", 30:"thirty",
            40:"forty", 50:"fifty", 60:"sixty",
            70:"seventy", 80:"eighty", 90:"ninety"}
    
    ones_list = list(ones.items())
    tens_list = list(tens.items())
    # dict1 will have numbers from 21 to 99 
    dict1 = {}
    i = 1
    while i <= 8:
      dict1.update({tens_list[i][0]:tens_list[i][1]})
      j = 1
      while j <= 9:
        dict1[tens_list[i][0]+j] = tens_list[i][1]
        + " " + ones_list[j][1]
        j+=1
      i+=1
    # dict2 will have numbers from 0 to 99         
    dict2 = {}
    dict2.update(ones)
    dict2.update(teens)
    dict2.update(dict1)
    dict2_list = list(dict2.items())

    # dict3 will have numbers from 100 to 999 
    dict3 = {}
    m = 1
    while m <= 9:
      dict3[int(str(m)+'00')] = ones_list[m][1]
      +" "+'hundred'
      k = 1
      while k <= 99:
        dict3[int(str(m)+'00')+k] = ones_list[m][1]
        +" "+'hundred'+ " "+ dict2_list[k][1]
        k+=1
      m+=1
    # dict4 will have numbers from 0 to 999     
    dict4 = {}
    dict4.update(dict2)
    dict4.update(dict3)

    # the method below helps us to separate integers from floating values.
    number_list = self.number.split(".")
    
    # the if block below declares the numeric value of
    # integers from 0 to 999,999,999,999,999,999 in words    
    if len(number_list) == 1:
    
      if len(self.number) <= 3:
        for x,y in dict4.items():
          if x == int(self.number):
            number_in_words = f"{self.number} in words is: {y}"
      elif 4 <= len(self.number) <= 6:
        for x,y in dict4.items():
          if x == int(self.number[-3:]) and x !=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-6:-3]):
            first_3 = b
    
        print_dict = {first_3:"thousand", last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        print_string = ', '.join(print_statement)
        number_in_words = f"{self.number} in words is: {print_string}"
                    
      elif 7 <= len(self.number) <= 9:
        for x,y in dict4.items():
          if x == int(self.number[-3:]) and x !=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-6:-3]) and a !=0:
            second_3 = b
          elif a == 0:
            second_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-9:-6]):
            first_3 = b
    
        print_dict = {first_3:"milllion",
                      second_3:"thousand",
                      last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        print_string = ', '.join(print_statement)
        number_in_words = f"{self.number} in words is: {print_string}"
            
      elif 10 <= len(self.number) <= 12:
        for x,y in dict4.items():
          if x == int(self.number[-3:]) and x !=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-6:-3]) and a!=0:
            third_3 = b
          elif a == 0:
            third_3 = ""      
        for a,b in dict4.items():
          if a == int(self.number[-9:-6]) and a!=0:
            second_3 = b
          elif a == 0:
            second_3 = "" 
        for a,b in dict4.items():
          if a == int(self.number[-12:-9]):
            first_3 = b
    
        print_dict = {first_3:"billlion",
                      second_3:"million",
                      third_3:"thousand",
                      last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        print_string = ', '.join(print_statement)
        number_in_words = f"{self.number} in words is: {print_string}"
        
      elif 13 <= len(self.number) <= 15:
        for x,y in dict4.items():
          if x == int(self.number[-3:]) and x !=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-6:-3]) and a !=0:
            fourth_3 = b
          elif a == 0:
            fourth_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-9:-6]) and a !=0:
            third_3 = b
          elif a == 0:
            third_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-12:-9]) and a !=0:
            second_3 = b
          elif a == 0:
            second_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-15:-12]):
            first_3 = b
    
        print_dict = {first_3:"trillion",
                      second_3:"billion",
                      third_3:"million",
                      fourth_3:"thousand", 
                      last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        print_string = ', '.join(print_statement)
        number_in_words = f"{self.number} in words is: {print_string}"
      
      elif 16 <= len(self.number) <= 18: 
        for x,y in dict4.items():
          if x == int(self.number[-3:]) and x !=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-6:-3]) and a !=0:
            fifth_3 = b
          elif a == 0:
            fifth_3 = ""
        for a,b in dict4.items():
          
          if a == int(self.number[-9:-6]) and a !=0:
            fourth_3 = b
          elif a == 0:
            fourth_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-12:-9]) and a !=0:
            third_3 = b
          elif a == 0:
            third_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-15:-12]) and a !=0:
            second_3 = b
          elif a == 0:
            second_3 = ""
        for a,b in dict4.items():
          if a == int(self.number[-18:-15]):
            first_3 = b
        print_dict = {first_3:"quadrilllion",
                      second_3:"trillion",
                      third_3:"billion",
                      fourth_3:"million",
                      fifth_3:"thousand",
                      last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        print_string = ', '.join(print_statement)
        number_in_words = f"{self.number} in words is: {print_string}"
    
    # the if block below declares the numeric value of decimal numbers
    # from 0.0 to 999,999,999,999,999,999.99 in words. 
    # The decimal number is truncated to 2 decimal places.
    
    elif len(number_list) == 2:
      if len(number_list[0]) == 0:
        left_part = 'zero'
      
      elif 1 <= len(number_list[0]) <= 3:
        for x,y in dict4.items():
          if x == int(number_list[0]):
            left_part = y
            
      elif 4 <= len(number_list[0]) <= 6:
        for x,y in dict4.items():
          if x == int(number_list[0][-3:]) and x !=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-6:-3]) and a!=0:
            first_3 = b
          elif a == 0:
            first_3 = ""
        print_dict = {first_3:"thousand", last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        left_part = ', '.join(print_statement)
                      
      elif 7 <= len(number_list[0]) <= 9:
        for x,y in dict4.items():
          if x == int(number_list[0][-3:]) and x!=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-6:-3]) and a!=0:
            second_3 = b
          elif a == 0:
            second_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-9:-6]) and a!=0:
            first_3 = b
          elif a == 0:
            first_3 = ""
    
        print_dict = {first_3:"milllion",
                      second_3:"thousand",
                      last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        left_part = ', '.join(print_statement)
         
      elif 10 <= len(number_list[0]) <= 12:
        for x,y in dict4.items():
          if x == int(number_list[0][-3:]) and x !=0:
            last_3 = y
          elif a == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-6:-3]) and a !=0:
            third_3 = b
          elif a == 0:
            third_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-9:-6]) and a !=0:
            second_3 = b
          elif a == 0:
            second_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-12:-9]) and a !=0:
            first_3 = b
          elif a == 0:
            first_3 = ""
    
        print_dict = {first_3:"billlion",
                      second_3:"million",
                      third_3:"thousand",
                      last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        left_part = ', '.join(print_statement)
                    
      elif 13 <= len(number_list[0]) <= 15:
        for x,y in dict4.items():
          if x == int(number_list[0][-3:]) and x !=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-6:-3]) and a !=0:
            fourth_3 = b
          elif a == 0:
            fourth_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-9:-6]) and a !=0:
            third_3 = b
          elif a == 0:
            third_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-12:-9]) and a !=0:
            second_3 = b
          elif a == 0:
            second_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-15:-12]) and a !=0:
            first_3 = b
          elif a == 0:
            first_3 = ""
    
        print_dict = {first_3:"trilllion",
                      second_3:"billion",
                      third_3:"million",
                      fourth_3:"thousand",
                      last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        left_part = ', '.join(print_statement)
 
       
      elif 16 <= len(number_list[0]) <= 18:
        for x,y in dict4.items():
          if x == int(number_list[0][-3:]) and x !=0:
            last_3 = y
          elif x == 0:
            last_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-6:-3]) and a !=0:
            fifth_3 = b
          elif a == 0:
            fifth_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-9:-6]) and a!=0:
            fourth_3 = b
          elif a == 0:
            fourth_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-12:-9]) and a!=0:
            third_3 = b
          elif a == 0:
            third_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-15:-12]) and a!=0:
            second_3 = b
          elif a == 0:
            second_3 = ""
        for a,b in dict4.items():
          if a == int(number_list[0][-18:-15]) and a!=0:
            first_3 = b
          elif a == 0:
            first_3 = ""
    
        print_dict = {first_3:"quadrilllion",
                      second_3:"trillion",
                      third_3:"billion",
                      fourth_3:"million",
                      fifth_3:"thousand",
                      last_3:""}
        print_statement = []
        for a,b in print_dict.items():
          if a != "":
            print_stats = a +" "+ b
            print_statement.append(print_stats)
        left_part = ', '.join(print_statement)
            
      if len(number_list[1]) >= 2:
        
        for a,b in ones.items():
          if a == int(number_list[1][0]):
            right_part1 = b
           
        for c,d in ones.items():
          if c == int(number_list[1][1]):
            right_part2 = d
              
        number_in_words = f"{number_list[0]}.{str(number_list[1])[0]}{str(number_list[1])[1]} in words is: {left_part} point {right_part1} {right_part2}"
          
      if len(number_list[1]) == 1:
        for a,b in ones.items():
          if a == int(number_list[1][0]):
            right_part1 = b
            
        number_in_words = f"{number_list[0]}.{str(number_list[1])[0]} in words is: {left_part} point {right_part1}"

      if len(number_list[1]) == 0:
        number_in_words = f"{self.number[:-1]} in words is: {left_part}"
        print("****************************************************")
    else:
      number_in_words = "You have either entered decimal points twice or no number at all!!"
    
    return number_in_words
