should_continue = True
first_move = True
game_run = True
my_card_sum = 0
com_card_sum = 0
my_card = []
computer_card = []

def add_card(drwn_card, my_card, computer_card):
    global my_card_sum
    global com_card_sum
    global should_continue
    from deck import cards
    import random
    my_card += random.sample(cards,drwn_card)
    computer_card += random.sample(cards,drwn_card)
    
    # resolve ace problem

    my_card_sum = sum(my_card)
    if my_card_sum > 21:
            if my_card.count(11)==0:
                should_continue = False
            else:
                my_card_sum -= 10
                pos = my_card.index(11)
                my_card[pos] = 1


    com_card_sum = sum(computer_card)
    if com_card_sum > 21:
            if computer_card.count(11)==0:
                should_continue = False
            else:
                com_card_sum -= 10
                pos = computer_card.index(11)
                computer_card[pos] = 1
            


# game starts from here
from art import logo
print(logo)


while game_run:
    
    my_card_sum = 0
    com_card_sum = 0
    my_card = []
    computer_card = []

    game_start = input("Do you want to play a game of balckjake? Type 'y' or 'n': ").lower()
    if game_start=="y":
        should_continue = True
        first_move = True
        import os
        clear = lambda: os.system('cls')
        clear()
        print(logo)
    else:
        should_continue = False
        game_run = False
        print("Good Byee..!! 😎")

    while should_continue:

        if first_move:
            first_move = False
            add_card(2, my_card, computer_card)

        print(f"Your cards: {my_card}, current score: {my_card_sum}")
        print(f"computer's first card: {computer_card[0]}")
        user = input("Type 'y' to get another card, or type 'n' to pass: ").lower()
        if user=="y":
            my_card_sum = 0
            com_card_sum = 0
            add_card(1, my_card, computer_card)
            if not should_continue:
                print(f"your final hand: {my_card}, final score: {my_card_sum}")
                print(f"computer's final hand: {computer_card}, final score: {com_card_sum}")
                if my_card_sum > 21 and com_card_sum > 21:
                    print("Both loose..!! 😤")
                elif my_card_sum > 21:
                    print("you went over/Bust 😭")
                    print("you loose..!! 😤")
                elif com_card_sum > 21:
                    print("delear went over/Bust 😤")
                    print("you win..!! 😃")

        else:
            should_continue = False
            print(f"your final hand: {my_card}, final score: {my_card_sum}")
            print(f"computer's final hand: {computer_card}, final score: {com_card_sum}")
            if com_card_sum > 21:
                print("delear went over/Bust 😤")
                print("you win..!! 😃")
            elif my_card_sum > com_card_sum and my_card_sum <= 21:
                print("you win..!! 😃")
            elif my_card_sum==com_card_sum:
                print("match draw 🙃")
            else:
                print("you loose..!! 😤")



    

