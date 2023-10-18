from time import sleep
print('''
                   _..-------++._
               _.-'/ |      _||  \"--._
         __.--'`._/_\j_____/_||___\    `----.
    _.--'_____    |          \     _____    /
  _j    /,---.\   |        =o |   /,---.\   |_
 [__]==// .-. \\==`===========/==// .-. \\=[__]
   `-._|\ `-' /|___\_________/___|\ `-' /|_.'
         `---'                     `---'
''')
print("Welcome to Extreme Ultimate Racing Showdown Extraordinaire 9000")
print("Your mission is simple, make it to the finish line.") 
sleep(2)

name = input("What's your name? ")
sleep(2)

print(f"Okay {name}, it's time to race.")
sleep(2)

print("You feel sweat roll down your face as the lights slowly go from red, to yellow, ...")
sleep(2)

print("then green!")
sleep(2)

print("You quickly notice there's a path up high around the first bank, or down low, which do you take?")
sleep(2)
gate1 = input("High or Low? ").lower()

if gate1 == "low":
  print("You expertly maneuver down low around Jeff and move into 3rd place.")
  sleep(2)
  
  print("You have to decide whether mashing the gas or hitting the brakes is the best way to react to the driver next to you.")
  sleep(2)
  
  gate2 = input("Gas or Brake? ").lower()
  if gate2 == "gas":
    print("You gun it, narrowly avoiding the idiot next to you who started to spin out.")
    sleep(2)
    
    print("You take his place, and are now in 2nd.")
    sleep(2)
    
    print("Well done! You're on the final stretch!")
    sleep(2)
    
    print("You are battling with 1st place, taking turns moving down low or up high around each corner.")
    sleep(2)
    
    print("On the final lap you must decide between being aggressive, defensive, or taking a risk.")
    sleep(2)
    
    gate3 = input("Which will it be? Aggressive, Defensive, or Risky? ").lower()
    if gate3 == "risky":
      print("You take just enough risk to move ahead of Ted, an amateur driver.")
      sleep(2)
      
      print("You cross the finish, seeing Ted spun out in the grass in your rear-view mirror.")
      sleep(2)
      
      print("You win! Here's a cookie, bucko.")
      
    elif gate3 == "aggressive":
      print("You overtake into 1st! But something is wrong... your engine is making an awful noise.")
      sleep(2)
      
      print("You recall your crew chief telling you to take it easy on the straights because your oil is over-temping.")
      sleep(2)
      
      print("Looks like you screwed the pooch, bucko.")
      sleep(2)
      
      print("If you ain't first, you're last, bucko.")
      
    elif gate3 == "defensive":
      print("Now is not the time to back off!")
      sleep(2)
      
      print("If you ain't first, you're last, bucko.")
      
    else:
      print("You either can't spell, or you think you have another option.")
      sleep(2)
      
      print("You waste enough time to let the other guy ahead of you.")
      sleep(2)
      
      print("If you ain't first, you're last, bucko.")
      
  elif gate2 == "brake":
    print("You hit the brakes way too hard, so the guy behind you rams you and you lose control into the wall.")
    
    sleep(2)
    print("Game Over, bucko.")
    
  else:
    print("Come on, it's one or the other.")
    sleep(2)
    
    print("After forgetting which pedal does what, you are passed by 6 cars.")
    
    sleep(2)
    print("Game Over, bucko.")

elif gate1 == "high":
  print("What a fool! You didn't realize how fast you were going into the corner?! You hit the wall!")
  sleep(2)
  
  print("Game Over, bucko.")
  
else:
  print("Directions are hard, I know.")
  sleep(2)

  print("You drop to the back of the pack because you can't remember which way is left or right.")
  sleep(2)

  print("Game Over, bucko.")