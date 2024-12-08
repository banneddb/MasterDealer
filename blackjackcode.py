import random


card_choices = {"Ace" : [1,11],"Two" : 2,"Three": 3, "Four": 4,"Five" : 5,"Six" : 6,"Seven" : 7,"Eight" : 8,"Nine" : 9,"Jack" : 10,"Queen" : 10,"Kings" : 10 }
#aces = 1 or 11 (player can pick)

def black_jack(player_choice: str = None):
    player_total = 0
    dealer_total = 0
    messages = []


    messages.append("Dealer hands you the first card...")
    print(messages)
    card = random.choice(list(card_choices.keys()))
    player_card = card_choices[card]
    messages.append(f"Your first card is {card} ({str(player_card)}).")
    print(messages)

    if isinstance(player_card, list):
            if player_choice and player_choice in ["1","11"]:
                player_total += int(player_choice)
            else:
                messages.append("You've got an Ace! Is it going to be a 1 or 11... (Please reply with '1' or '11') ")
                print(messages)
                return messages


    else:
        player_total += player_card
    messages.append(f"Your total is {str(player_total)}.")
    print(messages)

    while player_total < 21:
        if not player_choice:
            messages.append("Would you like to hit or stay? (Reply 'hit' or 'stay')")
            return messages
        elif "hit" in player_choice:
            card = random.choice(list(card_choices.keys()))
            player_card = card_choices[card]

            messages.append(f"You drew{card}({str(player_card)}).")

            if isinstance(player_card, list):
                if player_choice and player_choice in ["1", "11"]:
                    player_total += int(player_choice)
                else:
                    messages.append("You've got an Ace! Is it going to be a 1 or 11... (Please reply with '1' or '11') ")
                    return messages

            messages.append("Your total is now " + str(player_total) + ".")
            if player_total > 21:
                messages.append("You went over 21! Game over. Dealer wins.")
                return messages
        elif "stay" in player_choice:
            break
        else:
            messages.append("Invalid input. Please type 'hit' or 'stay'.")
            return messages
    messages.append("Dealer's turn begins.")

    while dealer_total < 17:
        card = random.choice(list(card_choices.keys()))
        dealer_card = card_choices[card]

        messages.append("Dealer's card is " + card + " (" + str(dealer_card) + ").")
        if isinstance(dealer_card, list):
            if dealer_total + 11 <= 21:
                dealer_total += 11
            else:
                dealer_total += 1
        else:
            dealer_total += dealer_card

        messages.append(f"Dealer's total: {str(dealer_total)}")


    messages.append("Your total: " + str(player_total))
    messages.append("Dealer's total: " + str(dealer_total))


    if dealer_total > 21 or player_total > dealer_total:
        messages.append("You win this round!!!")
    elif player_total == dealer_total:
        messages.append("It's a tie.")
    else:
        messages.append("Game Over. Dealer wins...")

    return messages

black_jack()