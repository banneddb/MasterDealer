import random

card_choices = {"One" : 1,"Two" : 2,"Three": 3, "Four": 4,"Five" : 5,"Six" : 6,"Seven" : 7,"Eight" : 8,"Nine" : 9,"Jack" : 10,"Queen" : 10,"Kings" : 10 }




def black_jack(card_choices, user_input: str) -> str:
    player_total = 0
    card_choices = random.shuffle(card_choices)
    userinput = user_input.lower()
    player_card = random.choice(card_choices)
    while player_total<21:
        if player_card in card_choices:
            player_total += player_card
            return f'Your first card is {player_card}. Would you like to hit or stay?'
        if 'hit' in userinput:
            player_card = random.choice(card_choices)
            player_total += player_card











"""""
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {random.randint(1,6)}'
    else:
        return random.randchocie(['I do not understand...',
                                'What are you talking about?',
                                'Do you mind rephrasing that?'])
"""""