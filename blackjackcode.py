import random

card_choices = {"Ace" : [1,11],"Two" : 2,"Three": 3, "Four": 4,"Five" : 5,"Six" : 6,"Seven" : 7,"Eight" : 8,"Nine" : 9,"Jack" : 10,"Queen" : 10,"Kings" : 10 }
#aces = 1 or 11 (player can pick)

def black_jack():
    player_total = 0
    dealer_total = 0

    card = random.choice(list(card_choices.keys()))
    player_card = card_choices[card]
    print("Your first card is " + card + " (" + str(player_card) + ").")


    if isinstance(player_card, list):
        player_total += max(player_card)
    else:
        player_total += player_card
    print("Your total is " + str(player_total) + ".")

    while player_total < 21:
        userinput = input("Would you like to hit or stay? ").lower
        if 'hit' in userinput:
            card = random.choice(list(card_choices.keys()))
            player_card = card_choices[card]
            print("You drew " + card + " (" + str(player_card) + ").")

            if isinstance(player_card, list):
                if player_total + 11 <= 21:
                    player_total += 11
                else:
                    player_total += 1
            else:
                player_total += player_card

            print("Your total is now " + str(player_total) + ".")
        elif "stay" in userinput:
            break

    while dealer_total < 17:
        card = random.choice(list())


def main():
    black_jack(card_choices)
main()



black_jack(card_choices)