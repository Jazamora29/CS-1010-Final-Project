from tkinter import *
from random import *

#Attributes of the tkinter window. Such as title and geometry or the size of the window.
mainwindow = Tk()
mainwindow.title("Poker")
mainwindow.geometry("800x450")

mainwindow.columnconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=1)

#Functions used as abstraction for making the code smaller.
#We call the showRed function when the button 'red' is pressed.
#And so on and so forth for the other colors. 
def showRed():
    redFrame.tkraise()

def showGreen():
    greenFrame.tkraise()

def showBlue():
    blueFrame.tkraise()

# bottom Frame ----------------------------------------------------
bottom_frame = Frame(mainwindow, bg="yellow", padx=5, pady=5)
bottom_frame.grid_propagate(False)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)


# green Frame ----------------------------------------------------
greenFrame = Frame(bottom_frame, bg="#228B22", padx=5, pady=5)
greenFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)
greenFrame

#Entry Box code---------------------------------------------------
L1 = Label(greenFrame,font=('times new roman', 15), text = "Add Money")
L1.grid(row=0, column=0, padx=(50), pady=30)
L1.grid_columnconfigure(0, weight=2)

E1 = Entry(greenFrame,font=('times new roman', 15))
E1.grid(row=0, column=1, padx=(50), pady=30)
E1.grid_columnconfigure(0, weight=2)

def changeMoney():
    global money
    if(E1.get().isnumeric()):
        money += int(E1.get())
        L1.configure(text = "Add Money")
        update()
    else:
        L1.configure(text = "Text must be numeric")

B1 = Button(greenFrame,font=('times new roman', 15), text="Submit", command= changeMoney)
B1.grid(row=0, column=2, padx=(50), pady=30)
B1.grid_columnconfigure(0, weight=2)

#---------

L2 = Label(greenFrame,font=('times new roman', 15), text = "Random%")
L2.grid(row=1, column=0, padx=(50), pady=30)
L2.grid_columnconfigure(1, weight=2)

E2 = Entry(greenFrame,font=('times new roman', 15))
E2.grid(row=1, column=1, padx=(50), pady=30)
E2.grid_columnconfigure(1, weight=2)

def changeRand():
    global rand
    if(E2.get().isnumeric()):
        if(int(E2.get()) <= 100 or int(E2.get) >= 0):
            rand = int(E2.get())
            L2.configure(text = "Money")
            print("Random is now: " + str(rand))
            update()
        else:
            L2.configure(text = "Number must be from 1 to 100")
    else:
        L2.configure(text = "Text must be numeric")

B2 = Button(greenFrame,font=('times new roman', 15),text="Submit", command=changeRand)
B2.grid(row=1, column=2, padx=(50), pady=30)
B2.grid_columnconfigure(1, weight=2)

#----------

L3 = Label(greenFrame,font=('times new roman', 15), text = "Ante")
L3.grid(row=2, column=0, padx=(50), pady=30)
L3.grid_columnconfigure(1, weight=2)

E3 = Entry(greenFrame, font=('times new roman', 15))
E3.grid(row=2, column=1, padx=(50), pady=30)
E3.grid_columnconfigure(1, weight=2)

def changeAnte():
    global ante
    if(E3.get().isnumeric):
        ante = int(E3.get())
        print("Ante is now: " + str(ante))
        L3.configure(text = "Ante")
    else:
        L3.configure(text = "Text must be numeric")
B3 = Button(greenFrame,font=('times new roman', 15), text="Submit", command=changeAnte)
B3.grid(row=2, column=2, padx=(50), pady=30)
B3.grid_columnconfigure(1, weight=2)
#------------------------------------------------------------------

btn_r3 = Button(greenFrame, fg="red", text='Menu', width='5', command=showRed)
btn_r3.place(x=0, y=385)

btn_b3 = Button(greenFrame, fg="green", text='Table', width='5', command=showBlue)
btn_b3.place(relx=1.0, y=385, anchor=(NE))


# blue Frame ----------------------------------------------------
blueFrame = Frame(bottom_frame, bg="#228B22", padx=5, pady=5)
blueFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

btn_g4 = Button(blueFrame, fg="green", text='Settings', width='5', command=showGreen)
btn_g4.place(x=0, rely=1.0, anchor=(SW))

btn_r4 = Button(blueFrame, fg="red", text='Menu', width='5', command=showRed)
btn_r4.place(relx=1.0, rely=1.0, anchor=(SE))

parval  =  [14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13]#a parallel array storing card value
parsuit =  [1 ,1,1,1,1,1,1,1,1,1 ,1 ,1 ,1 ,2 ,2,2,2,2,2,2,2,2,2 ,2 ,2 ,2 ,3 ,3,3,3,3,3,3,3,3,3 ,3 ,3 ,3 ,4 ,4,4,4,4,4,4,4,4,4 ,4 ,4 ,4 ]#a parallel array storing suit, I use spaces to line both up visually
disc =     [False, False, False, False, False]#an array that stores booleans for the discard portion
slotval =  [-1, -1, -1, -1, -1]#a parallel array that stores the values for the user's hand
slotsuit = [-1, -1, -1, -1, -1]#a parallel array that stores the suits for the user's hand
userHand = [-1, -1]#this will interpret the user's hand and find highcard, [hand, highcard]
compHand = [-1, -1]#this will interpret the computer's hand and find highcard, [hand, highcard]
money = 1000#stores user money count, I let you spend money you don't have so it may be negative
compmoney = 1000#stores the comp money count and I also let them spend money they don't have
ante = 50#the starting bet, also acts as the increment for raising or lowering a bet
bet = 0#this stores the current bet that is proposed to be added to the pool
pool = 0#this is the money in the pool that the winner will win
num = -1#this is the stage of the game we are in
game = False#this is a boolean on if we are in the game or not
rand = 20#this is a number from 1 to 100 that will determine how often the computer does an alternative action
hold = False#this boolean turns true when the computer raises the user and returns false after the user makes their decision
rais = 0#this is the proposed raise from the computer
discarded = False#this is a boolean that turns true once you have discarded your cards, you can only discard your cards once per match

def stop(fold):#we call this when we want to reset and start a new game.
    global img, parval, parsuit, disc, slotval, slotsuit, money, compmoney, bet, pool, num, game, hold, rais, discarded
    num = -1
    parval  = [14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13]
    parsuit = [1 ,1,1,1,1,1,1,1,1,1 ,1 ,1 ,1 ,2 ,2,2,2,2,2,2,2,2,2 ,2 ,2 ,2 ,3 ,3,3,3,3,3,3,3,3,3 ,3 ,3 ,3 ,4 ,4,4,4,4,4,4,4,4,4 ,4 ,4 ,4 ]
    disc = [False, False, False, False, False]
    slotval = [-1, -1, -1, -1, -1]
    slotsuit = [-1, -1, -1, -1, -1]
    if(fold):#if the player folds we want to give the pool to the computer and then get back the bet money as that hasn't joined the pool yet
        money += bet
        compmoney += pool
        label.configure(text = "You Folded")
    bet = 0
    pool = 0
    num = -1
    game = False
    hold = False
    rais = 0
    discarded = False
    total.configure(text = ("Your Balance: " + str(money)))
    botal.configure(text = ("Current Bet: " + str(bet)))
    mid.configure(text = ("Current Pool: " + str(pool)))
    comp.configure(text = ("Computer Balance : " + str(compmoney)))
    slot1.config(image = img[0])
    slot2.config(image = img[0])
    slot3.config(image = img[0])
    slot4.config(image = img[0])
    slot5.config(image = img[0])

def update():#updates the balance, bet, pool and computer balance
    total.configure(text = ("Your Balance: " + str(money)))
    botal.configure(text = ("Current Bet: " + str(bet)))
    mid.configure(text = ("Current Pool: " + str(pool)))
    comp.configure(text = ("Computer Balance : " + str(compmoney)))

def drawCard(num):#we draw a card, to make sure it is random we shuffle before drawing the new one and creating it
    shuffle()
    shuffle()
    global parval, parsuit
    createCard(parval[0], parsuit[0], num)
    parval.pop(0)#here we make sure the parallel arrays stay parallel when we remove the top card
    parsuit.pop(0)
    
def createCard(val, suit, num):#create's card and displays it
    global img, slotval, slotsuit
    if(suit == 1):#reads the suit variable and interprets it as a string
        strsuit = "clubs"
    elif(suit == 2):
        strsuit = "diamonds"
    elif(suit == 3):
        strsuit = "hearts"
    elif(suit == 4):
        strsuit = "spades"
    else:
        strsuit = "hearts"

    if(val == 14):#reads the val variable and interprets it as a string
        strval = "ace"
    elif(val == 2):
        strval = "2"
    elif(val == 3):
        strval = "3"
    elif(val == 4):
        strval = "4"
    elif(val == 5):
        strval = "5"
    elif(val == 6):
        strval = "6"
    elif(val == 7):
        strval = "7"
    elif(val == 8):
        strval = "8"
    elif(val == 9):
        strval = "9"
    elif(val == 10):
        strval = "10"
    elif(val == 11):
        strval = "jack"
    elif(val == 12):
        strval = "queen"
    elif(val == 13):
        strval = "king"
    else:
        strval = "ace"
    #we create the file name of the card which will be in the folder
    name = strval + "_of_" + strsuit + ".png"
    #num tells us which slot to display the image on, we also update the slot value and suit
    if(num == 1):
        img[1] = PhotoImage(file= name).subsample(4)
        slotval[0] = val
        slotsuit[0] = suit
    elif(num == 2):
        img[2] = PhotoImage(file= name).subsample(4)
        slotval[1] = val
        slotsuit[1] = suit
    elif(num == 3):
        img[3] = PhotoImage(file= name).subsample(4)
        slotval[2] = val
        slotsuit[2] = suit
    elif(num == 4):
        img[4] = PhotoImage(file= name).subsample(4)
        slotval[3] = val
        slotsuit[3] = suit
    elif(num == 5):
        img[5] = PhotoImage(file= name).subsample(4)
        slotval[4] = val
        slotsuit[4] = suit
    
def shuffle():#pretty simple, randomly select an index and put it in a new index, repeat 25 times
    global parval, parsuit
    num = 0
    while num <= 25:
        stor1 = randint(0,len(parval)-1)
        stor2 = parval.pop(stor1)#we make sure to keep the arrays parallel
        stor3 = parsuit.pop(stor1)
        stor1 = randint(0,51)
        parval.insert(stor1, stor2)
        parsuit.insert(stor1, stor3)
        num += 1

def discard(num):#discard cards for the discard phase, or if you chose to undo a discard.
    global disc, img
    #disc checks if that slot is ready to switch, ie it's the discard round and you haven't already discarded that slot
    #if you are able to discard, we change the image to the joker card to indicate that it is ready
    #if you already discarded that slot, we make it so you redisplay the card and so that the code recognized not to discard that card
    #we also check if discarded is false because if we already did the discard portion we don't want to be able to click cards and flip them
    #lastly, num is used to indicate which slot we are working on
    if(num == 1 and disc[0] == True and not discarded):
        slot1.config(image = img[0])
        disc[0] = False
    elif(num == 2 and disc[1] == True and not discarded):
        slot2.config(image = img[0])
        disc[1] = False
    elif(num== 3 and disc[2] == True and not discarded):
        slot3.config(image = img[0])
        disc[2] = False
    elif(num == 4 and disc[3] == True and not discarded):
        slot4.config(image = img[0])
        disc[3] = False
    elif(num == 5 and disc[4] == True and not discarded):
        slot5.config(image = img[0])
        disc[4] = False
    elif(num == 1 and disc[0] == False and not discarded):
        slot1.config(image = img[1])
        disc[0] = True
    elif(num == 2 and disc[1] == False and not discarded):
        slot2.config(image = img[2])
        disc[1] = True
    elif(num== 3 and disc[2] == False and not discarded):
        slot3.config(image = img[3])
        disc[2] = True
    elif(num == 4 and disc[3] == False and not discarded):
        slot4.config(image = img[4])
        disc[3] = True
    elif(num == 5 and disc[4] == False and not discarded):
        slot5.config(image = img[5])
        disc[4] = True    

def start():#this is the start function to start a new game
    global money, compmoney, bet, pool, game, num
    if(game == False):#we check if we are not in a game, if not we do below actions
        money -= ante#money is taken from user and computer to add to the pool, this is called the Ante
        compmoney -=ante
        pool += ante*2
        label.configure(text = "Bet")#tells the user to now bet  as they are given cards
        update()#updates to display info
        drawCard(1)#draw cards for each slot
        drawCard(2)
        drawCard(3)
        drawCard(4)
        drawCard(5)
        sortHand()#sort the hand
        game = True#change game boolean to true and num to zero so we are ready to move on
        num = 0
    elif(game):#if we are in a game we tell the user that they are in a game already
        label.configure(text = "You are in a game~")

def rai():#a functionto raise the bet, unlike real life I will let you spend money you don't have
    global money, bet
    #checks that you are in a game
    #also we check if you are currently being held by the computer raising your bet
    #in this case we don't want to be able to change the bet because I believe you can't counter raise
    if(game == True and not (bet == rais and hold)):#if above conditions are met, we take from money and add it to bet and update
        money -= ante
        bet += ante
        update()
    elif(bet == rais and hold):#if we are being held by a raise, we tell the user to match or fold
        label.configure(text = "You must match or fold the raise")
    elif(game != False):#if we get here we know that the game hasn't started
        label.configure(text = "Start the game")

def lows():#just like the one above, but we lower the bet
    global money, bet
    #we check if there is even money in bet
    #also checks that you are in a game
    #also we check if you are currently being held by the computer raising your bet
    #in this case we don't want to be able to change the bet because I believe you can't counter raise 
    if(bet >= ante and game == True and not (bet == rais and hold)):#if above conditions are met, we take from bet and add it to money and edit
        bet -= ante
        money += ante
        total.configure(text = ("Your Balance: " + str(money)))
        botal.configure(text = ("Current Bet: " + str(bet)))
    elif((bet == rais and hold)):#if we are being held by a raise, we tell the user to match or fold
        label.configure(text = "You must match or fold the raise")
    elif(game != False):#if we get here we know that the game hasn't started
        label.configure(text = "Start the game")

def winner():#return 0 for computer, 1 for user and 2 for tie
    intHand()#interprets user's hand
    #first we compare which hand is better, if they tie we compare the high card, and if those tie as well then it is a tie
    #the computer uses a seperate deck so it is possible for a tie
    if(compHand[0] > userHand[0]):
        return 0
    elif(compHand[0] < userHand[0]):
        return 1
    elif(compHand[1] > userHand[1]):
        return 0
    elif(compHand[1] < userHand[1]):
        return 1
    else:
        return 2

def sortHand():#sorts the user's hand
    global slotsuit, slotval, img
    #insertion sort: https://realpython.com/sorting-algorithms-python/
    for i in range(1, len(slotval)):
        key = slotval[i]
        keys = slotsuit[i]
        j = i - 1
        while(j >= 0 and slotval[j] > key):
            slotval[j + 1] = slotval[j]
            slotsuit[j + 1] = slotsuit[j]
            j -= 1
        slotval[j + 1] = key
        slotsuit[j + 1] = keys
    #after the sort we create the card so the image is stored, then display the image
    createCard(slotval[0], slotsuit[0], 1)
    slot1.config(image = img[1])
    createCard(slotval[1], slotsuit[1], 2)
    slot2.config(image = img[2])
    createCard(slotval[2], slotsuit[2], 3)
    slot3.config(image = img[3])
    createCard(slotval[3], slotsuit[3], 4)
    slot4.config(image = img[4])
    createCard(slotval[4], slotsuit[4], 5)
    slot5.config(image = img[5])

def drawComp():#we draw a hand for the computer
    #probabilities gotten from wikipedia: https://en.wikipedia.org/wiki/Poker_probability#
    #also the high card probability isn't right, I just don't want to do the math because I can't find it online
    global compHand
    hand = randint(1, 2598960)
    if(hand <= 4):#royal flush
        compHand[0] = 10
        compHand[1] = 14#royal flush always has an ace
    elif(hand <= 36):#straight flush
        compHand[0] = 9
        compHand[1] = randint(6, 14)#since this is 5 in a row I know the high card is atleast 6
    elif(hand <= 624):#four of a kind
        compHand[0] = 8
        compHand[1] = randint(2, 14)
    elif(hand <= 3744):#full houes
        compHand[0] = 7
        compHand[1] = randint(2, 14)
    elif(hand <= 5108):#flush
        compHand[0] = 6
        compHand[1] = randint(2, 14)
    elif(hand <= 10200):#straight
        compHand[0] = 5
        compHand[1] = randint(6, 14)#since this is 5 in a row I know the high card is atleast 6
    elif(hand <= 54912):#three of a kid
        compHand[0] = 4
        compHand[1] = randint(2, 14)
    elif(hand <= 123552):#two pairs
        compHand[0] = 3
        compHand[1] = randint(2, 14)
    elif(hand <= 1098240):#one pair
        compHand[0] = 2
        compHand[1] = randint(2, 14)
    else:#high card only
        compHand[0] = 1
        compHand[1] = randint(2, 14)

def intHand():#interprets user's hand
    global userHand
    #checks for straight
    straight = False
    flow = False#checks if the cards flow over from ace back to 2(technically king to ace but I wrote ace with a value of 14)
    count = 0#determines how many skips occur
    if(slotval[0] == 2 and slotval[4] == 14):#if a "flow" happened the first card once sorted would be a 2 and the last an ace
        flow = True
    for i in range(0, len(slotval) - 1):#for each slot
        if(slotval[i] != (slotval[i + 1] -1)):#if this position isn't equal to the next position minus 1 then there was a skip, count + 1
            count += 1
    if(count == 0 or (flow and count == 1)):#at the end we check that count is 0, or 1 if flow is true
        straight = True
    
    #checks for flush
    flush = (slotsuit[0] == slotsuit[1] == slotsuit[2] == slotsuit[3] == slotsuit[4])

    #royal flush is a straight flush from 10 to Ace to I check for straight, flush and for an 10 and ace, and high card is always ace
    if(flush and straight and slotval[0] == 10 and slotval[4] == 14):
        userHand[0] = 10
        userHand[1] = 14
    #I check for straight and flush, high card should be at the end
    elif(flush and straight):
        userHand[0] = 9
        userHand[1] = slotval[4]
    #I check for a 4 of a kind, and I know the middle card has to be part of it since it is sorted so I can use it for the high card
    elif((slotval[0] == slotval[1] == slotval[2] == slotval[3]) or (slotval[1] == slotval[2] == slotval[3] == slotval[4])):
        userHand[0] = 8
        userHand[1] = slotval[2]
    #for a full house I know the left 2 and right 2 must match eachother, and the middle must match either
    #since the middle is part of the 3 of a kind I know it is the value of the high card
    elif((slotval[0] == slotval[1]) and (slotval[3] == slotval[4]) and (slotval[0] == slotval[2] or slotval[4] == slotval[2])):
        userHand[0] = 7
        userHand[1] = slotval[2]
    #since a flush is the same suit I just check for that and the furthest right card is the high card as it is sorted
    elif(flush):
        userHand[0] = 6
        userHand[1] = slotval[4]
    #Straight logic is already calculated, I know the furthest right card is a high since it is sorted
    elif(straight):
        userHand[0] = 5
        userHand[1] = slotval[4]
    #three of a kind has 3 locations once sorted, and the middle card is always included so that is the high card
    elif((slotval[0] == slotval[1] == slotval[2]) or (slotval[1] == slotval[2] == slotval[3]) or (slotval[2] == slotval[3] == slotval[4])):
        userHand[0] = 4
        userHand[1] = slotval[2]
    #two pairs have 3 possible locations and each one has the high card in slot 4
    elif((slotval[0] == slotval[1] and (slotval[3] == slotval[2] or slotval[3] == slotval[4]) or (slotval[1] == slotval[2] and slotval[3] == slotval[4]))):
        userHand[0] = 3
        userHand[1] = slotval[3]
    #one pair has 4 possible locations, I split them in half to make it easier to find the high card
    elif(slotval[0] == slotval[1] or slotval[1] == slotval[2]):
        userHand[0] = 2
        userHand[1] = slotval[1]
    elif(slotval[2] == slotval[3] or slotval[3] == slotval[4]):
        userHand[0] = 2
        userHand[1] = slotval[3]
    #we are at the end now, no hands were made so the highest card is all that is left
    else:
        userHand[0] = 1
        userHand[1] = slotval[4]

def compLogic():#return 0 to fold, 1 to match, 2 small raise, 3 big raise
    num = winner()
    risk = randint(1, 100)
    #the logic is arbitrary so if it plays bad, its because I'm bad at poker
    if(bet > 2*ante):#intimidated computer
        if(num == 0 and compHand[0] >= 5):#winning with good hand
            if(risk <= int(rand/4)):
                return 0
            elif(risk <= rand):
                return 1
            else:
                return 2
        elif(num == 0):#winning
            if(risk <= int(rand/4)):
                return 2
            elif(risk <= rand):
                return 0
            else:
                return 1
        elif(num == 1 and userHand[0] <= 2):#losing to bad hand
            if(risk <= int(rand/4)):
                return 2
            elif(risk <= rand):
                return 1
            else:
                return 0
        elif(num == 1):#losing to a decent hand
            if(risk <= int(rand/2)):
                return 1
            else:
                return 0
        elif(num == 2 and compHand[0] <= 2):#tied to a bad hand
            if(risk <= int(rand/4)):
                return 2
            elif(risk <= rand):
                return 0
            else:
                return 1
        elif(num == 2):#tied
            if(risk <= int(rand/4)):
                return 2
            elif(risk <= rand):
                return 1
            else:
                return 0
    
    elif(bet > ante):#conflicted computer
        if(num == 0 and compHand[0] >= 5):#winning with good hand
            if(risk <= int(rand/4)):
                return 3
            elif(risk <= rand):
                return 1
            else:
                return 2
        elif(num == 0):#winning
            if(risk <= int(rand/4)):
                return 0
            elif(risk <= rand):
                return 2
            else:
                return 1
        elif(num == 1 and userHand[0] <= 2):#losing to bad hand
            if(risk <= int(rand/4)):
                return 3
            elif(risk <= rand):
                return 0
            else:
                return 1
        elif(num == 1):#losing to a decent hand
            if(risk <= rand):
                return 2
            else:
                return 0
        elif(num == 2 and compHand[0] <= 2):#tied to a bad hand
            if(risk <= int(rand/4)):
                return 0
            elif(risk <= rand):
                return 2
            else:
                return 1
        elif(num == 2):#tied
            if(risk <= int(rand/4)):
                return 0
            elif(risk <= rand):
                return 2
            else:
                return 1

    elif(bet > 0):#Normal computer
        if(num == 0 and compHand[0] >= 5):#winning with good hand
            if(risk <= int(rand/4)):
                return 1
            elif(risk <= rand):
                return 2
            else:
                return 3
        elif(num == 0):#winning
            if(risk <= int(rand/4)):
                return 3
            elif(risk <= rand):
                return 2
            else:
                return 1
        elif(num == 1 and userHand[0] <= 2):#losing to bad hand
            if(risk <= int(rand/4)):
                return 3
            elif(risk <= rand):
                return 0
            else:
                return 1
        elif(num == 1):#losing to a decent hand
            if(risk <= int(rand/4)):
                return 2
            elif(risk <= rand):
                return 1
            else:
                return 0
        elif(num == 2 and compHand[0] <= 2):#tied to a bad hand
            if(risk <= rand):
                return 2
            else:
                return 1
        elif(num == 2):#tied
            if(risk <= int(rand/4)):
                return 3
            elif(risk <= rand):
                return 2
            else:
                return 1

    else:#computer given a check
        if(compHand[0] == 1):
            if(risk <= rand):
                return 2
            else:
                return 1
        elif(compHand[0] >= 5):
            if(risk <= rand):
                return 1
            else:
                return 2
        else:
            return 1

def printComp():#this prints what the computer had in the terminal if the user is curious
    big = str(compHand[1])
    if(compHand[1] == 14):#checks for Ace King Queen or Jack as the rest are the value itself
        big = "Ace"
    elif(compHand[1] == 13):
        big = "King"
    elif(compHand[1] == 12):
        big = "Queen"
    elif(compHand[1] == 11):
        big = "Jack"

    if(compHand[0] == 10):#chekcs for each hand and tells the user what the computer had in the terminal
        print("Computer Had a Royal Flush")
    elif(compHand[0] == 9):
        print("Computer Had a Straight Flush With a High Card Of " + big)
    elif(compHand[0] == 8):
        print("Computer Had a Four of a Kind With a High Card Of " + big)
    elif(compHand[0] == 7):
        print("Computer Had a Full House With a High Card Of " + big)
    elif(compHand[0] == 6):
        print("Computer Had a Flush With a High Card Of " + big)
    elif(compHand[0] == 5):
        print("Computer Had a Straight With a High Card Of " + big)
    elif(compHand[0] == 4):
        print("Computer Had a Three of a Kind With a High Card Of " + big)
    elif(compHand[0] == 3):
        print("Computer Had a Two Pair With a High Card Of " + big)
    elif(compHand[0] == 2):
        print("Computer Had a Pair With a High Card Of " + big)
    elif(compHand[0] == 1):
        print("Computer Had Nothing With a High Card Of " + big)        

def printUser():#this prints the user's hand in the computer to compare
    big = str(userHand[1])
    if(userHand[1] == 14):#checks for Ace King Queen or Jack as the rest are the value itself
        big = "Ace"
    elif(userHand[1] == 13):
        big = "King"
    elif(userHand[1] == 12):
        big = "Queen"
    elif(userHand[1] == 11):
        big = "Jack"

    if(userHand[0] == 10):#chekcs for each hand and tells the user what they had in the terminal
        print("You Had a Royal Flush")
    elif(userHand[0] == 9):
        print("You Had a Straight Flush With a High Card Of " + big)
    elif(userHand[0] == 8):
        print("You Had a Four of a Kind With a High Card Of " + big)
    elif(userHand[0] == 7):
        print("You Had a Full House With a High Card Of " + big)
    elif(userHand[0] == 6):
        print("You Had a Flush With a High Card Of " + big)
    elif(userHand[0] == 5):
        print("You Had a Straight With a High Card Of " + big)
    elif(userHand[0] == 4):
        print("You Had a Three of a Kind With a High Card Of " + big)
    elif(userHand[0] == 3):
        print("You Had a Two Pair With a High Card Of " + big)
    elif(userHand[0] == 2):
        print("You Had a Pair With a High Card Of " + big)
    elif(userHand[0] == 1):
        print("You Had Nothing With a High Card Of " + big)
    
def cont():#this is where the game progresses
    global disc, money, compmoney, bet, pool, num, game, hold, rais, discarded
    if(num == 0):#after clicking draw you are shown 5 bets, when ready to bet we go here
        drawComp()#gives the computer their hand
        curr = compLogic()#runs the logic and stores the output
        if(hold):#if the user was raised and we get here they matched, the alternative is the fold button
            label.configure(text = "You Match, Now Discard")
            pool += bet
            bet = 0
            num += 1
            hold = False
            disc[0] = True
            disc[1] = True
            disc[2] = True
            disc[3] = True
            disc[4] = True
        else:#if there wasn't a raise then we know the computer has to make a decision
            if(curr == 0):#computer wants to fold
                label.configure(text = "Computer Folds")#tell the user this
                money += bet + pool#add pool and bet to money
                printComp()#print the hands into the terminal
                printUser()
                stop(False)#stops the game and resets
            elif(curr == 1):#computer matches
                label.configure(text = "Computer Matches, Now Discard")#tells the user
                compmoney -= bet#takes away the bet from computer's money
                pool += bet*2#adds the bet money to the pool from both players
                bet = 0#resets the bet total
                hold = False#makes sure the hold is false for the next round
                num += 1#increases num to get to the next stage
                disc[0] = True#changes these all to true so we can discard by clicking the cards
                disc[1] = True
                disc[2] = True
                disc[3] = True
                disc[4] = True
            elif(curr == 2):#computer wants to do a small raise
                label.configure(text = "Computer Raises a Little Bit")#tells the user
                bet += ante#adds money to bet
                rais = bet#sets raise to the new bet so the user can't counter raise or lower the raise
                compmoney -= bet#takes bet money from computer total
                pool += bet#adds that money to the pool
                money -= ante#takes money from user, but this was put in the bet part so you can fold and get your money back
                hold = True#makes sure the hold is false for the next round
            elif(curr == 3):#computer wants to do a big raise
                label.configure(text = "Computer Raises a Lot")
                bet += 2*ante#adds money to bet
                rais = bet#sets raise to the new bet so the user can't counter raise or lower the raise
                compmoney -= bet#takes bet money from computer total
                pool += bet#adds that money to the pool
                money -= 2*ante#takes money from user, but this was put in the bet part so you can fold and get your money back
                hold = True#makes sure the hold is false for the next round
        update()
    elif(num == 1):#we are now in the discard portion
        if(discarded == False):#if we haven't discarded already, we can discard
            if(disc[0] == False):
                drawCard(1)
            if(disc[1] == False):
                drawCard(2)
            if(disc[2] == False):
                drawCard(3)
            if(disc[3] == False):
                drawCard(4)
            if(disc[4] == False):
                drawCard(5)
            sortHand()
            discarded = True#changes this to true so the computer knows we already discarded
        if(winner() != 0):#if the computer is losing they draw a new hand
            drawComp()
        num += 1#move to the next section
        label.configure(text = "You Have New Cards, Bet")#tells the user to bet
    elif(num == 2):#with new cards we do another round of betting
        curr = compLogic()#runs logic and stores the outcome
        if(hold):#if the user was raised and we get here they matched, the alternative is the fold button
            label.configure(text = "You Match, Click Continue")
            pool += bet
            bet = 0
            num += 1
            hold = False
        else:#if there wasn't a raise then we know the computer has to make a decision
            if(curr == 0):#computer wants to fold
                label.configure(text = "Computer Folds")#tell the user this
                money += bet + pool#add pool and bet to money
                printComp()#print the hands into the terminal
                printUser()
                stop(False)#stops the game and resets
            elif(curr == 1):#computer matches
                label.configure(text = "Computer Matches, click Continue")#tells the user
                compmoney -= bet#takes away the bet from computer's money
                pool += bet*2#adds the bet money to the pool from both players
                bet = 0#resets the bet total
                hold = False#makes sure the hold is false for the next round
                num += 1#increases num to get to the next stage
            elif(curr == 2):#computer wants to do a small raise
                label.configure(text = "Computer Raises a Little Bit")#tells the user
                bet += ante#adds money to bet
                rais = bet#sets raise to the new bet so the user can't counter raise or lower the raise
                compmoney -= bet#takes bet money from computer total
                pool += bet#adds that money to the pool
                money -= ante#takes money from user, but this was put in the bet part so you can fold and get your money back
                hold = True#makes sure the hold is false for the next round
            elif(curr == 3):#computer wants to do a big raise
                label.configure(text = "Computer Raises a Lot")
                bet += 2*ante#adds money to bet
                rais = bet#sets raise to the new bet so the user can't counter raise or lower the raise
                compmoney -= bet#takes bet money from computer total
                pool += bet#adds that money to the pool
                money -= 2*ante#takes money from user, but this was put in the bet part so you can fold and get your money back
                hold = True#makes sure the hold is false for the next round
        update()
    elif(num == 3):#now we check for the winner
        result = winner()#stores the result
        if(result == 0):#if computer wins, we tell the user and give money to computer
            label.configure(text = "you lose")
            compmoney += pool
        elif(result == 1):#if the user wins, we tell the user and give them the money
            label.configure(text = "You win")
            money += pool
        else:#if it is a tie the money is splot
            label.configure(text = "You tie")
            money += pool/2
            compmoney += pool/2
        printComp()#prints the hands
        printUser()
        stop(False)#resets
        update()#updates the test

#I used grids to make it look nice, though I can't find out how to center it all in the frame
pic = PhotoImage(file="black_joker.png").subsample(4)#we create an image for black joker, which is a blank slot
img = [pic, pic, pic, pic, pic, pic]#we use an array of images to make it easier on the eyes
#we make buttons for the 5 cards and give them the black joker image for now
#we want buttons so when we discard you just click the card you want to discard
slot1 = Button(blueFrame, image = img[0], borderwidth=0, command = lambda: discard(1))
slot1.grid(row = 2, column = 1, padx=5, pady=5)
slot2 = Button(blueFrame, image = img[0], borderwidth=0, command = lambda: discard(2))
slot2.grid(row = 2, column = 2, padx=5, pady=5)
slot3 = Button(blueFrame, image = img[0], borderwidth=0, command = lambda: discard(3))
slot3.grid(row = 2, column = 3, padx=5, pady=5)
slot4 = Button(blueFrame, image = img[0], borderwidth=0, command = lambda: discard(4))
slot4.grid(row = 2, column = 4, padx=5, pady=5)
slot5 = Button(blueFrame, image = img[0], borderwidth=0, command = lambda: discard(5))
slot5.grid(row = 2, column = 5, padx=5, pady=5)
#the draw button will draw 5 cards and start the game
strt = Button(blueFrame, text = "Draw", command= lambda: start())
strt.grid(row = 4, column = 1, padx=5, pady=5)
#this button shuffles the cards if you would like
shuf = Button(blueFrame, text = "Shuffle", command = shuffle)
shuf.grid(row = 4, column = 2, padx=5, pady=5)
#this button raises the bet if possible
add = Button(blueFrame, text = "Raise", command = rai)
add.grid(row = 4, column = 3, padx=5, pady=5)
#this button lowers the bet if possible
minus = Button(blueFrame, text = "Lower", command = lows)
minus.grid(row = 4, column = 4, padx=5, pady=5)
#this button folds
end = Button(blueFrame, text = "Fold", command = lambda: stop(True))
end.grid(row = 4, column = 5, padx=5, pady=5)
#this is a label we will use to tell the user stuff
label = Label(blueFrame, text = "Have Fun~")
label.grid(row = 5, column = 1, columnspan = 5, padx=5, pady=5)
#this label shows the user balance
total = Label(blueFrame, text = ("Your Balance: " + str(money)))
total.grid(row = 1, column = 1, padx=5, pady=5)
#this label shows the current proposed bet
botal = Label(blueFrame, text = ("Current Bet: " + str(bet)))
botal.grid(row = 1, column = 2, padx=5, pady=5)
#this label shows the current pool
mid = Label(blueFrame, text = ("Current Pool: " + str(pool)))
mid.grid(row = 1, column = 3, padx=5, pady=5)
#this button shows the computer's balance
comp = Label(blueFrame, text = ("Computer Balance : " + str(compmoney)))
comp.grid(row = 1, column = 4, padx=5, pady=5)
#this button will be used to move on to the next stage of the background
move = Button(blueFrame, text = "Continue", command  = cont)
move.grid(row = 1, column = 5, padx=5, pady=5)

#Picture Background
bgr = PhotoImage(file="poker-dice-golden-border-casino-betting-background.png") #Background picture; change name 

# red Frame ----------------------------------------------------
redFrame = Frame(bottom_frame, bg="black")
redFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

pictureLabel = Label(redFrame, image = bgr, bd=0)#picture label(bg)
pictureLabel.pack()
 
#Added multi-button-multi-label --------------------------------
redLabel_2 = Label(redFrame, text="5-Draw Poker", bg='black', fg='red', font=('times new roman' ,30)) #Title name; change name 
redLabel_2.place(relx=0.5, rely=0.5, anchor=CENTER)

redFrame_button_1 = Button(redFrame, bg='black', fg='white',text="Play", font=('times new roman' ,15), command=showBlue) #Play button; change name
redFrame_button_1.place(relx=0.5, rely=0.65, anchor=CENTER)

redFrame_button_2 = Button(redFrame,bg='black', fg='white', text="Settings", font=('times new roman' ,15), command=showGreen)  #Settings button; change name 
redFrame_button_2.place(relx=0.5, rely=0.75, anchor=CENTER)

#---------------------------------------------------------------


mainwindow.mainloop()
