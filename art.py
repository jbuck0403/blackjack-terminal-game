import sys, io

def cardArt(cards, dealer = False, dealerReveal = False, playerName = "PLAYER"):
    """
    Displays all cards in cards list

    Checks if special characters can be printed, if not it prints letters representing them
    """
    suitsPictures = ["♥", "♦", "♣", "♠"]
    suitsLetters = ["H", "D", "C", "S"]
    exceptPicture = "$"
    suitsPicture = suitsPictures[1]
    playerOrDealer = playerName if not dealer else 'DEALER'
    header = f"{suitsPicture} === {playerOrDealer} === {suitsPicture}"
    exceptHeader = f"{exceptPicture} === {playerOrDealer} === {exceptPicture}"

    def cardArtException():
        try:
            print(header)
        except UnicodeEncodeError:
            print(exceptHeader)
            return suitsLetters
        return suitsPictures

    def letterToSuit(card):
        card = list(card)
    
        if len(card) == 2:
            if card[1] == "h":
                return suits[0]
            elif card[1] == "d":
                return suits[1]
            elif card[1] == "c":
                return suits[2]
            elif card[1] == "s":
                return suits[3]
        else:
            if card[2] == "h":
                return suits[0]
            elif card[2] == "d":
                return suits[1]
            elif card[2] == "c":
                return suits[2]
            elif card[2] == "s":
                return suits[3]
            
    suits = cardArtException()
    card_height = 6

    for i in range(card_height):
        row = ""
        for index, card in enumerate(cards):
            if dealer and index == 0 and not dealerReveal:
                if i == 0:
                    row += " _______ "
                elif i == 1:
                    row += "|       |"
                elif i == 2:
                    row += "|       |"
                elif i == 3:
                    row += "|       |"
                elif i == 4:
                    row += "|       |"
                elif i == 5:
                    row += "|_______|"
            else:
                if len(card) == 2:
                    number = card[0]
                    space = " "
                else:
                    number = card[0] + card[1]
                    space = ""

                if i == 0:
                    row += " _______ "
                elif i == 1:
                    row += f"|{number}{space}     |"
                elif i == 2:
                    row += "|       |"
                elif i == 3:
                    row += f"|   {letterToSuit(card)}   |"
                elif i == 4:
                    row += "|       |"
                elif i == 5:
                    row += "|_______|"

        print(row)

#TEST CALL
cardArt(["Ks", "Qh", "10h", "9s"], True, False)