while True :
 slap = input("Slap Nikki's face? Yes or No?\n")
 slap1 = slap.lower()
 if slap1 == "yes":
  fight_run = input('"You are fucking Yulianka!\n Do you wanna "fight" or "run" ?\n')
  fight_run1 = fight_run.lower()
  if fight_run1 == "fight" :
    print ('Seriously? You dont have even a chance!You have died,\n GAME OVER.')
  elif fight_run1 == "run" :
    print("You run away like a rat. Nikki hates you.\n GAME OVER!")
 if slap1 == "no" :
   slap2 = input('"Nah, you are not a personality!" Wanna SLAP him? "Yes" or "No"\n')
   if slap2 == "Yes" :
     slap2 = slap2.lower()
     print('You are filthy mongrel! How dare you! Die bitch and rot in your swamp!') 
     print('You have died!\nGAME OVER')
   elif slap2 == "No" :
     print("nikki kills you anyway. Just because it's funny. You have died.\nGAME OVER")
 again = input("Do you want to try again? Yes or No?\n")
 again1 = again.lower()
 if again == "No" :
  break
