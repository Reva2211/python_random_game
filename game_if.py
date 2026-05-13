print("----Welcome to the fun city----")
import random
while True:
    print("\nEvents\n")
    print("1.guessing a number")
    print("2.dice game")
    print("3.head or tail")
    print("4.UNO card")
    print("5.card game")
    print("6.lucky draw")
    print("7.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        number=int(input("enter your number(1 to 9):"))
        guess=random.randint(1,9)
        if guess==number:
            print("Congrats!You have guessed the correct number")
        else:
            print("Unfortunately.You have not guessed the correct number")
    elif choice==2:
        dice_game=int(input("enter your number(1 to 6):"))
        dice=random.randint(1,6)
        if dice==dice_game:
            print("Congrats!You have guessed the correct number")
        else:
            print("Unfortunately.You have not guessed the correct number")
    elif choice==3:
        coin=["head","tail"]
        coin_random=random.choice(coin)
        if coin_random=="head":
            print("you won a head")
        else:
            print("you lost a tail")
    elif choice==4:
        colors=["red","green","blue","yellow"]
        special=["reverse","+2","+4","no play"]
        numbers=[0,1,2,3,4,5,6,7,8,9]
        color=random.choice(colors)
        card_type=random.choice(["special","numbers"])
        if card_type=="numbers":
            card_type=random.choice(numbers)
        else:
            card_type=random.choice(special)
        print("Your card is",card_type)
        print(color,card_type)
    elif choice==5:
        symbol=["spade","clover","heart","diamond"]
        numbers=[0,1,2,3,4,5,6,7,8,9]
        special=["king","jack","queen"]
        symbol_random=random.choice(symbol)
        card_type=random.choice(["numbers","special"])
        if card_type=="numbers":
            card_type=random.choice(numbers)
        else:
            card_type=random.choice(special)
        print("Your card is",card_type)
        print(symbol_random,card_type)
    elif choice==6:
        draw=["free food","offer","no gift","loss"]
        draw_random=random.choice(draw)
        print("Your card is",draw_random)
    else:
        print("Have a good day")
