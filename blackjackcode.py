import random
import time

card_choices = {"Ace" : [1,11],"Two" : 2,"Three": 3, "Four": 4,"Five" : 5,"Six" : 6,"Seven" : 7,"Eight" : 8,"Nine" : 9,"Jack" : 10,"Queen" : 10,"Kings" : 10 }
#aces = 1 or 11 (player can pick)

def black_jack():
    player_total = 0
    dealer_total = 0
    time.sleep(0.2)
    print("Dealer hands you the first card...")
    time.sleep(2)
    card = random.choice(list(card_choices.keys()))
    player_card = card_choices[card]
    print("Your first card is " + card + " (" + str(player_card) + ").")

    time.sleep(2)
    if isinstance(player_card, list):
        while True:
            user_choice = input("Do you want it as 1 or 11? ")
            user_choice = user_choice.lower()
            if user_choice == "1" or user_choice == "one":
                player_total += 1
                break
            elif user_choice == "11" or user_choice == "eleven":
                player_total += 11
                break
            else:
                print("Invalid input. Please enter the digits 1 or 11 or type 'one' or 'eleven'")

    else:
        player_total += player_card
    print("Your total is " + str(player_total) + ".")

    while player_total < 21:
        userinput = input("Would you like to hit or stay? ")
        userinput = userinput.lower()
        if "hit" in userinput:
            card = random.choice(list(card_choices.keys()))
            player_card = card_choices[card]
            time.sleep(2)
            print("You drew " + card + " (" + str(player_card) + ").")

            if isinstance(player_card, list):
                if player_total + 11 <= 21:
                    player_total += 11
                else:
                    player_total += 1
            else:
                player_total += player_card

            print("Your total is now " + str(player_total) + ".")
            if player_total > 21:
                print("You went over 21! Game over. Dealer wins.")
                return
        elif "stay" in userinput:
            break
        else:
            print("Invalid input. Please type 'hit' or 'stay'.")
    print("Dealer's turn begins...")
    time.sleep(1)
    while dealer_total < 17:
        card = random.choice(list(card_choices.keys()))
        dealer_card = card_choices[card]
        time.sleep(2)
        print("Dealer's card is " + card + " (" + str(dealer_card) + ").")
        if isinstance(dealer_card, list):
            if dealer_total + 11 <= 21:
                dealer_total += 11
            else:
                dealer_total += 1
        else:
            dealer_total += dealer_card
        time.sleep(2)
        print("Dealer's total: " + str(dealer_total))
        time.sleep(2)
    print("Your total: " + str(player_total))
    print("Dealer's total: " + str(dealer_total))


    if dealer_total > 21 or player_total > dealer_total:
        print("You win this round!!!")
    elif player_total == dealer_total:
        print("It's a tie :0")
    else:
        print("Dealer wins...")


def main():
    while True:
        black_jack()
        play_again = input("Do you want to play one more round? (yes/no) ")
        play_again = play_again.lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()