# Blackjack Game (Text-Based)

A simple text-based Blackjack game where you compete against a dealer. The goal is to have a hand value as close to 21 as possible without exceeding it. If either you or the dealer busts (exceeds 21), that player loses. 

## Features

- **Card Deck**: A deck is generated with standard playing cards. Each card is assigned a point value.
- **Ace Handling**: When an Ace is dealt, the player can choose if it should be counted as 1 or 11.
- **Player Actions**: The player can choose to "Hit" (get another card) or "Pass" (end their turn).
- **Dealer Behavior**: The dealer automatically "hits" if their points are below 17. The game ends if either the player or dealer busts.
- **Winning Conditions**: The player wins by achieving a hand value of 21 or by having a higher point value than the dealer without busting.

## How to Play

1. The game begins with 2 cards dealt to both the player and the dealer.
2. On your turn, you can choose to "Hit" or "Pass". If you "Hit", you get another card, and if you choose Ace, you decide whether it should be 1 or 11.
3. If your total points exceed 21, you bust and lose.
4. The dealer plays according to the rules, hitting until their points are 17 or more.
5. If the dealer busts, you win. If you have higher points than the dealer without busting, you win. If the dealer has higher points, they win.

## Code Overview

### 1. `lstadd(lst)`
This function calculates the sum of points in a list of cards.

### 2. `lsttotext(lst)`
Converts a list of cards into a string format to display the player's or dealer's hand.

### 3. `deckgen()`
Generates a shuffled deck of 52 cards, each card having one of the following faces: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.

### 4. `deckshuffles(x)`
Shuffles the deck `x` times for randomness.

### 5. `pointvaluedictionary`
Maps each card (Ace, 2-10, Jack, Queen, King) to its corresponding point value.

### 6. `main()`
Contains the core logic for the Blackjack game:
- Deals cards to the player and dealer.
- Prompts the player to choose "Hit" or "Pass".
- The dealer automatically plays based on certain rules.
- Determines the winner based on the final hand values.

## Running the Game

1. Clone or download this repository to your local machine.
2. Run the script using a Python interpreter.


## Additional Notes

- **Ace Handling**: You can choose whether the Ace is counted as 1 or 11 when drawn.
- **Player Actions**: The player can choose "Hit" to receive another card or "Pass" to end their turn.

