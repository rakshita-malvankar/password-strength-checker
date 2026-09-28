#import string
while True:
    password=input("Enter your Password:")
    score=0
    if len(password)>=8:
     score+=1
    if any(char.isupper()for char in password):
      score+=1
    if any(char.islower()for char in password):
       score+=1
    if any(char.isdigit()for char in password):
     score+=1
    special_characters="!@#$%^&*()-_=+[]{};:,.?/"
    if any(char in special_characters for char in password):
      score+=1
    if score==5:
       print("Password Strength:Strong")
       print("password accepted")
       break
    else:
          print("password is not strong")
          print("enter a strong password")
          print()