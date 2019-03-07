#!/usr/bin/python3

import itertools, time, sys, random, os
from colorama import Fore,init,Style, Back
init()
if sys.platform == "win32":
    cl = "cls"
else:
    cl = "clear"
os.system(cl)
ranks = ['0','1','2','3','4','5','6','7','8','9','10','switch','block','+2']
color = ['red','yellow','green','blue']
deck = list(itertools.product(ranks,color))
ranks = ['1','2','3','4','5','6','7','8','9','10','switch','block','+2']
deck += list(itertools.product(ranks,color))
deck += [("+4","black"),("+4","black"),("+4","black"),("+4","black"),("Switch Color","black"),("Switch Color","black"),("Switch Color","black"),("Switch Color","black")]
random.shuffle(deck)
mydeck = deck[0:7]
odeck1 = deck[7:14]
odeck2 = deck[14:21]
odeck3 = deck[21:28]
decks = [mydeck,odeck1,odeck2,odeck3]
disc = [deck[28]]
deck = deck[29:]
col = -1
direction = 1

player = 0
debug = False
x=""
options = ["p","P","h","H"]
while x not in options:
    x=input("Play(p|P) or Help(h|H)? ")
if x in options[2:4]:
    print("\nRules of this UNO:\n","1) If a number card is played, the following card")
    print("\tshould contain the same number or have the same color.")
    print("\tA black card is always allowed, even if the player can play.")
    print("2) +2 or +4 cards cannot be stacked, the player is not allowed")
    print("\t to play a card if they had to take 2 or 4 cards")
    print("3) It is allowed to finish with special cards")
    print("4) It is allowed to choose the same color if a color card is played")
    input("\nPress Enter to continue")


def addcards(number):
    if player+direction == 4:
        tempplayer = 0
    elif player+direction == -1:
        tempplayer = 3
    else:
        tempplayer=player+direction
    print("Added {} cards to player {}".format(number,tempplayer+1))
    for i in range(0,number):
        checkpile()
        decks[tempplayer] = decks[tempplayer]+[tuple(deck[0])]
        deck.remove(deck[0])

def printtable():
    print("Table: ", end="")
    if disc[len(disc)-1][1] == "red":
        print(Fore.RED, end="")
    elif disc[len(disc)-1][1] == "green":
        print(Fore.GREEN, end="")
    elif disc[len(disc)-1][1] == "blue":
        print(Fore.BLUE, end="")
    elif disc[len(disc)-1][1] == "yellow":
        print(Fore.YELLOW, end="")
    
    print(disc[len(disc)-1][0],Fore.WHITE)
    if col != -1:
        print("Color: ",end="")
        if col == 0:
            print(Fore.RED, end="")
        elif col == 1:
            print(Fore.YELLOW, end="")
        elif col == 2:
            print(Fore.GREEN, end="")
        else:
            print(Fore.BLUE, end="")
        print(color[col] + Fore.WHITE)
    for i in range(1,5):
        if player+1 == i:
            print(Back.MAGENTA, end="")
        print("Player {}: {}".format(i,len(decks[i-1])),Back.RESET, end='   ')

def playerupdate():
    global player
    player += direction
    if player == 4:
        player=0
    elif player == -1:
        player= 3
    elif player == 5:
        player=1
    elif player == -2:
        player=2

def printdeck():
    count = 0
    for i in decks[0]:
        count +=1
        print("Card {}: ".format(count), end="")
        if i[1] == "red":
            print(Fore.RED, end="")
        elif i[1] == "green":
            print(Fore.GREEN, end="")
        elif i[1] == "blue":
            print(Fore.BLUE, end="")
        elif i[1] == "yellow":
            print(Fore.YELLOW, end="")
        print("{}".format(i[0]), Fore.WHITE)

def grabcard():
    checkpile()
    decks[player] = decks[player]+[tuple(deck[0])]
    deck.remove(deck[0])

def printcard(i):
    print("Player {} played ".format(player+1), end="")
    if i[1] == "red":
        print(Fore.RED, end="")
    elif i[1] == "green":
        print(Fore.GREEN, end="")
    elif i[1] == "blue":
        print(Fore.BLUE, end="")
    elif i[1] == "yellow":
        print(Fore.YELLOW, end="")
    print("{}".format(i[0]), Fore.WHITE)

def checkpile():
    global deck
    if len(deck) == 0:
        deck = disc[0:len(disc)]
        random.shuffle(deck)
        disc = disc[len(disc)-1]
        print("Reshuffled the discarded cards!")

def checkUNO():
    if len(decks[player]) == 1:
        print(Back.CYAN+"UNO!"+Back.RESET)

if disc[0][1] == "black":
    col = -1
    printdeck()
    print("Table: ",disc[len(disc)-1])
    while col not in range(0,3):
        col = int(input("What color should be played next? \n Red = 1 \n Yellow = 2 \n Green = 3 \n Blue = 4 \n"))
        try:
            int(col)
            col = col-1
        except ValueError:
            col = -1
    os.system(cl)
    


while len(decks[0])>0 and len(decks[1])>0 and len(decks[2])>0 and len(decks[3])>0:
    if player == 0:
        #Player itself
        invalmov = True
        while invalmov:
            invalmov = False
            printtable()
            print("\nMy Deck:")
            printdeck()
            x=-1
            while int(x) not in range(0,len(decks[0])+1):
                x = input("Card to play (number), or take card(0): ")
                try:
                    int(x)
                except ValueError:
                    x = -1
            x = int(x)
            os.system(cl)
            disccard = disc[len(disc)-1]
            
            if x == 0:
                haspossiblemove=False
                for card in decks[0]:
                    if card[0] == disccard[0] or card[1] == disccard[1] or card[1] == "black":
                        haspossiblemove = True
                    if col != -1:
                        if card[1] == color[col]:
                            haspossiblemove = True
                if haspossiblemove == True:
                    print("You can play a card!")
                    invalmov=True
                else:
                    #print(decks[0])
                    grabcard()
            elif decks[0][x-1][0] == disccard[0] or decks[0][x-1][1] == disccard[1] or (decks[0][x-1][1] == color[col] and col != -1) :
                col = -1
                disc += [tuple(decks[0][x-1])]
                if decks[0][x-1][0] == "switch":
                    direction *= -1
                decks[0].remove(decks[0][x-1])
                checkUNO()
                if disc[len(disc)-1][0] == "+2":
                    addcards(2)
                    player += direction
                if disc[len(disc)-1][0] == "block":
                    player += direction
                
            elif decks[0][x-1][1] == "black":

                disc += [tuple(decks[0][x-1])]
                decks[0].remove(decks[0][x-1])
                if disc[len(disc)-1][0] == "+4":
                    addcards(4)
                    checkUNO()
                    player += direction
                printdeck()
                col = -1
                while col not in range(0,4):
                    col = int(input("What color should be played next? \n Red = 1 \n Yellow = 2 \n Green = 3 \n Blue = 4 \n"))
                    try:
                        int(col)
                        col = col-1
                    except ValueError:
                        col = -1
                os.system(cl)
            else:
                invalmov = True
                print("Not a valid move!")
        else:
            playerupdate()
    else:
        #other players
        printtable()
        
        print("\nPlayer {} is thinking".format(player+1),end="")
        if debug == True:
            print(decks[player])
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".",end="")
        os.system(cl)
        for card in decks[player][:]:
            if col != -1:
                #print(card, color[col])
                if card[1] == color[col]:
                    printcard(card)
                    col = -1
                    disc += [card]
                    decks[player].remove(card)
                    checkUNO()
                    break
            elif card[0] == disc[len(disc)-1][0] or card[1] == disc[len(disc)-1][1]:
                #print(card, player)
                printcard(card)
                col = -1
                disc += [card]
                if card[0] == "switch":
                    direction *= -1
                decks[player].remove(card)
                checkUNO()
                if disc[len(disc)-1][0] == "+2":
                    addcards(2)
                    player += direction
                if disc[len(disc)-1][0] == "block":
                    player += direction
                break
            
            if card[1] == "black":
                printcard(card)
                #print("black card")
                col = random.randint(0,3)
                disc += [tuple(card)]
                decks[player].remove(card)
                if disc[len(disc)-1][0] == "+4":
                    addcards(4)
                    checkUNO()
                    player += direction
                break
        else:
            grabcard()
            print("Player {} took a card!".format(player+1))
        
        playerupdate()
        
else:
    if len(decks[0])==0:
        win = "Congratulations! you win!"
    elif len(decks[1])==0:
        win = "Player 2 wins!"
    elif len(decks[2])==0:
        win = "Player 3 wins!"
    elif len(decks[3])==0:
        win = "Player 4 wins!"
    cols = [Back.YELLOW,Back.BLUE,Back.CYAN,Back.GREEN,Back.MAGENTA,Back.RED,Back.BLACK]
    for i in win:
        print(i,end="")
    for j in range(1,20):
        for i in range(1,20):
            print(cols[random.randint(0,len(cols)-1)], end = "")
        print("")
