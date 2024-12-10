import random


card_choices = {"Ace" : [1,11],"Two" : 2,"Three": 3, "Four": 4,"Five" : 5,"Six" : 6,"Seven" : 7,"Eight" : 8,"Nine" : 9,"Jack" : 10,"Queen" : 10,"King" : 10 }
classes= ["♣️", "♦️", "♠️", "♥️"]
#aces = 1 or 11 (player can pick)

def black_jack(player_choice: str = None, start_new: bool = False, state: dict = None):

    messages = []

    if start_new:
        #The first card of the player
        messages.append("Dealer hands you the first card...")
        card = random.choice(list(card_choices.keys()))
        cardClass = random.choice(classes)
        player_card = card_choices[card]
        state['player_cards'].append(card)
        state['player_total'] += player_card
        messages.append(f"Your first card is {card} {cardClass} ({str(player_card)}).")

        #Player pulls an ace
        if isinstance(player_card, list):
            cardClass = random.choice(classes)
            messages.append(f"You've got an Ace {cardClass}! Is it going to be a 1 or 11... (Please reply with '1' or '11') ")
            return messages
        messages.append(f"Your total is {str(state['player_total'])}.")

        #The first card of the dealer
        dealer_card = random.choice(list(card_choices.keys()))
        cardClass = random.choice(classes)
        dealer_card_value = card_choices[dealer_card]
        state['dealer_cards'] = [dealer_card]
        state['dealer_total'] = dealer_card_value


        #Dealer pulls an ace. Depending on his total, he either plays it as a 1 or an 11.
        if isinstance(dealer_card_value, list):
            if 11 <= 21:
                state['dealer_total'] = 11
            else:
                state['dealer_total'] = 1
        else:
            state['dealer_total'] = dealer_card_value
        cardClass = random.choice(classes)
        messages.append(f"The dealer's first card is {dealer_card} {cardClass} {str(dealer_card_value)}.")
        messages.append(f"The dealer's total is {str(state['dealer_total'])}.")
        messages.append("Turn is over. Are you hitting or staying? (reply with 'hit' or 'stay')")

    #Taking care of the Ace
    elif player_choice == "1" or player_choice == "11":
        ace_value = int(player_choice)
        state['player_total'] += ace_value
        messages.append(f"Your total is {str(state['player_total'])}.")
        messages.append("Turn is over. Are you hitting or staying? (reply with 'hit' or 'stay')")

    elif "hit" in player_choice:
        card = random.choice(list(card_choices.keys()))
        cardClass = random.choice(classes)
        player_card = card_choices[card]
        state['player_cards'].append(card)

        if isinstance(player_card, list):
            if state['player_total'] + 11 <= 21:
                state['player_total'] += 11
            else:
                state['player_total'] += 1
        else:
            state['player_total'] += player_card
            messages.append(f"Your new card is {card} {cardClass} {str(player_card)}.")
            messages.append(f"Your total is now {str(state['player_total'])}.")
            if state['player_total'] > 21:
                messages.append("You went over 21! Game over. Dealer wins.")
                return messages
        messages.append("Turn is over. Are you hitting or staying? (reply with 'hit' or 'stay')")
    elif "stay" in player_choice:
        messages.append(f"You chose to stay. Your total is {str(state['player_total'])}.")
        while state['dealer_total'] < 17:
            dealer_card = random.choice(list(card_choices.keys()))
            cardClass = random.choice(classes)
            dealer_card_value = card_choices[dealer_card]
            state['dealer_cards'].append(dealer_card)
            state['dealer_total'] += dealer_card_value
            messages.append(f"Dealer draws a {dealer_card} {cardClass} {str(dealer_card)}.")
            messages.append(f"Dealer's total: {str(state['dealer_total'])}")


        if state['dealer_total'] > 21:
            messages.append("The dealer busts! You win!")
        elif state['dealer_total'] > state['player_total']:
            messages.append("The dealer wins!")
        elif state['dealer_total'] < state['player_total']:
            messages.append("You win!")
        else:
            messages.append("It's a tie")
        return messages
    else:
        messages.append("Invalid input. Please type 'hit' or 'stay'.")
        return messages


    return messages

