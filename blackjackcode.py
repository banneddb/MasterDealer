import random


card_choices = {"Ace" : [1,11],"Two" : 2,"Three": 3, "Four": 4,"Five" : 5,"Six" : 6,"Seven" : 7,"Eight" : 8,"Nine" : 9,"Jack" : 10,"Queen" : 10,"Kings" : 10 }
#aces = 1 or 11 (player can pick)

def black_jack(player_choice=None, start_new=False, state=None):

    messages = []

    if start_new:
        messages.append("Dealer hands you the first card...")

        card = random.choice(list(card_choices.keys()))
        player_card = card_choices[card]
        state['player_cards'].append(card)
        state['player_total'] += player_card
        messages.append(f"Your first card is {card} ({str(player_card)}).")


        if isinstance(player_card, list):
            messages.append("You've got an Ace! Is it going to be a 1 or 11... (Please reply with '1' or '11') ")
            return messages
        messages.append(f"Your total is {str(state['player_total'])}.")

        #Time to deal the card to the dealer
        dealer_card = random.choice(list(card_choices.keys()))
        dealer_card_value = card_choices[dealer_card]
        state['dealer_cards'] = [dealer_card]
        state['dealer_total'] = dealer_card_value
        messages.append("The dealer's first card is " + dealer_card + " (" + str(dealer_card_value) + ").")
        messages.append("The dealer's total is " + str(state['dealer_total']) + ".")

    #Taking care of the Ace
    elif player_choice == "1" or player_choice == "11":
        ace_value = int(player_choice)
        state['player_total'] += ace_value
        messages.append("Your total is " + str(state['player_total']) + ".")

    elif "hit" in player_choice:
        card = random.choice(list(card_choices.keys()))
        player_card = card_choices[card]
        state['player_cards'].append(card)

        if isinstance(player_card, list):
            if state['player_total'] + 11 <= 21:
                state['player_total'] += 11
            else:
                state['player_total'] += 1
        else:
            state['player_total'] += player_card

            messages.append("Your new card is " + card + " (" + str(player_card) + ").")
            messages.append("Your total is now " + str(player_total) + ".")
            if state['player_total'] > 21:
                messages.append("You went over 21! Game over. Dealer wins.")
                return messages
    elif "stay" in player_choice:
        messages.append("You chose to stay. Your total is " + str(state['player_total']) + ".")

        while state['dealer_total'] < 17:
            dealer_card = random.choice(list(card_choices.keys()))
            dealer_card_value = card_choices[dealer_card]
            state['dealer_cards'].append(dealer_card)
            state['dealer_total'] += dealer_card_value
            messages.append("Dealer draws a " + dealer_card + " (" + str(dealer_card) + ").")
            messages.append(f"Dealer's total: {str(state['dealer_total'])}")





        if state['dealer_total'] > 21:
            messages.append("The dealer busts! You win!")
        elif state['dealer_total'] > state['player_total']:
            messages.append("The dealer wins!")
        elif state['dealer_total'] < state['player_total']:
            messages.append("You win!")
        else:
            messages.append("It's a tie")
    else:
        messages.append("Invalid input. Please type 'hit' or 'stay'.")
        return messages


    return messages
