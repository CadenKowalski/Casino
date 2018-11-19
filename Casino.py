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
        if Admin == True:
            hold = 'yes'
            turnScore = 0
            CurrentRoll = 0
            while hold == 'yes' and PlayerTotal + turnScore < 100:
                CurrentRoll = int(input('CurrentRoll = '))
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
        else:
            hold = 'yes'
            turnScore = 0
            CurrentRoll = 0
            while hold == 'yes' and PlayerTotal + turnScore < 100:
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
    if Admin ==True:
        HouseTotal = int(input('House Total = '))
        PlayerTotal = int(input('Player Total = '))
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
            print('Player Wins!')
            scoring = input('Automatic risk or custom risk?: ').lower()
            if scoring != 'automatic' and scoring != 'custom':
                while scoreing != 'automatic' and scoring != 'custom':
                    print('Error')
                    scoring = input('Automatic or Custom: ').lower()
            if scoring == 'automatic':
                if maximumP - 10 <= maximumC:
                    Money += (1.5 * int(Bet))
                elif maximumP - 20 <= maximumC:
                    Money += (2 * int(Bet))
                elif maximumP - 30 <= maximumC:
                    Money += (2.5 * int(Bet))
                else:
                    Money += (3 * int(Bet))
            elif scoring == 'custom':
                Risk = int(input('Risk: '))
                Money += (Risk * int(Bet))
            print('Money:', Money)
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
            print('Player Wins!')
            if maximumP - 10 <= maximumC:
                Money += (1.5 * int(Bet))
            elif maximumP - 20 <= maximumC:
                Money += (2 * int(Bet))
            elif maximumP - 30 <= maximumC:
                Money += (2.5 * int(Bet))
            else:
                Money += (3 * int(Bet))
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
                    Card = random.randint(1,14)
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
        elif Admin == True:
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
                    Risk = int(input('Risk: '))
                    Money += (Risk * int(Bet))
                elif PlayerTotal > HouseTotal:
                    print('You win. The House had',HouseTotal)
                    Risk = int(input('Risk: '))
                    Money += (Risk * int(Bet))
                elif HouseTotal > PlayerTotal:
                    print('You lose. The House had',HouseTotal)
                    Money -= int(Bet)
                elif PlayerTotal == HouseTotal:
                    print('You tied with the House')
                print('Money:',Money)
    House()
    Player(Bet)
def HighRiskSlots(Bet):
    if int(Bet) < 200:
        print('Sorry th minimum bet for this game is 200')
        while int(bet) < 200:
            Bet = input('Bet: ')
    global Money
    GUI = GraphWin('HighRiskSlots',650,650)
    GUI.setBackground('Black')
    nOne = random.randint(1,10)
    nTwo = random.randint(1,10)
    a = Text(Point(325,325),'Press Anywhere To Start')
    a.setTextColor('Red')
    a.setSize(40)
    a.draw(GUI)
    GUI.getMouse()
    a.undraw()
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
    if nOne == nTwo:
        Money += 50 * int(Bet)
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
        print('Money: ', Money)
    else:
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
        GUI = GraphWin('LowRiskSlots',650,650)
        GUI.setBackground('Black')
        n = random.randint(1,100)
        Winning_number = random.randint(1,100)
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
            show_number = Text(Point(325,325), Winninhg_number)
            show_number.setSize(300)
            show_number.setTextColor('Red')
            show_number.draw(GUI)
            time.sleep(1)
            show_number.undraw()
            wn.undraw()
            wnt.undraw()
            Money += 5 * int(Bet)
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
            print('Money: ', Money)
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
    elif Admin == True:
        print('If you are in full screen mode, exit and click on the "LowRiskSlots" window.')
        GUI = GraphWin('LowRiskSlots',650,650)
        GUI.setBackground('Black')
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
            Risk = int(input('Risk: '))
            Money += Risk * int(Bet)
            print('Money: ', Money)
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
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        Letters = len(word)
        ShowWord = '_' * Letters
        guess = ''
        NOG = 0
        guessed = []
        if Admin == False:
            print(ShowWord)
            while guess != word and NOG <= 7:
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
                    print('Guesses remaining: ', 13 - NOG)
                    print(ShowWord)
                    print('Guessed Letters:')
                    for x in guessed:
                        print(' -', x)
            if NOG == 13:
                print('You are out of guesses')
                print('The word was:', word)
                Money -= Bet
                print('Money:',Money)
        elif Admin == True:
            print('Word:',word)
            print(ShowWord)
            while guess != word:
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
                    print('Guesses remaining: N/A')
                    print('Word:', word)
                    print(ShowWord)
                    print('Guessed Letters:')
                    for x in guessed:
                        print(' -', x)
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
        if Admin == False:
            Letters = len(word)
            ShowWord = '_' * Letters
            print(ShowWord)
            guess = ''
            NOG = 0
            guessed = []
            while guess != word and NOG <= 7:
                if ShowWord == word:
                    print('YOU GUESSED THE WORD!!!!')
                    Money += 2 * int(Bet)
                    print('Money:',Money)
                    break
                guess = input('Guess a letter, guess the word if you know it: ').lower()
                while guess not in letters and guess != word:
                    guess = input('That is not a valid letter. Choose again: ').lower()
                while guess in guessed:
                    guess = input('You already guessed that letter. Choose again: ').lower()
                if guess == word:
                    print('YOU GUESSED THE WORD!!!!!')
                    Money += 2 * int(Bet)
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
                    print('Guesses remaining:', 13 - NOG)
                    print(ShowWord)
                    print('Guessed Letters:')
                    for x in guessed:
                        print(' -', x)
            if NOG == 13:
                print('You are out of guesses')
                print('The word was:', word)
                Money -= Bet
                print('Money:',Money)
        if Admin == True:
            Letters = len(word)
            ShowWord = '_' * Letters
            print(word)
            print(ShowWord)
            guess = ''
            guessed = []
            while guess != word:
                if ShowWord == word:
                    print('YOU GUESSED THE WORD!!!!')
                    Money += 2 * int(Bet)
                    print('Money:',Money)
                    break
                guess = input('Guess a letter, guess the word if you know it: ').lower()
                while guess not in letters and guess != word:
                    guess = input('That is not a valid letter. Choose again: ').lower()
                while guess in guessed:
                    guess = input('You already guessed that letter. Choose again: ').lower()
                if guess == word:
                    print('YOU GUESSED THE WORD!!!!!')
                    Money += 2 * int(Bet)
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
                    print('Guesses remaining: N/A')
                    print('Word:',word)
                    print(ShowWord)
                    print('Guessed Letters:')
                    for x in guessed:
                        print(' -', x)
            if NOG == 13:
                print('You are out of guesses')
                print('The word was:', word)
                Money -= Bet
                print('Money:',Money)
global Admin
Admin = False
Money = 100000
print('Money: 100000')
print('1.) Low Risk Slots, Risk: 10x')
print('2.) High Risk Slots, Risk: 100x')
print('3.) Dice, Risk: 2-5x')
print('4.) Black Jack, Risk: 2x or 5x')
print('5.) Hangman, Risk: 2-4x')
print('6.) Exit the Casino')
game = input('Select the number of the game you want to play: ')
while game != '6':
    if game == '1':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN != 'yes' and DescriptionYN != 'no':
            while DescriptionYN != 'yes' and DescriptionYN != 'no':
                print('Invalid input')
                DesecriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('When the "LowRiskSlots" window pops up, click anywhere on it to start the slots machine. Once it finishes, if the number on the screen matches the number next to "Winning Number", you won. After the animation, the window will close automatically and tell you how much to won or lost. If you are in full screen mode, exit and click on the "LowRiskSlots" window.')
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        LowRiskSlots(Bet)
        PlayAgainO = input('Do you want to play again? y/n: ')
        while PlayAgainO == 'y':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            LowRiskSlots(Bet)
            PlayAgainO = input('Do you want to play again? y/n: ')
    elif game == '2':
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        HighRiskSlots(Bet)
        PlayAgainT = input('Do you want to play again? y/n: ')
        while PlayAgainT == 'y':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            HighRiskSlots(Bet)
            PlayAgainT = input('Do you want to play again? y/n: ')
    elif game == '3':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN != 'yes' and DescriptionYN != 'no':
            while DescriptionYN != 'yes' and DescriptionYN != 'no':
                print('Invalid input')
                DesecriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('When you start the game, a dice will roll and return a value from 1-6. If that value is 2-6, it is added to your turn score. Then, it asks you if you want to roll again. If you say yes, the process will repeat. If not, your turn score will be added to your overall score. However, if you choose to roll again and roll a 1, the points from your turn get erased and not added to your overall score.')
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        Dice(Bet)
        PlayAgainTh = input('Do you want to play again? y/n: ')
        while PlayAgainTh =='y':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            Dice(Bet)
            PlayAgainTh = input('Do you want to play again? y/n: ')
    elif game == '4':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN != 'yes' and DescriptionYN != 'no':
            while DescriptionYN != 'yes' and DescriptionYN != 'no':
                print('Invalid input')
                DesecriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('At the start of the game, you will be dealt 2 cards. The total of these to cards will be displayed. After that it will ask you if you want to hit (get another card) or stay (stop getting cards). If you choose to hit, you will be dealt another card and it will be added to your score. If you choose to stay, your total will be compared to the House. If your score is larger than theirs and less than or equal to 21, you win. If your score is less than theirs, you lose. If your score is greater than 21, the House automaticaly wins. If your first 2 cards add up to 21, that is Black Jack and you automatically win')
        Bet = int(input('Bet: '))
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        BlackJack(Bet)
        PlayAgainF = input('Do you want to play again? y/n: ')
        while PlayAgainF =='y':
            Bet = int(input('Bet: '))
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            BlackJack(Bet)
            PlayAgainF = input('Do you want to play again? y/n: ')
    elif game == '5':
        DescriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN != 'yes' and DescriptionYN != 'no':
            while DescriptionYN != 'yes' and DescriptionYN != 'no':
                print('Invalid input')
                DesecriptionYN = input('Do you want a description of this game?: ').lower()
        if DescriptionYN == 'yes':
            print('When the game starts, choose if you want to make your own word or select one from a list. If you choose your own word and are in full screen mode, exit and click on the "Hangman Input" window. Once you have entered your word, click anywhere within the window to set it. After that, type your letter guess and then it will tell you if that letter is in the word. You have 7 wrong guesses and once you are out, you lose.') 
        Bet = int(input('Bet: '))
        Hangman(Bet)
        if (Money - Bet) < 0:
            print('Insuficient Funds')
            Bet = int(input('Bet: '))
        PlayAgainFI = input('Do you want to play again? y/n: ')
        while PlayAgainFI == 'y':
            Bet = int(input('Bet: '))
            Hangman(Bet)
            if (Money - Bet) < 0:
                print('Insuficient Funds')
                Bet = int(input('Bet: '))
            PlayAgainFI = input('Do you want to play again? y/n: ')
    elif game == '7':
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
                game = '6'
    if game != '6':
        print('1.) Low Risk Slots, Risk: 10x')
        print('2.) High Risk Slots, Risk: 100x')
        print('3.) Dice, Risk: 2-5x')
        print('4.) Black Jack, Risk: 2x or 5x')
        print('5.) Hangman, Risk: 2-4x')
        print('6.) Exit the Casino')
        game = input('Select the number of the game you want to play: ')
    else:
        pass
if Money < 100000:
    print('Losings:', 100000 - Money)
elif Money > 100000:
    print('Earnings:', Money - 100000) 
