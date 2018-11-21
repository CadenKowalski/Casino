import random
import time
from Graphics import *
def Dice(Bet):
    global HouseTotal
    global PlayerTotal
    global win
    global Money
    def Player():
        global win
        global PlayerTotal
        hold = 'yes'
        turnScore = 0
        CurrentRoll = 0
        while hold == 'yes' and PlayerTotal + turnScore < 100:
            if Admin == True:
                CurrentRoll = int(input('CurrentRoll = '))
            else:
                CurrentRoll = random.randint(1,6)
            if CurrentRoll == 1:
                print('Player rolled a: 1')
                hold = 'no'
            else:
                turnScore += CurrentRoll
                print('Player rolled a:', CurrentRoll)
                print('Player Turn Score:', turnScore)
                hold = input('Do you want to roll again?: ').lower()
                if hold != 'yes' and hold != 'no':
                    while hold != 'yes' and hold != 'no':
                        print('Invalid input')
                        hold = input('Do you want to roll again?: ').lower()
        if hold == 'no' and CurrentRoll != 1:
            PlayerTotal += turnScore
            print('Player Total:', PlayerTotal)
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            turnScore = 0
        elif hold == 'no' and CurrentRoll == 1:
            turnScore == 0
            print('Player Total:', PlayerTotal)
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        if PlayerTotal + turnScore >= 100:
            win = True
    def House():
        global HouseTotal
        global win
        hold = 1
        turnScore = 0
        CurrentRoll = 0
        while hold == 1 and HouseTotal + turnScore < 100:
            CurrentRoll = random.randint(1,6)
            if CurrentRoll == 1:
                hold = 2
            else:
                hold = random.randint(1,2)
                turnScore += CurrentRoll
        if hold == 2 and CurrentRoll != 1:
            HouseTotal += turnScore
            print('House turn score:', turnScore)
            print('House Total:', HouseTotal)
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            turnScore = 0
        elif hold == 2 and CurrentRoll == 1:
            turnScore = 0
            print('House turn score:', turnScore)
            print('House Total:', HouseTotal)
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        elif HouseTotal + turnScore >= 100:
            print('House turn score:', turnScore)
            print('House Total:', HouseTotal)
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            win = True
    if Admin == True:
        HouseTotal = int(input('House Total = '))
        PlayerTotal = int(input('Player Total = '))
    else:
        HouseTotal = 0
        PlayerTotal = 0
    win = False
    while win != True:
        Player()
        if win != True:
            House()
    maximumC = HouseTotal
    maximumP = PlayerTotal
    if maximumC > maximumP:
        print('House Wins!')
        Money -= int(Bet)
        print('Money:', Money)
    else:
        if Admin == False:
            print('Player Wins!')
            if maximumP - 10 <= maximumC:
                Money += int((1.5 * int(Bet)))
            elif maximumP - 20 <= maximumC:
                Money += (2 * int(Bet))
            elif maximumP - 30 <= maximumC:
                Money += int((2.5 * int(Bet)))
            else:
                Money += (3 * int(Bet))
            print('Money:', Money)
        else:
            print('Player Wins!')
            scoring = input('Automatic risk or custom risk?: ').lower()
            if scoring != 'automatic' and scoring != 'custom':
                while scoreing != 'automatic' and scoring != 'custom':
                    print('Error')
                    scoring = input('Automatic or Custom: ').lower()
            if scoring == 'automatic':
                if maximumP - 10 <= maximumC:
                    Money += int((1.5 * int(Bet)))
                elif maximumP - 20 <= maximumC:
                    Money += (2 * int(Bet))
                elif maximumP - 30 <= maximumC:
                    Money += int((2.5 * int(Bet)))
                else:
                    Money += (3 * int(Bet))
            elif scoring == 'custom':
                Risk = int(input('Risk: '))
                Money += (Risk * int(Bet))
            print('Money:', Money)

def BlackJack(Bet):
    global Money
    if Admin == False:
        if int(Bet) < 1000:
            print('Sorry, the minimum bet for this game is 1000')
            while int(Bet) < 1000:
                Bet = input('Bet: ')
    def House():
        global HouseTotal
        global CTotal
        HouseTotal = 0
        CTotal = 0
        card1 = random.randint(1,14)
        if card1 == 11 or card1 == 12 or card1 == 13:
            card1 = 10
        elif card1 == 1 or card1 == 14:
            card1 = 11
        CTotal += card1
        card2 = random.randint(1,14)
        if card2 == 11 or card2 == 12 or card2 == 13:
            card2 = 10
        elif card2 == 1 or card2 == 14:
            if CTotal + 11 <= 21:
                card2 = 11
            else:
                card2 = 1
        if card1 == 11 and CTotal + card2 > 21:
            CTotal -= card1
            card1 = 1
            CTotal += card1
        CTotal += card2
        HouseTotal += card1
        HouseTotal += card2
        while HouseTotal < 17:
            card = random.randint(1,14)
            if card == 11 or card == 12 or card == 13:
                card = 10
            elif card == 1 or card == 14:
                if HouseTotal + 11 < 21:
                    card = 11
                else:
                    card = 1
            HouseTotal += card
    def Player(Bet):
        global PlayerTotal
        global Money
        if Admin == False:
            PlayerTotal = 0
            Card1 = random.randint(1,14)
            if Card1 == 11 or Card1 == 12 or Card1 == 13:
                Card1 = 10
            elif Card1 == 1 or Card1 == 14:
                Card1 = 11
            PlayerTotal += Card1
            Card2 = random.randint(1,14)
            if Card2 == 11 or Card2 == 12 or Card2 == 13:
                Card2 = 10
            elif Card2 == 1 or Card2 == 14:
                if PlayerTotal + 11 <= 21:
                    Card2 = 11
                else:
                    Card2 = 1
            if Card1 == 11 and PlayerTotal + Card2 > 21:
                PlayerTotal -= Card1
                Card1 = 1
                PlayerTotal += Card1
            PlayerTotal += Card2
        else:
            PlayerTotal = 0
            Card1 = int(input('Card1 = '))
            Card2 = int(input('Card2 = '))
            PlayerTotal += Card1
            PlayerTotal += Card2
        if Card1 + Card2 == 21:
            print('Black Jack')
            Money += 5 * int(Bet)
            print('Money:',Money)
        else:
            if Card1 == 1:
                print('Your first card is a 1')
            if Card1 == 11:
                print('Your first card is an Ace')
            if Card1 != 1 and Card1 != 11:
                print('Your first card is a',Card1)
            if Card2 == 1:
                print('Your second card is a 1')
                print('Your total is',PlayerTotal)
                print("The House's face up total is",(HouseTotal - CTotal))
            if Card2 == 11:
                print('Your second card is an Ace')
                print('Your total is',PlayerTotal)
                print("The House's face up total is",(HouseTotal - CTotal))
            if Card2 != 1 and Card2 != 11:
                print('Your second card is a',Card2)
                print('Your total is',PlayerTotal)
                print("The House's face up total is a",(HouseTotal - CTotal)) 
            HitStay = input('Do you want to hit or stay?: ').lower()
            if HitStay != 'hit' and HitStay != 'stay':
                while HitStay != 'hit' and HitStay != 'stay':
                    print('Invalid input')
                    HitStay = input('Do you want to hit or stay: ').lower()
            while HitStay == 'hit' and PlayerTotal <= 21:
                if Admin == False: 
                    Card = random.randint(1,14)
                else:
                    Card = int(input('Card = '))
                if Card == 11 or Card == 12 or Card == 13:
                    Card = 10
                elif Card == 1 or Card == 14:
                    if PlayerTotal + 11 < 21:
                        Card = 11
                    else:
                        Card = 1
                PlayerTotal += Card
                print('Your Card is a',Card)
                print('Your total is',PlayerTotal)
                print("The House's Face up total is",(HouseTotal - CTotal))
                if PlayerTotal <= 21:
                    HitStay = input('Do you want to hit or stay?: ').lower()
                    if HitStay != 'hit' and HitStay != 'stay':
                        while HitStay != 'hit' and HitStay != 'stay':
                            print('Invalid input')
                            HitStay = input('Do you want to hit or stay: ').lower()
            if PlayerTotal > 21:
                print('Bust')
                Money -= int(Bet)
            elif HouseTotal > 21:
                print('you win. The House had a bust')
                Money += (2 * int(Bet))
            elif PlayerTotal > HouseTotal:
                print('You win. The House had',HouseTotal)
                Money += (2 * int(Bet))
            elif HouseTotal > PlayerTotal:
                print('You lose. The House had',HouseTotal)
                Money -= int(Bet)
            elif PlayerTotal == HouseTotal:
                print('You tied with the House')
            print('Money:',Money)
    House()
    Player(Bet)
def HighRiskSlots(Bet):
    global Money
    if Admin == False:
        if int(Bet) < 1000:
            print('Sorry the minimum bet for this game is 1000')
            while int(Bet) < 1000:
                Bet = input('Bet: ')
    print('If you are in full screen mode, exit and click on the "HighRiskSlots" window.')
    GUI = GraphWin('HighRiskSlots', 650, 650)
    GUI.setBackground('Black')
    if Admin == False:
        n = random.randint(1,1000)
        Winning_Number = random.randint(1,1000)
    else:
        Winning_Number = int(input('Winning Number = '))
        n = int(input('Number = '))
    a = Text(Point(325,325), 'Press Anywhere To Start')
    a.setTextColor('Red')
    a.setSize(40)
    a.draw(GUI)
    GUI.getMouse()
    a.undraw()
    wns_one = random.randint(1,9)
    wns_two = random.randint(1,9)
    wns_three = random.randint(1,9)
    wnt = Text(Point(280,550), 'The winning number is: ')
    wnt.setSize(40)
    wnt.setTextColor('Red')
    wnt.draw(GUI)
    wn = Text(Point(520,550), Winning_Number)
    wn.setSize(40)
    wn.setTextColor('Red')
    wn.draw(GUI)
    for numbers in range(5):
        for number in range (9):
            a = Text(Point(130,325),number)
            b = Text(Point(325,325),abs(number-9))
            c = Text(Point(520,325),number)
            a.setSize(300)
            b.setSize(300)
            c.setSize(300)
            a.setTextColor('Red')
            b.setTextColor('Red')
            c.setTextColor('Red')
            a.draw(GUI)
            b.draw(GUI)
            c.draw(GUI)
            time.sleep(.01)
            a.undraw()
            b.undraw()
            c.undraw()
    if n == Winning_Number:
        show_number = Text(Point(325,325), Winning_Number)
        show_number.setSize(300)
        show_number.setTextColor('Red')
        show_number.draw(GUI)
        time.sleep(1)
        show_number.undraw()
        wn.undraw()
        wnt.undraw()
        a = Text(Point(325,325),'You Win!')
        a.setSize(100)
        a.setTextColor('Red')
        a.draw(GUI)
        for x in range(2):
            GUI.setBackground('LimeGreen')
            time.sleep(.5)
            GUI.setBackground('Black')
            time.sleep(.5)
        GUI.close()
        if Admin == False:
            Money += 1000 * int(Bet)
            print('Money:', Money)
        else:
            GUI.close()
            Risk = int(input('Risk: '))
            Money += Risk * int(Bet)
            print('Money:', Money)
    else:
        show_number = Text(Point(325,325), n)
        show_number.setSize(300)
        show_number.setTextColor('Red')
        show_number.draw(GUI)
        time.sleep(1)
        show_number.undraw()
        wn.undraw()
        wnt.undraw()
        Money -= int(Bet)
        a = Text(Point(325,325),'You Lose')
        a.setSize(100)
        a.setTextColor('LimeGreen')
        a.draw(GUI)
        for x in range(2):
            GUI.setBackground('Red')
            time.sleep(.5)
            GUI.setBackground('Black')
            time.sleep(.5)
        GUI.close()
        print('Money: ', Money)
def LowRiskSlots(Bet):
    global Money
    if Admin == False:
        if int(Bet) > 1000:
            print('Sorry, the maximum bet for this game is 1000')
            while int(Bet) > 1000:
                    Bet = input('Bet: ')
    print('If you are in full screen mode, exit and click on the "LowRiskSlots" window.')
    GUI = GraphWin('LowRiskSlots',650,650)
    GUI.setBackground('Black')
    if Admin == False:
        n = random.randint(1,100)
        Winning_number = random.randint(1,100)
    else:
        Winning_number = int(input('Winning Number = '))
        n = int(input('Number = '))
    a = Text(Point(325,325),'Press Anywhere To Start')
    a.setTextColor('Red')
    a.setSize(40)
    a.draw(GUI)
    GUI.getMouse()
    a.undraw()
    wns_one = random.randint(1,9)
    wns_two = random.randint(1,9)
    wnt = Text(Point(280,550), 'The winning number is: ')
    wnt.setSize(40)
    wnt.setTextColor('Red')
    wnt.draw(GUI)
    wn = Text(Point(510,550), Winning_number)
    wn.setSize(40)
    wn.setTextColor('Red')
    wn.draw(GUI)
    for numbers in range(7):
        for number in range(9):
            a = Text(Point(175,325),number)
            b = Text(Point(475,325),abs(number-9))
            a.setSize(300)
            a.setTextColor('Red')
            b.setSize(300)
            b.setTextColor('Red')
            a.draw(GUI)
            b.draw(GUI)
            time.sleep(.01)
            a.undraw()
            b.undraw()
    if n == Winning_number:
        show_number = Text(Point(325,325), Winning_number)
        show_number.setSize(300)
        show_number.setTextColor('Red')
        show_number.draw(GUI)
        time.sleep(1)
        show_number.undraw()
        wn.undraw()
        wnt.undraw()
        a = Text(Point(325,325),'You Win!')
        a.setSize(100)
        a.setTextColor('Red')
        a.draw(GUI)
        for x in range(2):
            GUI.setBackground('LimeGreen')
            time.sleep(.5)
            GUI.setBackground('Black')
            time.sleep(.5)
        GUI.close()
        if Admin == False:
            Money += 100 * int(Bet)
            print('Money:', Money)
        else:
            GUI.close()
            Risk = int(input('Risk: '))
            Money += Risk * int(Bet)
            print('Money:', Money)
    else:
        show_number = Text(Point(325,325), n)
        show_number.setSize(300)
        show_number.setTextColor('Red')
        show_number.draw(GUI)
        time.sleep(1)
        show_number.undraw()
        wn.undraw()
        wnt.undraw()
        Money -= int(Bet)
        a = Text(Point(325,325),'You Lose')
        a.setSize(100)
        a.setTextColor('LimeGreen')
        a.draw(GUI)
        for x in range(2):
            GUI.setBackground('Red')
            time.sleep(.5)
            GUI.setBackground('Black')
            time.sleep(.5)
        GUI.close()
        print('Money: ', Money)
def Hangman(Bet):
    global Money
    def Hangman_Processing(word):
        global Money
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        Letters = len(word)
        ShowWord = '_' * Letters
        guess = ''
        NOG = 0
        guessed = []
        if Admin == False:
            print(ShowWord)
        else:
            print('Word:', word)
        while guess != word and NOG <= 6:
            if ShowWord == word:
                print('YOU GUESSED THE WORD!!!!')
                if Letters > 11:
                    Money += 4* int(Bet)
                else:
                    Money += 3 * int(Bet)
                print('Money:',Money)
                break
            guess = input('Guess a letter, guess the word if you know it: ').lower()
            while guess not in letters and guess != word:
                guess = input('That is not a valid letter. Choose again: ').lower()
            while guess in guessed:
                guess = input('You already guessed that letter. Choose again: ').lower()
            if guess == word:
                print('YOU GUESSED THE WORD!!!!!')
                if Letters > 11:
                    Money += 4* int(Bet)
                else:
                    Money += 3 * int(Bet)
                print('Money:',Money)
            else:
                if word.count(guess) > 1:
                    location = []
                    a = []
                    x = 0
                    y = 0
                    z = -1
                    while x < word.count(guess):
                        z = word.find(guess, z+1)
                        location.append(z)
                        x += 1
                    for x in range(len(word)):
                        a.append(ShowWord[x])
                    while y < word.count(guess):
                        a[location[y]] = guess
                        y += 1
                    ShowWord = ''.join(a)
                    print('There are', word.count(guess), guess, "'s in the word")
                    guessed.append(guess)
                elif word.count(guess) == 1:
                    a = []
                    location = word.find(guess)
                    for x in range(len(word)):
                        a.append(ShowWord[x])
                    a[location] = guess
                    ShowWord = ''.join(a)
                    print('There is 1', guess, 'In the word')
                    guessed.append(guess)
                else:
                    print('That letter is not in the word')
                    guessed.append(guess)
                    NOG += 1
                    print('Guesses remaining:', 7 - NOG)
                if Admin == True:
                    print('Word:', word)
                print(ShowWord)
                if ShowWord != word:
                    print('Guessed Letters:')
                    for x in guessed:
                        print(' -', x)
        if NOG == 7:
            print('You are out of guesses')
            print('The word was:', word)
            Money -= Bet
            print('Money:',Money)
    if Admin == False:
        if int(Bet) < 200:
            print('Sorry th minimum bet for this game is 200')
            while int(Bet) < 200:
                Bet = input('Bet: ')
        if int(Bet) > 1000:
            print('Sorry th maximum bet for this game is 1000')
            while int(Bet) > 1000:
                Bet = input('Bet: ')
    inputt = input('Do you want to create your own word or select one from a predetermined list? If you choose your own word, you will get a bigger reward. (own/predetermined): ')
    if inputt == 'own':
        print('If your word is over 11 letters, you will get a bonus.')
        print('If you are in full screen, exit and click on the "Hangman Input" window')
        time.sleep(1)
        win = GraphWin("Hangman Input", 500, 500)
        textEntry = Entry(Point(250,250),20)
        textEntry.draw(win)
        exitText = Text(Point(250,350), 'Click anywhere to set word')
        exitText.setSize(40)
        exitText.draw(win)
        win.getMouse()
        word = textEntry.getText()
        word = word.lower()
        win.close()
        Hangman_Processing(word)
    else:
        Word_1 = 'pumpkin'
        Word_2 = 'racecar'
        Word_3 = 'firefighter'
        Word_4 = 'snowflake'
        Word_5 = 'sunshine'
        Word_6 = 'pillow'
        Word_7 = 'bulldozer'
        Word_8 = 'armchair'
        Word_9 = 'television'
        Word_10 = 'elevator'
        Word_11 = 'alphabet'
        Word_12 = 'teacup'
        Word_13 = 'charming'
        Word_14 = 'delicious'
        Word_15 = 'gorilla'
        Word_16 = 'helium'
        Word_17 = 'impossible'
        Word_18 = 'jailbreak'
        Word_19 = 'kangeroo'
        Word_20 = 'lamborghini'
        Word_21 = 'mercury'
        Word_22 = 'octopus'
        Word_23 = 'periscope'
        Word_24 = 'question'
        Word_25 = 'security'
        Word_26 = 'telescope'
        Word_27 = 'pneumonoultramicroscopicsilicovolcanoconiosis'
        numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26', 'challenge']
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        number = input('choose a number 1-26 or "challenge": ')
        while number not in numbers:
            number = input('That is not a valid number. Choose again: ') 
        if number == '1':
            word = Word_1
        elif number == '2':
            word = Word_2
        elif number == '3':
            word = Word_3
        elif number == '4':
            word = Word_4
        elif number == '5':
            word = Word_5
        elif number == '6':
            word = Word_6
        elif number == '7':
            word = Word_7
        elif number == '8':
            word = Word_8
        elif number == '9':
            word = Word_9
        elif number == '10':
            word = Word_10
        elif number == '11':
            word = Word_11
        elif number == '12':
            word = Word_12
        elif number == '13':
            word = Word_13
        elif number == '14':
            word = Word_14
        elif number == '15':
            word = Word_15
        elif number == '16':
            word = Word_16
        elif number == '17':
            word = Word_17
        elif number == '18':
            word = Word_18
        elif number == '19':
            word = Word_19
        elif number == '20':
            word = Word_20
        elif number == '21':
            word = Word_21
        elif number == '22':
            word = Word_22
        elif number == '23':
            word = Word_23
        elif number == '24':
            word = Word_24                               
        elif number == '25':
            word = Word_25
        elif number == '26':
            word = Word_26
        elif number == 'challenge':
            word = Word_27
        Hangman_Processing(word)
def BS(Bet):
    global CurrentCard
    global played_cards
    global win
    global Money
    if Admin == False:
        if int(Bet) < 1000:
            print('Sorry, the minimum bet for this game is 1000')
            while int(Bet) < 1000:
                Bet = input('Bet: ')
    def Deal(num_players):
        global hands
        global PlayerHand
        global num_AI
        cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
        hands = []
        for x in range(num_players):
            hands.append([])
        for hand in hands:
            for y in range(52 // num_players):
                index = random.randint(0, len(cards) - 1)
                hand.append(cards[index])
                del cards[index]
        if len(cards) > 0:
            for z in range(52 - ((y + 1) *3)):
                if len(cards) == 1:
                    hands[z].append(cards[0])
                    del cards[0]
                elif len(cards) > 1:
                    index = random.randint(0, len(cards) - 1)
                    hands[z].append(cards[index])
                    del cards[index]
        PlayerHand = hands[0]
        Sort(PlayerHand)
        num_AI = num_players
    def Sort(hand):
        global PlayerHand
        sorted_hand = []
        for x in range(len(hand)):
            sorted_hand.append(min(hand))
            PlayerHand.remove(min(hand))
        PlayerHand = sorted_hand
    def Player(diff):
        global CurrentCard
        global lie
        global win
        global played_cards
        global PlayerHand
        lie = False
        print('Players Turn')
        print('Hand:', PlayerHand)
        print('You are', str(CurrentCard) + "'s")
        card = int(input('Card: '))
        while card not in PlayerHand:
            print('That card is not in your hand')
            card = int(input('Card: '))
        if card != CurrentCard:
            lie = True
        ammount = int(input('How many: '))
        while PlayerHand.count(card) < ammount or ammount < 1:
            print("Invalid input")
            ammount = int(input('How many: '))
        if ammount == 1:
            played_cards.append(card)
            PlayerHand.remove(card)
        else:
            for c in range(ammount):
                played_cards.append(card)
                PlayerHand.remove(card)
        Call_BS = random.randint(1,5)
        if diff == 2:
            if Admin == False:
                if lie == True:
                    print('The house called BS on you')
                    for f in played_cards:
                        PlayerHand.append(f)
                    played_cards = []
                    Sort(PlayerHand)
            else:
                if lie == True:
                    print('The house called BS on you')
                    override = input('Override = ').lower()
                    if override == 'yes':
                        pass
                    else:
                        for f in played_cards:
                            PlayerHand.append(f)
                        played_cards = []
                        Sort(PlayerHand)
        else:
            if Call_BS == 1 or Call_BS == 5:
                print('The house called BS on you')
                if Admin == False:
                    if lie == True:
                        for f in played_cards:
                            PlayerHand.append(f)
                        played_cards = []
                        Sort(PlayerHand)
                    else:
                        pickAI = random.randint(1,3)
                        for f in played_cards:
                            hands[pickAI].append(f)
                        played_cards = []
                else:
                    override = input('Override = ').lower()
                    if override == 'yes':
                        pass
                    else:
                        if lie == True:
                            for f in played_cards:
                                PlayerHand.append(f)
                            played_cards = []
                            Sort(PlayerHand)
                        else:
                            pickAI = random.randint(1,3)
                            for f in played_cards:
                                hands[pickAI].append(f)
                            played_cards = []
        if CurrentCard < 13:
            CurrentCard += 1
        elif CurrentCard == 13:
            CurrentCard = 1
        if len(PlayerHand) == 0:
            print('The house called BS on you')
            if Admin == False:
                if lie == True:
                    for f in played_cards:
                        PlayerHand.append(f)
                    played_cards = []
                    Sort(PlayerHand)
                else:
                    win = True
            else:
                override = input('Override = ').lower()
                if override == 'yes':
                    win = True
                else:
                    if lie == True:
                        for f in played_cards:
                            PlayerHand.append(f)
                        played_cards = []
                        Sort(PlayerHand)
                    else:
                        win = True
        if win != True:
            print('Hand:', PlayerHand)
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    def House(num_AI):
        global PlayerHand
        global lie
        global win
        global CurrentCard
        global played_cards
        global hands
        for AI in range(1, num_AI):
            if Admin == True:
                print(hands[AI])
            if CurrentCard in hands[AI]:
                if hands[AI].count(CurrentCard) == 1:
                    played_cards.append(CurrentCard)
                    hands[AI].remove(CurrentCard)
                    print('House', AI, 'played 1,', CurrentCard)
                    PlayerCall_BS = input('Do you want to call BS?: ')
                    while PlayerCall_BS != 'yes' and PlayerCall_BS != 'Yes' and PlayerCall_BS != 'no' and PlayerCall_BS != 'No':
                        print('Invalid input')
                        PlayerCall_BS = input('Do you want to call BS?: ')
                    if PlayerCall_BS == 'yes' or PlayerCall_BS == 'Yes':
                        print('House', AI, 'did play 1,', CurrentCard)
                        for d in played_cards:
                            PlayerHand.append(d)                                                                                                    
                        Sort(PlayerHand)
                        played_cards = []
                        print('Your hand:', PlayerHand)
                elif hands[AI].count(CurrentCard) > 1:
                    print('House', AI, 'played', str(hands[AI].count(CurrentCard)) + ',', str(CurrentCard) + "'s")
                    PlayerCall_BS = input('Do you want to call BS?: ')
                    while PlayerCall_BS != 'yes' and PlayerCall_BS != 'Yes' and PlayerCall_BS != 'no' and PlayerCall_BS != 'No':
                        print('Invalid input')
                        PlayerCall_BS = input('Do you want to call BS?: ')
                    if PlayerCall_BS == 'yes' or PlayerCall_BS == 'Yes':
                        print('House', AI, 'did play', str(hands[AI].count(CurrentCard)) + ',', str(CurrentCard) + "'s")
                        for d in played_cards:
                            PlayerHand.append(d)
                        Sort(PlayerHand)
                        played_cards = []
                        print('Your hand:', PlayerHand)
                    for e in range(hands[AI].count(CurrentCard)):
                            played_cards.append(CurrentCard)
                            hands[AI].remove(CurrentCard)
                    
            else:
                for card in hands[AI]:
                    if hands[AI].count(card) > 1:
                        more = True
                        break
                    else:
                        more = False
                one_or_more = random.randint(1,2)
                if one_or_more == 1 or more == False:
                    card = random.randint(0, len(hands[AI]) - 1)
                    played_cards.append(hands[AI][card])
                    del hands[AI][card]
                    print('House', AI, 'played 1,', CurrentCard)
                    PlayerCall_BS = input('Do you want to call BS?: ')
                    while PlayerCall_BS != 'yes' and PlayerCall_BS != 'Yes' and PlayerCall_BS != 'no' and PlayerCall_BS != 'No':
                        print('Invalid input')
                        PlayerCall_BS = input('Do you want to call BS?: ')
                    if PlayerCall_BS == 'yes' or PlayerCall_BS == 'Yes':
                        print('Correct, House', AI, 'did not play 1,', CurrentCard)
                        for d in played_cards:
                            hands[AI].append(d)
                        played_cards = []
                    else:
                        print('Penut Butter')
                else:
                    for card in hands[AI]:
                        if hands[AI].count(card) > 1:
                            ammount = hands[AI].count(card)
                            break
                    for g in range(ammount):
                        played_cards.append(card)
                        hands[AI].remove(card)
                    print('House', AI, 'played', str(ammount) + ',', str(CurrentCard) + "'s")
                    PlayerCall_BS = input('Do you want to call BS?: ')
                    if PlayerCall_BS == 'yes' or PlayerCall_BS == 'Yes':
                        print('Correct, House', AI, 'did not play', ammount, ',', str(CurrentCard) + "'s")
                        for d in played_cards:
                            hands[AI].append(d)
                        played_cards = []
                    else:
                        print('Penut Butter')
            if CurrentCard < 13:
                CurrentCard += 1
            elif CurrentCard == 13:
                CurrentCard = 1
            if len(hands[AI]) == 0:
                win = True
                break
        if win != True:
            for b in range(1,num_AI):
                print('House', str(b) , 'has', len(hands[b]), 'cards left')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    Num_Players = int(input('How many players?: '))
    Difficulty = input('Computer difficulty, easy or hard: ').lower()
    while Difficulty != 'easy' and Difficulty != 'hard':
        print('Invalid input')
        Difficulty = input('Computer diffuculty, easy or hard: ').lower()
    if Difficulty == 'easy':
        Difficulty = 1
    else:
        Difficulty = 2
    Deal(Num_Players)
    CurrentCard = 1
    win = False
    played_cards = []
    if 1 in PlayerHand:
        turn = 'player'
        print('You started the game with 1 Ace')
        PlayerHand.remove(1)
        print('Hand:', PlayerHand)
        CurrentCard = 2
        while win != True:
            House(num_AI)
            if win != True:
                Player(Difficulty)
        if len(PlayerHand) == 0:
            print('Player Wins!')
            if Admin == True:
                Risk = int(input('Risk = '))
                Money += Risk * int(Bet)
            else:
                if Difficulty == 1:
                    Money += 3 * int(Bet)
                else:
                    Money += 10 * int(Bet)
            print('Money:', Money)
        else:
            print('House Wins')
            Money -= int(Bet)
            print('Money:', Money)
    else:
        for AI in range(1, num_AI):
            if 1 in hands[AI]:
                hands[AI].remove(1)
                CurrentCard = 2
                turn = AI
                break
        print('The House started the game with 1 Ace')
        while win != True:
            Player(Difficulty)
            if win != True:
                House(num_AI)
        if len(PlayerHand) == 0:
            print('Player Wins!')
            if Admin == True:
                Risk = int(input('Risk = '))
                Money += Risk * int(Bet)
            else:
                if Diffuculty == 1:
                    Money += 3 * int(Bet)
                else:
                    Money += 10 * int(Bet)
            print('Money:', Money)
        else:
            print('House Wins')
            Money -= int(Bet)
            print('Money:', Money)
global Admin
Admin = False
Money = 100000
print('Money: 100000')
print('1.) Low Risk Slots, Risk: 100x')
print('2.) High Risk Slots, Risk: 1000x')
print('3.) Dice, Risk: 1.5-3x')
print('4.) Black Jack, Risk: 2x or 5x')
print('5.) Hangman, Risk: 2-4x')
print('6.) BS, Risk: 3x or 10x')
print('7.) Exit the Casino')
game = input('Select the number of the game you want to play: ')
while game != '7':
    if game == '1':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        while DescriptionYN != 'yes' and DescriptionYN != 'no':
            print('Invalid input')
            DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('When the "LowRiskSlots" window pops up, click anywhere on it to start the slots machine. Once it finishes, if the number on the screen matches the number next to "Winning Number", you won. After the animation, the window will close automatically and tell you how much you won or lost. If you are in full screen mode, exit and click on the "LowRiskSlots" window.')
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        LowRiskSlots(Bet)
        PlayAgainO = input('Do you want to play again?: ')
        while PlayAgainO == 'yes':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            LowRiskSlots(Bet)
            PlayAgainO = input('Do you want to play again?: ')
    elif game == '2':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        while DescriptionYN != 'yes' and DescriptionYN != 'no':
            print('Invalid input')
            DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('When the "HighRiskSlots" window pops up, click anywhere on it to start the slots machine. Once it finishes, if the number on the screen matches the number next to "Winning Number", you won. After the animation, the window will close automatically and tell you how much you won or lost. If you are in full screen mode, exit and click on the "HighRiskSlots" window.')
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        HighRiskSlots(Bet)
        PlayAgainT = input('Do you want to play again?: ')
        while PlayAgainT == 'yes':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            HighRiskSlots(Bet)
            PlayAgainT = input('Do you want to play again?: ')
    elif game == '3':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        while DescriptionYN != 'yes' and DescriptionYN != 'no':
            print('Invalid input')
            DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('When you start the game, a dice will roll and return a value from 1-6. If that value is 2-6, it is added to your turn score. Then, it asks you if you want to roll again. If you say yes, the process will repeat. If not, your turn score will be added to your overall score. However, if you choose to roll again and roll a 1, the points from your turn get erased and not added to your overall score.')
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        Dice(Bet)
        PlayAgainTh = input('Do you want to play again?: ')
        while PlayAgainTh =='yes':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            Dice(Bet)
            PlayAgainTh = input('Do you want to play again?: ')
    elif game == '4':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        while DescriptionYN != 'yes' and DescriptionYN != 'no':
            print('Invalid input')
            DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('At the start of the game, you will be dealt 2 cards. The total of these to cards will be displayed. After that it will ask you if you want to hit (get another card) or stay (stop getting cards). If you choose to hit, you will be dealt another card and it will be added to your score. If you choose to stay, your total will be compared to the House. If your score is larger than theirs and less than or equal to 21, you win. If your score is less than theirs, you lose. If your score is greater than 21, the House automaticaly wins. If your first 2 cards add up to 21, that is Black Jack and you automatically win')
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        BlackJack(Bet)
        PlayAgainF = input('Do you want to play again?: ')
        while PlayAgainF =='yes':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            BlackJack(Bet)
            PlayAgainF = input('Do you want to play again?: ')
    elif game == '5':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        while DescriptionYN != 'yes' and DescriptionYN != 'no':
            print('Invalid input')
            DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('When the game starts, choose if you want to make your own word or select one from a list. If you choose your own word and are in full screen mode, exit and click on the "Hangman Input" window. Once you have entered your word, click anywhere within the window to set it. After that, type your letter guess and then it will tell you if that letter is in the word. You have 7 wrong guesses and once you are out, you lose.') 
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        Hangman(Bet)
        PlayAgainFI = input('Do you want to play again?: ')
        while PlayAgainFI == 'yes':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            Hangman(Bet)
            PlayAgainFI = input('Do you want to play again?: ')
    elif game == '6':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        while DescriptionYN != 'yes' and DescriptionYN != 'no':
            print('Invalid input')
            DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('When the game starts, you will be asked how many players you want to play with. For example, if I put "4", it would be me and 3 Computers. Finally it will ask you what difficulty you want the computers to be set at. Making them harder will give you a bigger reward if you win. Then it will start the game. The first play of the game is allways putting down an ace face up so if you have an ace, you will go first but if you do not, one of the computers will go first. Then on your turn it will show you your hand and then tell you what card you are supposed to put down. ones are Aces, elevens are Jacks, twelves are Queens, and thirteens are Kings. It will ask you what card you want to put down and you can either put down the correct card or lie and put down a different card if you do not have the one you need. Then it will ask you how many of the card you want to put down so if you have more than one, you can put them all down together. Then on the computers turn, it will tell you what they played and how many cards they played. Then it will ask you if you want to call BS. By calling BS you are saying that you think they are lying and not putting down the card they are supposed to. If you are right and they are lying, they have to take all of the cards that have been played. If you are wrong and they did play what they were supposed to, you have to take all of the cards. The first person to 0 cards wins.')
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        BS(Bet)
        PlayAgainFI = input('Do you want to play again?: ')
        while PlayAgainFI == 'yes':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            BS(Bet)
            PlayAgainFI = input('Do you want to play again?: ')
    elif game == '8':
        password = input('Security ID: ')
        if password == '699':
            Admin = True
            print('Admin privileges granted')
        else:
            print('One More Chance')
            password = input('Security ID: ')
            if password == '699':
                Admin = True
                print('Admin privileges granted')
            else:
                Money = 0
                print('Money:', Money)
                game = '7'
    if game != '7':
        print('1.) Low Risk Slots, Risk: 100x')
        print('2.) High Risk Slots, Risk: 1000x')
        print('3.) Dice, Risk: 1.5-3x')
        print('4.) Black Jack, Risk: 2x or 5x')
        print('5.) Hangman, Risk: 2-4x')
        print('6.) BS, Risk: 3x or 10x')
        print('7.) Exit the Casino')
        game = input('Select the number of the game you want to play: ')
    else:
        pass
if Money < 100000:
    print('Losings:', 100000 - Money)
elif Money > 100000:
    print('Earnings:', Money - 100000)
