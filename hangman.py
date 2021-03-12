import tkinter as tk
import random
from PIL import Image, ImageTk

window1 = tk.Tk()
window1.geometry("400x400")

wins = 0
loses = 0

words = ['piano', 'guitar', 'flute', 'kookaburra', 'tiger', 'apple', 'bigmac',
         'walrus', 'egg', 'grass', 'project', 'explosion', 'destruction',
         'mayhem', 'weight', 'towel', 'cannabis', 'incomprehensibility',
         'interdisciplinary', 'consequential', 'surreptitious', 'external',
         'hypothetical', 'proliferation', 'nuclear', 'excessive', 'god',
         'opposite', 'offspring', 'abberant', 'abrasive', 'abundant',
         'elephant', 'program', 'code', 'synergy', 'vertical', 'cyber',
         'dynamic', 'fight', 'look', 'journey', 'disk', 'extend', 'timber',
         'influencer', 'astronomy', 'genetic', 'cylinder', 'enhance', 'science',
         'temperature', 'corrosive', 'blanket', 'surround', 'permanent',
         'asteroid', 'protection', 'racket', 'kingdom', 'common', 'theory',
         'practice', 'electric', 'further', 'magnetic', 'intermediate',
         'movement', 'design', 'matter', 'gift', 'measurement', 'volume',
         'density', 'table', 'stool', 'sheet', 'gun', 'lamp', 'bus', 'path',
         'dirt', 'sun', 'cloud', 'cloth', 'hot', 'bat', 'goth', 'isolate',
         'split', 'negative', 'droplet', 'float', 'evaporate', 'attract',
         'herbivore', 'humid', 'swing', 'induct', 'vertebrate', 'liquid',
         'brilliant', 'dinosaur', 'reactor', 'road', 'bus', 'knight', 'ninja',
         'blade', 'sing', 'play', 'talk', 'school', 'university', 'police',
         'retail', 'road', 'box', 'ox', 'igloo', 'soil', 'feudal', 'ancient',
         'modern', 'tattoo', 'combine', 'economy', 'plate', 'cup', 'fork',
         'spoon', 'kettle', 'refrigerator', 'floor', 'roof', 'picture',
         'keyboard', 'computer', 'lamp', 'wood', 'metal', 'program']
            
def reset_game():
    global inputtl
    global display
    global word
    global word_dic
    global display_word
    global wrong_count
    global wnl_display
    global checkbletter
    window1.title("^_^")
    frame = tk.Frame(window1, bg='white')
    frame.place(relx=0,rely=0,relheight=1,relwidth=1)
    explainer = tk.Label(window1, text="Enter a letter")
    explainer.grid(row=0, column=0)
    word = tk.Label(window1, text=" ")
    word.grid(column=0, row=1)
    inputtl = tk.Entry(window1)
    inputtl.grid(column=0, row=2)
    checkbletter = tk.Button(window1, text="Check Letter", command=game)
    checkbletter.grid(column=1, row=2, sticky=tk.W)
    display = tk.Label(window1, text='')
    display.grid(column=1, row=4)
    result = tk.Label(window1, text="")
    result.grid(column=0, row=0)
    #hsb2 = tk.Button(window1, text="See Past Scores", command=to_hswindow)
    #hsb2.grid(column=0, row=6)
    wrong_count = tk.Label(window1, text='')
    wrong_count.grid(column=1, row=5)
    wnl_display = tk.Label(window1,text="Wins: "+str(wins)+" Loses: "+str(loses))
    wnl_display.grid(column=1, row=0)
    quitb2 = tk.Button(window1, text="Quit", command=window1.quit)
    quitb2.grid(column=0, row=5)

    global incorrect
    incorrect = 0
    global correct
    correct = 0
    global random_word
    rn = random.randint(1,142)
    random_word = words[rn]
    word_dic = {}
    display_word = []
    for i in random_word:
        word_dic[i] = False
    for i in random_word:
        if word_dic[i] == True:
            display_word.append(i)
        else:
            display_word.append('*')
    word['text'] = display_word
    wrong_count['text'] = "Wrong guesses "+str(incorrect)+"/7"
    print(random_word)
    print(display_word)
    if incorrect == 0:
        piclab2 = tk.Label(image=test1)
        piclab2.grid(column=0, row=4)
    else:
        pass
    
def game():
    global wins
    global loses
    global word
    global word_dic
    global display_word
    global random_word
    global incorrect
    global correct
    global wrong_count
    global wnl_display
    global inputtl
    global checkbletter
    guess = inputtl.get()
    ng = False
    # validate entry
    if len(guess) > 1 or guess.isalpha() == False or guess == '':
        display['text'] = "Please enter a single letter"
        invalid_entry = True
    else:
        display['text'] = ''
        invalid_entry = False

    # update display with results  
    if invalid_entry == True:
        pass
    else:
        display_word = []
        for key in word_dic:
            if key == guess:
                word_dic[key] = True
            else:
                pass
        for i in random_word:
            if word_dic[i] == True:
                display_word.append(i)
            else:
                display_word.append('*')
    word['text'] = display_word
    
    # check if the answer was correct or not and apply results
    if invalid_entry == False:
        if guess in random_word:
            display['text'] = "Good job, it contains the " + guess
            correct += 1
        else:
            incorrect += 1
            display['text'] = "Sorry it doesn't contain the " + guess
    else:
        pass
    # check if they have won or lost a game yet
    win_check = True
    for letter in display_word:
        if letter == '*':
            win_check = False
        else:
            win_check = True
    if win_check == True:
        display['text'] = "WIN! press button for new word"
        wins += 1
        ng = True
    else:
        pass
        
    if incorrect >= 7:
        display['text'] = "It was " + str(random_word)
        loses += 1
        ng = True
    else:
        pass
    if ng == True:
        newgameb = tk.Button(window1, text="New word", command=reset_game)
        newgameb.grid(column=1, row=2)
        checkbletter.grid_forget()
    else:
        pass
    
    print(word_dic)
    print(incorrect)
    wnl_display['text'] = "Wins: "+str(wins)+" Loses: "+str(loses)
    wrong_count['text'] = "Wrong guesses "+str(incorrect)+"/7"
    inputtl.delete(0, tk.END)

    if incorrect == 0:
        piclab2a = tk.Label(image=test1)
        piclab2a.grid(column=0, row=4)
    elif incorrect == 1:
        piclab3 = tk.Label(image=test2)
        piclab3.grid(column=0, row=4)
    elif incorrect == 2:
        piclab4 = tk.Label(image=test3)
        piclab4.grid(column=0, row=4)
    elif incorrect == 3:
        piclab5 = tk.Label(image=test4)
        piclab5.grid(column=0, row=4)
    elif incorrect == 4:
        piclab6 = tk.Label(image=test5)
        piclab6.grid(column=0, row=4)
    elif incorrect == 5:
        piclab7 = tk.Label(image=test6)
        piclab7.grid(column=0, row=4)
    elif incorrect == 6:
        piclab8 = tk.Label(image=test7)
        piclab8.grid(column=0, row=4)
    else:
        piclab9 = tk.Label(image=test)
        piclab9.grid(column=0, row=4)
                
    
def search():
    pass

def to_hswindow():
    newwin = tk.Toplevel(window1)
    newwin.title("^o^")
    hsl = tk.Label(newwin, text="High scores")
    hsl.grid(column=0, row=0)
    hsoutput = tk.Text(newwin, bg="light gray", height=10, width=40)
    hsoutput.grid(column=0, row=1)
    hsinput = tk.Entry(newwin)
    hsinput.grid(column=0, row=2)
    hssb = tk.Button(newwin, text="Search", command=search)
    hssb.grid(column=1, row=2)

hml = tk.Label(window1, text="Hangman by Tim Randall")
hml.grid(column=0, row=0)

playb = tk.Button(window1, text="Play", command=reset_game)
playb.grid(column=0, row=1)

#hsb = tk.Button(window1, text="See Past Scores", command=to_hswindow)
#hsb.grid(column=1, row=1)

quitb = tk.Button(window1, text="Quit", command=window1.quit)
quitb.grid(column=2, row=1)

openimage = Image.open("/Users/timrandall/Projects/Hangman/end.png")
test = ImageTk.PhotoImage(openimage)
piclab1 = tk.Label(image=test)
piclab1.grid(column=0, row= 5)

openimage1 = Image.open("/Users/timrandall/Projects/Hangman/one.png")
test1 = ImageTk.PhotoImage(openimage1)
openimage2 = Image.open("/Users/timrandall/Projects/Hangman/two.png")
test2 = ImageTk.PhotoImage(openimage2)
openimage3 = Image.open("/Users/timrandall/Projects/Hangman/three.png")
test3 = ImageTk.PhotoImage(openimage3)
openimage4 = Image.open("/Users/timrandall/Projects/Hangman/four.png")
test4 = ImageTk.PhotoImage(openimage4)
openimage5 = Image.open("/Users/timrandall/Projects/Hangman/five.png")
test5 = ImageTk.PhotoImage(openimage5)
openimage6 = Image.open("/Users/timrandall/Projects/Hangman/six.png")
test6 = ImageTk.PhotoImage(openimage6)
openfillimage = Image.open("/Users/timrandall/Projects/Hangman/fill.png")
test7 = ImageTk.PhotoImage(openfillimage)

window1.title("Welcome")

window1.mainloop()
