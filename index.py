"""
Simplified Blackjack Game.
"""
import sys
from game_objects import Deck, Player
from bet_exception import BetException


def take_bet(user):
    """Asks user for a bet."""
    while True:
        try:
            user.chips.set_bet(ask_int(f'{user.name}, place your bet: '))
        except BetException as bet_exception:
            print(bet_exception)
            continue
        else:
            break


def hit_or_stand(users_deck, users_hand, users_name):
    """Asks user to decide hit or stand."""
    player_decision = ask_int(f'{users_name}, Hit (1) or Stand (0): ', (0, 1))
    if player_decision == 1:
        users_hand.add_card(users_deck.pop(0))
        print(f'{users_name} has got new card "{users_hand.cards[-1]}":'
              f' {users_hand.value} points total.')

    return player_decision


def show_some(players, dealer):
    """Show cards and left one dealer's card hidden."""
    for player in players:
        print(
            f'{player.name} cards: {", ".join(str(card) for card in player.hand.cards)} - '
            f'{player.hand.value} points.')

    print(f'{dealer.name} cards: {dealer.hand.cards[0]}, [hidden]')


def show_all(players, dealer):
    """Show all cards."""
    for player in players:
        print(
            f'{player.name} cards: {", ".join(str(card) for card in player.hand.cards)} - '
            f'{player.hand.value} points.')

    print(f'{dealer.name} cards: {", ".join(str(card) for card in dealer.hand.cards)} - '
          f'{dealer.hand.value} points.')


def player_busts(player):
    """Proceed player busts' scenario."""
    player.chips.lose_bet()
    print(f'{player.name}, you are busted with {player.hand.value} points.')
    print(f'- {player.chips.bet} chips points. {player.chips.total} chips points total.')


def player_wins(player):
    """Proceed player wins' scenario."""
    player.chips.win_bet()
    print(f'Congratulations! {player.name} wins the game with {player.hand.value} points!')
    print(f'+ {player.chips.bet} chips points. {player.chips.total} chips points total.')


def dealer_busts(dealer):
    """Proceed dealer busts' scenario."""
    print(f'{dealer.name} is busted with {dealer.hand.value} points.')


def dealer_wins(dealer):
    """Proceed dealer wins' scenario."""
    print(f'{dealer.name} wins the game with {dealer.hand.value} points!')


def push():
    """Show message of a push."""
    print("It's a push.")


def ask_int(message='Please, write an integer number: ', int_range=(0, sys.maxsize)):
    """Ask user to input an integer."""
    while True:
        try:
            users_input = int(input(message))
            if users_input < int_range[0] or users_input > int_range[1]:
                raise ValueError
        except ValueError:
            print('Wrong value! Please, try again.')
            continue
        else:
            break

    return users_input


def replay():
    """Ask user to replay a game."""
    return ask_int('\nDo you want to play again? Yes (1) or No (0): ', (0, 1))


def play_game():
    """Main game logic."""
    while True:
        print('Welcome to BlackJack game!\n')

        players = [Player(input('What is player name? '))]
        dealer = Player('Dealer')

        take_bet(players[0])

        deck = Deck()

        for _ in range(0, 2):
            for player in players:
                player.hand.add_card(deck.deal())
            dealer.hand.add_card(deck.deal())

        show_some(players, dealer)

        playing = True
        while playing:

            if players[0].hand.value == players[0].hand.win_value:
                break

            playing = hit_or_stand(deck.deck, players[0].hand, players[0].name)

            if players[0].hand.value > players[0].hand.win_value:
                player_busts(players[0])
                break

        while dealer.hand.value < 17:
            dealer.hand.add_card(deck.deal())

        show_all(players, dealer)

        if players[0].hand.win_value >= players[0].hand.value > dealer.hand.value:
            player_wins(players[0])
            dealer_busts(dealer)
        elif (dealer.hand.win_value >= dealer.hand.value > players[0].hand.value) or \
                dealer.hand.value == dealer.hand.win_value:
            dealer_wins(dealer)
            player_busts(players[0])
        else:
            push()

        if replay():
            play_game()
            break
        else:
            break


play_game()
