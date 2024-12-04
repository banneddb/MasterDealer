import random

card_choices = {"One" : 1,"Two" : 2,"Three": 3, "Four": 4,"Five" : 5,"Six" : 6,"Seven" : 7,"Eight" : 8,"Nine" : 9,"Jack" : 10,"Queen" : 10,"Kings" : 10 }
#aces = 1 or 11 (player can pick)

def black_jack(card_choices):
    player_total = 0
    dealer_total = 0
    player_card = random.choice(list(card_choices.values()))
    print(player_card)
    while player_total<21:
        if player_card in card_choices:
            player_total += player_card
            userinput = input(f'Your first card is {player_card}. Would you like to hit or stay?')
            if 'hit' in userinput:
                player_card = random.choice(list(card_choices.values()))
                player_total += player_card
            elif 'stay' in userinput:
                dealer_total += random.choice(list(card_choices.values()))

def main():
    black_jack(card_choices)



black_jack(card_choices)