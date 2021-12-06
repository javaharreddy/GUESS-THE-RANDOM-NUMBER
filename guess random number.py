import random
def guess_the_random_number():
      a=random.randint(1,6)
      score=100
      print("hey there guess the number iam trying to think in the range of 1 to 6")
      print("i will give you hints")
      print("you will loose score for each clue you get")
      print("no score will be deducted for the first clue maximum score is 100")
      print("if you  get it right for the first clue you will get score = 100")
      print("if you  get it right for the second clue you will get score = 70")
      print("if you  get it right for the third clue you will get score = 40")
      print("if you  get it right for the first clue you will get score = 25")
      clue1=str()
      clue2=str()
      clue3=str()
      clue4=str()
      guessednumber=int()
      global response1
      response1=int()
      if(a==1):
        clue2="this is neither composite nor prime"
        clue3="this number is first natural number"
        clue4="this is the first odd number "
        clue1="this number is the multiplicative identity"
      if(a==2):
        clue1="in october month on this day gandhi is born"
        clue2="this is the first even number"
        clue3="it is the only even prime number"
        clue4="this is the first prime number"
      if(a==3):
        clue1="this is the number of harmony and wisdom"
        clue2="it is a perfect number"
        clue3="this is the second odd number"
        clue4="this is the second prime number"
      if(a==4):
        clue1="this number is considered to be positive reflection of the sun"
        clue4="this number is the second even number "
        clue3="it is twice the number of first prime number"
        clue2="it is the adding of one to the second odd number"
      if(a==5):
        clue2=" a natural number greater than 1 that is not a product of two smaller natural numbers"
        clue3="second largest number in the dice"
        clue1="this number is the atomic number of the boron element"
        clue4="this number is the half of the number 10"
      if(a==6):
        clue1="the smallest positive integer which is neither a square number nor a prime number"
        clue2="second smallest composite number"
        clue4="twice the number of second odd number"
        clue3="this is the largest number in the dice"
      global response
      response=int()
      def takeresponse():
            global response
            response=int(input("ok are you ready? if yes enter 1 else 0 "))
      takeresponse()
      while(response==0):
          takeresponse()
      def clue1take():
         global response
         print("here we go with the first clue\n"+clue1)
         response=int(input("ok did you understand the clue?if yes enter 1 else 0 "))
      clue1take()
      while(response==0):
            clue1take()
      guessednumber=int(input("enter the guessed number "))
      if(guessednumber==a):
         print("yes you guessed it right")
         print("score = "+str(score))
      else:
          print("you guessed it wrong")
          def clue2take():
              global response
              print("here we go with the second clue\n" + clue2)
              response = int(input("ok did you understand the clue?if yes enter 1 else 0 "))
          clue2take()
          while (response == 0):
               clue2take()
          guessednumber = int(input("enter the guessed number now "))
          if(guessednumber==a):
                print("yes you got it right now")
                print("score = "+str(score-30))
          else:
                print("you guessed it wrong agian")
                def clue3take():
                    global response
                    print("here we go with the third clue\n" + clue3)
                    response = int(input("ok did you understand the clue?if yes enter 1 else 0 "))
                clue3take()
                while (response == 0):
                       clue3take()
                guessednumber = int(input("enter the guessed number now "))
                if (guessednumber == a):
                      print("yes you got it right now")
                      print("score = "+str(score-60))
                else:
                      print("you guessed it wrong agian")
                      def clue4take():
                           global response
                           print("here we go with the fourth clue\n" + clue4)
                           response = int(input("ok did you understand the clue?if yes enter 1 else 0 "))
                      clue4take()
                      while (response == 0):
                               clue4take()
                      guessednumber = int(input("enter the guessed number now "))
                      if (guessednumber == a):
                             print("yes you got it right now")
                             print("score = "+str(score-75))
                      else:
                             print("sorry you  got it wrong all time ")
                             print("score = 0")
                             response1=int(input("do you want guess right now? if yes enter 1 else enter 0 "))
guess_the_random_number()
while(response1==1):
    guess_the_random_number()
