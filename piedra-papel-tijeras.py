import random

def chooseOptions():
    options = ("Piedra", "Papel", "Tijera")
    user = input("Elige: Piedra, Papel o Tijera =>")
    user = user.capitalize()
    userComp = random.choice(options)

    print('User eligio =>', user)
    print('userComp eligio =>', userComp)
    return user, userComp

def rules(user, userComp, userWins, compWins):
    if user != "Piedra" and user != "Papel" and user != "Tijera":
        print("Digita un valor correcto")
    elif user == userComp:
        print("Esto fue un empate")
    elif user == "Piedra" and userComp == "Tijera":
        print(f"Ganaste! {user} le gana a {userComp}")
        userWins += 1
    elif user == "Papel" and userComp == "Piedra":
        print(f"Ganaste! {user} le gana a {userComp}")
        userWins += 1
    elif user == "Tijera" and userComp == "Papel":
        print(f"Ganaste! {user} le gana a {userComp}")
        userWins += 1     
    else:
        print(f"Perdiste {userComp} le gana a {user}")
        compWins += 1        
    return userWins, compWins

def checkWinner(userWins, compWins):
    if userWins == 3:
        print('+' * 15)
        print('La batalla ha terminado! El USUARIO ha GANADO🎉🎉🎉!')            
        
    if compWins == 3:
        print('+' * 15)
        print('La batalla ha terminado! La COMPUTADORA ha GANADO!🎉🎉🎉')
    return userWins, compWins,

def runGame():
    userWins = 0
    compWins = 0
    rounds = 1   
    
    while True:    
        print('*' * 15)
        print('ROUND', rounds)
        print('*' * 15)
        
        print("user_wins", userWins)
        print("cumputer_wins", compWins) 
        rounds += 1               
       
        user, userComp = chooseOptions()
        userWins, compWins = rules(user, userComp, userWins, compWins)        
        userWins, compWins = checkWinner(userWins, compWins)

        if userWins == 3 or compWins == 3:
            break        
runGame()