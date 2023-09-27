import random
from ui import clearTerminal
from art import cardArt

class BlackjackTable:

    newPlayerChips = 500
    requiredStartBet = 0
    suits = ['h', 'd', 'c', 's']
    faceCards = ['J', 'Q', 'K']

    def __init__(self, chips = newPlayerChips, deck = [], currentGames = [], dealerCards = [], cutCardFound = False):
        self.chips = chips
        self.deck = deck
        self._shuffle()
        self.reShuffle = False
        self.needToReshuffle = False
        self.dealerCards = dealerCards
        self.currentGames = currentGames
        self.startingChips = chips
        self.cutCardFound = cutCardFound
        self.dealerScore = 0
        self.dealerHitting = False
        self.dealerBlackjack = False
        self.dealerBust = False
        self.playerHandsIncomplete = 0
        self.exitMessage = ""
        self.splitsAllowed = 3
        self.insuranceBet = 0
        self.insuranceDenied = False
        self.exitMessageRelayed = False
        self.completedSplitHands = []
        self.completedSplitHandsValues = []
        self.completedSplitHandsMessages = []
        self.insuranceMessage = ""
        self.insurancePaidOut = False

    def startFresh(self, message):
        self.needToReshuffle = False
        self.dealerCards = []
        self.currentGames = []
        self.dealerScore = 0
        self.dealerHitting = False
        self.dealerBlackjack = False
        self.dealerBust = False
        self.playerHandsIncomplete = 0
        self.exitMessage = ""
        self.splitsAllowed = 3
        self.insuranceBet = 0
        self.insuranceDenied = False
        self.exitMessageRelayed = False
        self.completedSplitHands = []
        self.completedSplitHandsValues = []
        self.completedSplitHandsMessages = []
        self.insuranceMessage = ""
        self.insurancePaidOut = False
        
        self.createBlackjackGame(message)

    #GETTERS AND SETTERS
    def insurancePaidOutAttr(self, value = None):
        if value == None:
            return self.insurancePaidOut
        else:
            self.insurancePaidOut = value

    def insuranceMessageAttr(self, value = None):
        if value == None:
            return self.insuranceMessage
        else:
            self.insuranceMessage = value

    def insuranceDeniedAttr(self, value = None):
        if value == None:
            return self.insuranceDenied
        else:
            self.insuranceDenied = value

    def completedSplitHandsAttr(self, value = None):
        if value == None:
            return self.completedSplitHands
        else:
            self.completedSplitHands.append(value)

    def completedSplitHandsValuesAttr(self, value = None):
        if value == None:
            return self.completedSplitHandsValues
        else:
            self.completedSplitHandsValues.append(value)

    def completedSplitHandsMessagesAttr(self, value = None):
        if value == None:
            return self.completedSplitHandsMessages
        else:
            self.completedSplitHandsMessages.append(value)

    def chipsAttr(self, key = None, value = None):
        if key == "subtract":
            self.chips -= value
        elif key == "add":
            self.chips += value
        else:
            return self.chips
    
    def dealerCardsAttr(self, value = None):
        if value == None:
            return self.dealerCards
        elif value ==  "reset":
            self.dealerCards = []
        else:
            self.dealerCards = value
    
    def deckAttr(self):
        return self.deck
    
    def reShuffleAttr(self, value = None):
        if value in [True, False]:
            self.reShuffle = value
        else:
            return self.reShuffle
        
    def needToReshuffleAttr(self, value = None):
        if value in [True, False]:
            self.needToReShuffle = value
        else:
            return self.needToReshuffle
        
    def dealerScoreAttr(self, value = None):
        if not value == None:
            self.dealerScore = value
        else:
            return self.dealerScore
    
    def dealerBlackjackAttr(self, value = None):
        if value in [True, False]:
            self.dealerBlackjack = value
        else:
            return self.dealerBlackjack
        
    def dealerBustAttr(self, value = None):
        if value in [True, False]:
            self.dealerBust = value
        else:
            return self.dealerBust
    
    def dealerHittingAttr(self, value = None):
        if value in [True, False]:
            self.dealerHitting = value
        else:
            return self.dealerHitting
        
    def cutCardFoundAttr(self, value = None):
        if value in [True, False]:
            self.cutCardFound = value
        else:
            return self.cutCardFound
        
    def startingChipsAttr(self):
        return self.startingChips
    
    def playerHandsIncompleteAttr(self, value = None):
        if value == None:
            return self.playerHandsIncomplete
        elif value == "subtract":
            self.playerHandsIncomplete -= 1
        elif value == "add":
            self.playerHandsIncomplete += 1
        elif value == "reset":
            self.playerHandsIncomplete = 0
    
    def currentGamesAttr(self, value = None):
        if value == "reset":
            self.currentGames = []
        else:
            return self.currentGames
    
    def splitsAllowedAttr(self, value = None):
        if value == None:
            return self.splitsAllowed
        elif value == "subtract":
            self.splitsAllowed -= 1

    def insuranceBetAttr(self, value = None):
        if value == None:
            return self.insuranceBet
        else:
            self.insuranceBet = value

    def exitMessageAttr(self, value = None):
        if value == None:
            return self.exitMessage
        else:
            self.exitMessage = value
    
    def exitMessageRelayedAttr(self, value = None):
        if value == None:
            return self.exitMessageRelayed
        else:
            self.exitMessageRelayed = value

    def _shuffle(self, cutCard = True):
        """Returns a randomized deck of 52 cards
        
        (optional bool parameter to include cut card "Joker" [default = True])
        """
        def includeCutCard():
            deck.insert(random.randint(14,len(deck) - 15), "Joker")
        
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [value + suit for suit in self.suits for value in values]

        random.shuffle(deck)

        if cutCard:
            includeCutCard()
            self.cutCardFound = False

        self.deck = deck

    def createBlackjackGame(self, message = None, splitInitiated = False, splitCard = "", initialBet = requiredStartBet, insuranceTaken = False):
        newHandIndex = len(self.currentGames)
        self.currentGames.append(self.Blackjack(self, newHandIndex, initialBet, insuranceTaken))

        self.currentGames[newHandIndex].startHand(message, splitInitiated, splitCard)

    def HANDTESTER(self, dealerHand = [], playerHand = []):
        """FOR DEBUGGING PURPOSES ONLY, DO NOT USE"""
        self.currentGames.append(self.Blackjack(self, 0, 0))
        self.currentGames[0].startHand(artificialDealerHand=dealerHand, artificialPlayerHand=playerHand)


    class Blackjack:
        ace = ['A']
        allAces = ['Ah', 'Ad', 'Ac', 'As']

        def __init__(self, outerInstance, handIndex, initialBet, insuranceTaken = False):
            self.outerInstance = outerInstance
            self.handIndex = handIndex
            self.playerCards = []
            self.playerScore = 0
            self.playerBust = False
            self.playerBlackjack = False
            self.playerHitting = True
            self.roundActive = True
            self.playerWins = False
            self.dealerWins = False
            self.push = False
            self.currentBet = initialBet
            self.exitMessageGiven = False
            self.insuranceTaken = insuranceTaken
            self.doubleDown = False
            self.canDoubleDown = True
            self.hasSplit = False
            self.outerInstance.playerHandsIncompleteAttr("add")

        def startHand(self, message = None, splitInitiated = False, splitCard = "", artificialDealerHand = None, artificialPlayerHand = None):
            def yesOrNoInput(message = "", revealDealer = False, showSplitCards = False):
                while True:
                    clearTerminal()
                    showCardArt(True, message, revealDealer, showSplitCards)
                    inputStr = input("Yes or No?: ")

                    if inputStr == "":
                        message = "Please enter something..."
                        continue

                    inputStr = inputStr.lower()[0]

                    if inputStr in ['y', 'n']:
                        return inputStr
                    else:
                        message = "Please only enter Yes or No..."

            def hitOrStandInput(message = ""):
                while True:
                    clearTerminal()
                    showCardArt(True, message)
                    inputStr = input("Hit or Stand?: ")

                    if inputStr == "":
                        message = "Please enter something..."
                        continue

                    inputStr = inputStr.lower()[0]

                    if inputStr in ['h', 's']:
                        return inputStr
                    else:
                        message = "Please only enter Hit or Stand..."

            def doubleDown(inputStr = "", message = ""):
                """
                players can choose to double their original bet after seeing their initial two cards and receive
                only one additional card.
                """
                while not inputStr in ['y','n']:
                    if not message == "":
                        clearTerminal()
                        showCardArt(True, message)

                    inputStr = input("Would you like to double down?: (y/n)(help): ")

                    if inputStr == "":
                        message = "Please enter something..."

                    if len(inputStr) > 0:
                        inputStr = inputStr.lower()[0]

                    if inputStr == 'n':
                        return False
                    elif inputStr == 'y':
                        self.playerHitting = False
                        self.outerInstance.dealerHittingAttr(True)
                        self.canDoubleDown = False
                        
                        currentBet = self.currentBet
                        self.currentBet = currentBet * 2
                        self.outerInstance.chipsAttr("subtract", currentBet)
                        
                        if hitOrStandInput() == 'h':
                            self._hit()

                        return True
                    else:
                        if inputStr == 'h':
                            message = "players can choose to double their original bet after seeing their initial two cards but only receive up to ONE additional card."
                        else:
                            message = "Yes or No"

            def insurance(message = ""):
                """
                Insurance: Players have the option to take insurance when the dealer's face-up card is an Ace.
                This is a side bet that pays 2:1 if the dealer has a Blackjack.
                """
                self.outerInstance.insuranceDeniedAttr(True)

                if self.outerInstance.dealerCardsAttr()[1] in BlackjackTable.Blackjack.allAces and not self.insuranceTaken:
                    message = "The dealer has a visible Ace, would you like to take insurance?\nSeparate bet with a 2:1 payout if the dealer has Blackjack."
                    
                    if yesOrNoInput(message) == 'y':
                        self.insuranceTaken = True
                        message = placeBet(self.insuranceTaken)
                    else:
                        message = ""

                    return message
                        
            def placeBet(insurance = False, bet = False):
                """Returns bet [(int) if number, (bool) if not number] and message (string)"""
                def inputChecker(betStr):
                    for char in betStr:
                        if not char.isdigit():
                            return False, "Whole numbers only..."
                    if betStr == "" or betStr == " " or betStr == None:
                        return False, "You must bet something..."
                    bet = int(betStr)
                    if bet == 0:
                        return False, "You must bet something..."
                    elif not bet % 10 == 0:
                        return False, "Bets must be in increments of 10 only..."
                    elif bet > self.outerInstance.chipsAttr():
                        return False, f"You only have {self.outerInstance.chipsAttr()} chips to bet..."
                    return bet, f"Your bet of {bet} chips has been accepted, dealer matches..."
                
                def betInput(betStr = False, message = ""):
                    """Returns a valid bet"""
                    bet = False
                    while bet == False:
                        clearTerminal()
                        if not message == "":
                            print(message)
                        betStr = input(f"You have {self.outerInstance.chipsAttr()} chips.\nPlace your bet (increments of 10 only): ")
                        bet, message = inputChecker(betStr)

                    return bet, message

                clearTerminal()
                bet, message = betInput()
                self.outerInstance.chipsAttr("subtract", bet)
                
                if not insurance:
                    self.currentBet = bet
                else:
                    self.outerInstance.insuranceBetAttr(bet)

                return message

            def settleBet(outcome):
                pot = self.currentBet * 2

                if outcome == "win":
                    if self.playerBlackjack:
                        blackjackPot = self.currentBet * 3
                        self.outerInstance.chipsAttr("add", blackjackPot)
                        message = f"You won with a {'natural ' if len(self.playerCards) == 2 else ''}Blackjack!! You take the pot with {blackjackPot} chips!\n"
                        
                    else:
                        self.outerInstance.chipsAttr("add", pot)
                        message = f"Player wins! You take the pot with {pot} chips!\n"
                elif outcome == "lose" and not self.push:
                    message = f"Dealer wins...\n"
                else:
                    self.outerInstance.chipsAttr("add", self.currentBet)
                    self.outerInstance.chipsAttr("add", self.outerInstance.insuranceBetAttr())
                    message = "Push! All bets are returned.\n"

                if self.insuranceTaken and not self.outerInstance.insurancePaidOutAttr() and self.outerInstance.playerHandsIncompleteAttr() == 1:
                    if self.outerInstance.dealerBlackjackAttr():
                        insurancePayout = self.outerInstance.insuranceBetAttr() * 2
                        self.outerInstance.chipsAttr("add", insurancePayout)
                        self.outerInstance.insurancePaidOutAttr(True)
                        insuranceMessage = f"Dealer had Blackjack, insurance pays out {insurancePayout} chips!\n"
                        self.outerInstance.insuranceMessageAttr(insuranceMessage)
                        

                self.playerWins = False
                self.dealerWins = False
                self.push = False
                self.currentBet = 0
                self.insuranceTaken = False

                return message
            
            def showCardArt(messageAtEnd = False, message = "", dealerReveal = False, displaySplit = False):
                clearTerminal()
                
                if not messageAtEnd:
                    print(message)

                print(f"Chips: {self.outerInstance.chipsAttr()}\tCurrent Bet: {self.currentBet}")
                if self.insuranceTaken:
                    print(f"Insurance Bet: {self.outerInstance.insuranceBetAttr()}")

                cardArt(self.outerInstance.dealerCardsAttr(), True, dealerReveal)
                
                if dealerReveal:
                    print(f"\nCard Value: {self.outerInstance.dealerScoreAttr()}\n")
                else:
                    print()
                
                if displaySplit:
                    for index in range(0, len(self.outerInstance.completedSplitHandsAttr())):
                        cardArt(self.outerInstance.completedSplitHandsAttr()[index], playerName=f"Hand {index + 1}")
                        print(f"\nCard Value: {self.outerInstance.completedSplitHandsValuesAttr()[index]}\n")
                        print(self.outerInstance.completedSplitHandsMessagesAttr()[index])
                else:
                    cardArt(self.playerCards)
                    print(f"\nCard Value: {self.playerScore}\n")

                if messageAtEnd:
                    print(message)

            def checkWinner():
                if self.push:
                    message = settleBet("push")
                    return message

                if self.playerBust:
                    self.dealerWins = True
                elif self.outerInstance.dealerBustAttr():
                    self.playerWins = True
                elif self.playerScore > self.outerInstance.dealerScoreAttr():
                    self.playerWins = True
                elif self.outerInstance.dealerScoreAttr() > self.playerScore:
                    self.dealerWins = True
                else:
                    if self.playerBlackjack:
                        if self.outerInstance.dealerBlackjackAttr():
                            self.push = True
                    elif self.playerScore == self.outerInstance.dealerScoreAttr():
                        self.push = True
                
                if self.playerWins:
                    message = settleBet("win")
                elif self.dealerWins:
                    message = settleBet("lose")
                elif self.push:
                    message = settleBet("push")
                return message
            
            def splitChecker():
                if self.outerInstance.splitsAllowedAttr() > 0:
                    if self.hasSplit == False:

                        card1 = self.playerCards[0]
                        card2 = self.playerCards[1]
                        card1Length = len(card1)
                        card2Length = len(card2)

                        if card1Length == card2Length:
                            if card1Length == 2:
                                if card1[0] == card2[0]:
                                    return True
                            else:
                                card1Concat = card1[0] + card1[1]
                                card2Concat = card2[0] + card2[1]
                                if card1Concat == card2Concat:
                                    return True
                return False
            
            #start the game with 2 cards for player and dealer
            if not splitInitiated:
                self._hit()
                self._hit("dealer")
                self._hit()
                self._hit("dealer")
            elif splitInitiated:
                self.playerCards.append(splitCard)
                self._hit()

            #DEBUG PURPOSES ONLY
            if not artificialDealerHand == None and not artificialPlayerHand == None:
                self.playerCards = []
                self.outerInstance.dealerCardsAttr("reset")
                
                self._hit(TESTCARD=artificialPlayerHand[0])
                self._hit("dealer", TESTCARD=artificialDealerHand[0])
                self._hit(TESTCARD=artificialPlayerHand[1])
                self._hit("dealer", TESTCARD=artificialDealerHand[1])

            self.outerInstance.reShuffleAttr(False)

            if self.currentBet == 0:
                message = placeBet()

            if not self.outerInstance.insuranceDeniedAttr():
                insurance(message)
            
            if splitChecker():
                message = "You received a pair, would you like to split?\nA split is when you split your two starting cards into separate hands and receive an additional card for both.\nYour bet for the second hand will be the same as the first and you'll play each hand individually against the same dealer cards.\n"
                if yesOrNoInput(message) == 'y':
                    self.hasSplit = True
                    self.outerInstance.splitsAllowedAttr("subtract")
                    message = "Split Initiated!\n"
                    splitCard = self.playerCards.pop(1)
                    self._hit() 
                    self.outerInstance.chipsAttr("subtract", self.currentBet)
                    self.outerInstance.createBlackjackGame(message, True, splitCard, self.currentBet, self.insuranceTaken)
                else:
                    message = ""


            while self.roundActive and not self.playerBust and not self.outerInstance.dealerBustAttr():
                showCardArt(True, message)

                if self.currentBet * 2 <= self.outerInstance.chipsAttr() + self.currentBet + self.outerInstance.insuranceBetAttr() and self.canDoubleDown:
                    self.doubleDown = doubleDown()

                if self.playerHitting and not self.doubleDown:
                    if hitOrStandInput() == 'h':
                        self._hit()
                    else:
                        self.playerHitting = False
                        self.outerInstance.dealerHittingAttr(True)
                        
                    self.canDoubleDown = False
                elif not self.playerHitting and self.outerInstance.dealerHittingAttr():
                    self._stand()
                else:
                    self.roundActive = False

            self.outerInstance.playerHandsIncompleteAttr("subtract")
            topMessage = checkWinner()
            
            self.outerInstance.completedSplitHandsAttr(self.playerCards)
            self.outerInstance.completedSplitHandsValuesAttr(self.playerScore)
            self.outerInstance.completedSplitHandsMessagesAttr(topMessage)
            
            if self.outerInstance.playerHandsIncompleteAttr() == self.handIndex and self.handIndex == 0:

                if self.outerInstance.chipsAttr() > 0:
                    topMessage = self.outerInstance.insuranceMessageAttr()
                    bottomMessage = ("Play another round? ")
                    fullMessage = topMessage + bottomMessage

                    if yesOrNoInput(fullMessage, True, False if len(self.outerInstance.completedSplitHandsAttr()) == 0 else True) == "y":
                        if self.outerInstance.needToReshuffleAttr():
                            self.outerInstance._shuffle()
                            self.outerInstance.reShuffleAttr(True)

                        self.outerInstance.startFresh(message)
                
            if not self.outerInstance.exitMessageRelayedAttr():
                apostrophe = "'"
                if self.outerInstance.chipsAttr() >= self.outerInstance.startingChipsAttr():
                    message = f"{f'You left with {self.outerInstance.chipsAttr()} chips, {self.outerInstance.chipsAttr() - self.outerInstance.startingChipsAttr()} more than you started with!' if self.outerInstance.chipsAttr() > self.outerInstance.startingChipsAttr() else f'You broke even... Could be worse!'}"
                else:    
                    message = f"{f'You left with {self.outerInstance.chipsAttr()} chips! At least you didn{apostrophe}t lose it all...' if self.outerInstance.chipsAttr() > 0 else f'You{apostrophe}re down to the felt... Better luck next time...'}"
                message += "Thanks for playing!!!"
                self.outerInstance.exitMessageAttr(message)
                print(self.outerInstance.exitMessageAttr())
                self.outerInstance.exitMessageRelayedAttr(True)

            

        def _hit(self, player = "player", TESTCARD = ""):
            def checkBust():
                if score > 21:
                    if player == "player":
                        self.playerBust = True
                    elif player == "dealer":
                        if self.outerInstance.dealerScoreAttr() == 22: # special case for if the dealer has a value of 22, triggers a push
                            self.push = True
                        else:
                            self.outerInstance.dealerBustAttr(True)

            def checkBlackjack():
                if score == 21 and len(cards) == 2:
                    if player == "player":
                        self.playerBlackjack = True
                    elif player == "dealer":
                        self.outerInstance.dealerBlackjackAttr(True)
            
            def cardTotal():
                tempCards = []
                acesRemaining = 0
                for tempCard in cards:
                    if tempCard in BlackjackTable.Blackjack.allAces:
                        tempCards.append(tempCard)
                        acesRemaining += 1
                    else:
                        tempCards.insert(0,tempCard)

                score = 0
                for card in tempCards:
                    if len(card) == 2:
                        number = card[0]
                        if number in BlackjackTable.faceCards:
                            number = 10
                        elif number in BlackjackTable.Blackjack.ace:
                            if acesRemaining == 1:
                                if score <= 10:
                                    number = 11
                                else:
                                    number = 1
                            elif acesRemaining == 2:
                                if score <= 9:
                                    number = 11
                                else:
                                    number = 1
                            elif acesRemaining == 3:
                                if score <= 8:
                                    number = 11
                                else:
                                    number = 1
                            else:
                                if score <= 7:
                                    number = 11
                                else:
                                    number = 1
                            acesRemaining -= 1
                        else:
                            number = int(number)
                    else:
                        number = int(card[0] + card[1])
                    score += number
                    
                return score
            
        
            if player == "player":
                cards = self.playerCards
            elif player == "dealer":
                cards = self.outerInstance.dealerCardsAttr()

            if not TESTCARD == "":
                pulledCard = TESTCARD
            else:
                pulledCard = self.outerInstance.deckAttr().pop(random.randint(0,len(self.outerInstance.deckAttr()) - 1))

            if pulledCard == 'Joker':
                self.outerInstance.needToReshuffleAttr(True)
                self.outerInstance.cutCardFoundAttr(True)
                cards.append(self.outerInstance.deckAttr().pop(random.randint(0,len(self.outerInstance.deckAttr()) - 1)))
            else:
                cards.append(pulledCard)

            score = cardTotal()
            
            if player == "player":
                self.playerScore = score
            elif player == "dealer":
                self.outerInstance.dealerScoreAttr(score)
            
            checkBust()
            checkBlackjack()

        def _stand(self):
            """
            Start the dealer sequence
            """
            self.playerHitting = False
            print(self.outerInstance.playerHandsIncompleteAttr())
            if self.outerInstance.playerHandsIncompleteAttr() == self.handIndex + 1:

                if self.outerInstance.dealerScoreAttr() >= 17:
                    if self.outerInstance.dealerScoreAttr() == 17:
                        for card in self.outerInstance.dealerCardsAttr():
                            if card in BlackjackTable.Blackjack.allAces:
                                self._hit("dealer")
                                
                    self.outerInstance.dealerHittingAttr(False)
                else:
                    self._hit("dealer")