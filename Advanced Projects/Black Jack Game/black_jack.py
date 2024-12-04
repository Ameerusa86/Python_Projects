import random

# Function to create and shuffle a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card['rank'] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card['rank'] == 'Ace':
            num_aces += 1
            value += 11
        else:
            value += int(card['rank'])
    
    # Adjust the value for aces if necessary
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    
    return value

# Function to display the player's hand
def display_hand(hand, hide_first_card=False):
    print("Your hand:")
    for i, card in enumerate(hand):
        if i == 0 and hide_first_card:
            print("[Hidden]")
        else:
            print(f"{card['rank']} of {card['suit']}")

# Function to play the dealer's turn
def play_dealer_turn(deck, dealer_hand):
    print("\nDealer's turn:")
    display_hand(dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand)
    return dealer_hand

# Function to check who wins
def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if player_value > 21:
        return "You bust! Dealer wins."
    elif dealer_value > 21:
        return "Dealer busts! You win."
    elif player_value == dealer_value:
        return "It's a tie!"
    elif player_value > dealer_value:
        return "You win!"
    else:
        return "Dealer wins."

# Main function to play the game
def blackjack():
    print("Welcome to Blackjack!\n")
    
    # Initialize deck and hands
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    # Display initial hands
    print("Dealer's hand:")
    print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
    print("[Hidden]")
    display_hand(player_hand)
    
    # Player's turn
    while True:
        choice = input("\nDo you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            display_hand(player_hand)
            if calculate_hand_value(player_hand) > 21:
                print("You bust!")
                return
        elif choice == 's':
            break
        else:
            print("Invalid choice! Please enter 'h' or 's'.")
    
    # Dealer's turn
    dealer_hand = play_dealer_turn(deck, dealer_hand)
    
    # Determine winner
    print("\n" + determine_winner(player_hand, dealer_hand))

# Start the game
blackjack()
