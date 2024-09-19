import random


# make a deck shuffles function that will deal 2 cards then ask the user to hit or pass and depending on users choice - use a point value dictionary to access - dealer always hits if any of the hands go above 21 then its a bust. For ace ask 1 or 11 before appending to a list

# Optional - Maybe a difficulty thing and maybe more text based instead of lists


# addition function for lists

def lstadd(lst):
    returnaddition = 0
    for i in range(0, len(lst)):
        returnaddition += lst[i]
    return returnaddition


# converts lists to texts

def lsttotext(lst):
    returntext = ""
    for i in range(len(lst)):
        returntext += str(lst[i])
        if i != (len(lst) - 1):
            returntext += ", "
    return returntext


# deckgenerator

def deckgen():
    cardfaces = ["Ace", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    returndeck = []

    for i in range(0, 13):
        for j in range(0, 4):
            returndeck.append(cardfaces[i])

    return returndeck


# deckshuffles

deck = deckgen()


def swap(lst, x, y):
    temp = deck[x]
    deck[x] = deck[y]
    deck[y] = temp


def deckshuffles(x):
    for i in range(x):
        pos1 = random.randint(0, 51)
        pos2 = random.randint(0, 51)

        swap(deck, pos1, pos2)


deckshuffles(500)

# pointvaluedictionary


pointvaluedictionary = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,

}

# main variables

deckplaceholder = 3
playerpoints = []
computerpoints = []
hand = []
dealerhand = []
playerpass = 0
computerpass = 0

# begin dealing 2 cards and getting point value

hand.append(deck[0])
hand.append(deck[2])

print("\nThis is your hand: ", lsttotext(hand))

for i in range(len(hand)):
    if (hand[i] == "Ace"):
        acepoint = int(input(("You have a ace - would you like it to be 1 or 11: ")))
        playerpoints.append(acepoint)
    else:
        playerpoints.append(pointvaluedictionary[hand[i]])

if (lstadd(playerpoints) == 21):
    print("You Win - Good Job")
    quit()

dealerhand.append(deck[1])
dealerhand.append(deck[3])

for i in range(len(dealerhand)):
    if (dealerhand[i] == "Ace"):
        if (lstadd(computerpoints) + 11) <= 21:
            computerpoints.append(11)
        else:
            computerpoints.append(1)

    else:
        computerpoints.append(pointvaluedictionary[dealerhand[i]])

print("\nYou have: ", lstadd(playerpoints), "Points")

print("\nThis is the Dealer's Hand: ", lsttotext(dealerhand))

print("\nDealer has: ", lstadd(computerpoints), "Points")

if (lstadd(computerpoints) == 21):
    print("Tough Game - Dealer won")
    quit()

# Main loop

while True:

    deckplaceholder += 1

    usercardchoice = input("\nWould you like to Hit(H) or Pass(P): ")
    if usercardchoice == "H" or usercardchoice == "h" or usercardchoice == "Hit" or usercardchoice == "hit":

        hand.append(deck[deckplaceholder])
        print("\nYou currently have: ", lsttotext(hand), "- cards in your hand")

        if (hand[-1] == "Ace"):
            acepoint = int(input(("You have a ace - would you like it to be 1 or 11: ")))
            playerpoints.append(acepoint)
            pass

        else:
            playerpoints.append(pointvaluedictionary[hand[-1]])

        print("\nYou currently have: ", lstadd(playerpoints), "Points")

        if (lstadd(playerpoints) == 21):
            print("You win - Good Job")
            quit()

        if (lstadd(playerpoints) > 21):
            print("Tough Luck - You bust")
            quit()

    else:
        playerpass += 1
        pass

    deckplaceholder += 1

    # dealer turn

    if (lstadd(computerpoints) < 17):

        dealerhand.append(deck[deckplaceholder])

        if (dealerhand[-1] == "Ace"):
            if (lstadd(computerpoints) + 11) < 21:
                computerpoints.append(11)
            else:
                computerpoints.append(1)
        else:
            computerpoints.append(pointvaluedictionary[dealerhand[-1]])

    else:

        if (lstadd(computerpoints) >= 17):
            passchoice = random.randint(1, 5)
            if passchoice == 1:

                dealerhand.append(deck[deckplaceholder])

                if (dealerhand[-1] == "Ace"):
                    if (lstadd(computerpoints) + 11) < 21:
                        computerpoints.append(11)
                    else:
                        computerpoints.append(1)

                else:
                    computerpoints.append(pointvaluedictionary[dealerhand[-1]])
                    computerpass += 1

        if playerpass == 3 or playerpass == 4 and computerpass == 3 or computerpass == 4:
            print("Both you and the dealer passed 3 times")

            if (lstadd(computerpoints) > lstadd(playerpoints)):
                print("\nTough Luck ", lstadd(computerpoints), ">", lstadd(playerpoints),
                      "- Dealer won - due to higher points")

            elif (lstadd(playerpoints) > lstadd(computerpoints)):
                print("You won ", lstadd(playerpoints), ">", lstadd(computerpoints), " - due to higher points")
            else:
                print("Tie")

            break

    print("\nDealer currently has: ", lsttotext(dealerhand), "- cards in his hand")
    print("\nDealer currently has: ", lstadd(computerpoints), "Points")

    if (lstadd(computerpoints) == 21):
        print("Tough luck - Dealer Won")
        quit()

    if (lstadd(computerpoints) > 21):
        print("You Win - Dealer busts")
        quit()