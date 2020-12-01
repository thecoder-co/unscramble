# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 09:35:21 2020
made to unscramble a jumble of letters into coherent words
@author: idunnuoluwa
"""

# imported frameworks
from tkinter import *
import sys
import tkinter.font as font

# main program
class Window:
    
    def __init__(self, master):
        
        def find(a, letters):
            foundWords = []
            eng = open('words_alpha.txt', 'r')  #open the file in read mode
            file_content = eng.read()   # read the file
            # note that python reads the content of the file as one long string.
            # so the file_content variable refers to a single string containing all the words in the file.
    
            word_list = file_content.split()    # split method turns it into a list
            necessary_words = []
    
            for i in word_list: # this loop traverses the list and creates a new list containing all words of length a
                if len(i) in range(a+1):
                    necessary_words.append(i)

            # now the variable necessary_words contains a list of all words of length a.

            for j in necessary_words:
                if isin(j, letters):
                    foundWords.append(j)
        
            return foundWords
        
        
        def freql(w, lst): # used to find the frequency of a particular object in its iterable object 
            count = 0 # if it doesn't appear freql returns zero
            for i in lst: # tranverses the container
       	        if i == w:
                    count += 1 # adds to the count frequency
            return count
	       
                    
        def isin(lily, ylil): # used to confirm if a word can be gotten from another word
	        a = list(lily) # turns arg 1 to a transversable object
	        b = list(ylil) # turns arg 2 to a transversable object
	        for i in a: 
		        if i not in ylil: # first condition to confirm whether they have the same letters
			        return False
	        for i in a:
		        if freql(i, a) > freql(i, b): # second condition to confirm whether duplicates are allowed in arg 2
			        return False
	        return True


        def from_rgb(r, g, b):
            return "#%02x%02x%02x" %(r, g, b)
    
        def quit(event):
            sys.exit()
            
        def round_rect(x1, y1, x2, y2, radius=25, **kwargs):
                self.points = [x1+radius, y1,
                               x1+radius, y1,
                               x2-radius, y1,
                               x2-radius, y1,
                               x2, y1,
                               x2, y1+radius,
                               x2, y1+radius,
                               x2, y2-radius,
                               x2, y2-radius,
                               x2, y2,
                               x2-radius, y2,
                               x2-radius, y2,
                               x1+radius, y2,
                               x1+radius, y2,
                               x1, y2,
                               x1, y2-radius,
                               x1, y2-radius,
                               x1, y1+radius,
                               x1, y1+radius,
                               x1, y1]
                return self.c.create_polygon(self.points, **kwargs, smooth=True)
            
        def info(self):
                self.toplevel = Toplevel(bg=from_rgb(0, 68, 136))
                self.toplevel.transient()
                self.frame = Frame(self.toplevel, width=400, height=300)
                self.toplevel.title("Program info")
                Label(self.toplevel, text='unscramble', bg=from_rgb(0, 68, 136),    fg='white').pack(pady=20)
                Label(self.toplevel, text="abimbola idunnuoluwa programed this", bg=from_rgb(0, 68, 136), fg='white').pack()
                Label(self.toplevel, text="for unscrambling random jumbles of letters into coherent words", bg=from_rgb(0, 68, 136), fg='white').pack()
                Label(self.toplevel, text="thank you :-)", bg=from_rgb(0, 68, 136), fg='white').pack()
                Button(self.toplevel, text="close", command=self.toplevel.withdraw).pack(pady=30)
            
        def firstWindow():
            # to make the canvas global
            global c
            
            def unscramble(event):
                self.c.delete('all')
                secondWindow()
        
            # c is the canvas
            self.c = Canvas(width=1300, height=750)

            # the background image
            self.c.create_image(0, 0, anchor=NW, image=bgimage)
            
            # the big unscramble text
            self.c.create_text(650, 290, text='UNSCRAMBLE', font=('Bookman Old Style', 90), fill='white')
            
            # code for the info button
            
            def infoenter(event):
                self.c.itemconfig(infoBtn, fill='blue')
                self.c.move(infoBtn, 1, -1)
                self.c.move(infoTxt, 1, -1)
                
            def infoleave(event):
                self.c.itemconfig(infoBtn, fill=from_rgb(0, 68, 136))
                self.c.move(infoBtn, -1, 1)
                self.c.move(infoTxt, -1, 1)
            
            infoBtn = round_rect(10, 675, 160, 735, fill=from_rgb(0, 68, 136))
            infoTxt = self.c.create_text(85, 707, text='Info', font='helvetica 48', fill='white')
            self.c.tag_bind(infoBtn, '<ButtonPress-1>', info)
            self.c.tag_bind(infoTxt, '<ButtonPress-1>', info)
            self.c.tag_bind(infoBtn, '<Enter>', infoenter)
            self.c.tag_bind(infoTxt, '<Enter>', infoenter)
            self.c.tag_bind(infoBtn, '<Leave>', infoleave)
            self.c.tag_bind(infoTxt, '<Leave>', infoleave)
            
            # code for the exit button
            
            def exitenter(event):
                self.c.itemconfig(exitBtn, fill='blue')
                self.c.move(exitBtn, 1, -1)
                self.c.move(exitTxt, 1, -1)
                
            def exitleave(event):
                self.c.itemconfig(exitBtn, fill=from_rgb(0, 68, 136))
                self.c.move(exitBtn, -1, 1)
                self.c.move(exitTxt, -1, 1)
            
            exitBtn = round_rect(1135, 675, 1295, 735, fill=from_rgb(0, 68, 136))
            exitTxt = self.c.create_text(1215, 707, text='Exit', font='helvetica 48', fill='white')
            self.c.tag_bind(exitBtn, '<ButtonPress-1>', quit)
            self.c.tag_bind(exitTxt, '<ButtonPress-1>', quit)
            self.c.tag_bind(exitBtn, '<Enter>', exitenter)
            self.c.tag_bind(exitTxt, '<Enter>', exitenter)
            self.c.tag_bind(exitBtn, '<Leave>', exitleave)
            self.c.tag_bind(exitTxt, '<Leave>', exitleave)
            
            # code for the unscramble button to go to the second window
            
            def uscenter(event):
                self.c.itemconfig(uscBtn, fill='blue')
                self.c.move(uscBtn, 1, -1)
                self.c.move(uscTxt, 1, -1)
                
            def uscleave(event):
                self.c.itemconfig(uscBtn, fill=from_rgb(0, 68, 136))
                self.c.move(uscBtn, -1, 1)
                self.c.move(uscTxt, -1, 1)
            
            uscBtn = round_rect(400, 365, 890, 455, fill=from_rgb(0, 68, 136))
            uscTxt = self.c.create_text(640, 415, text='Unscramble', font='helvetica 65', fill='white')
            self.c.tag_bind(uscBtn, '<ButtonPress-1>', unscramble)
            self.c.tag_bind(uscTxt, '<ButtonPress-1>', unscramble)
            self.c.tag_bind(uscBtn, '<Enter>', uscenter)
            self.c.tag_bind(uscTxt, '<Enter>', uscenter)
            self.c.tag_bind(uscBtn, '<Leave>', uscleave)
            self.c.tag_bind(uscTxt, '<Leave>', uscleave)
            
            self.c.pack()
            
        def secondWindow():
            
            def unscramble(event):
                word = userEntry.get()
                word = word.lower()
                
                print(word)
                
                lst = find(len(word)+1, word)
                
                allWords.delete(0, END)
                for i in range(len(word)+1):
                    for j in lst:
                        if len(j) == i:
                            allWords.insert(END, j)
                threeLetsWrds.delete(0, END)
                for i in lst:
                    if len(i) == 3:
                        threeLetsWrds.insert(END, i)            
                fourLetsWrds.delete(0, END)
                for i in lst:
                    if len(i) == 4:
                        fourLetsWrds.insert(END, i)
                fiveLetsWrds.delete(0, END)
                for i in lst:
                    if len(i) == 5:
                        fiveLetsWrds.insert(END, i)
                sixLetsWrds.delete(0, END)
                for i in lst:
                    if len(i) == 6:
                        sixLetsWrds.insert(END, i)
                sevenLetsWrds.delete(0, END)
                for i in lst:
                    if len(i) == 7:
                        sevenLetsWrds.insert(END, i)
                eightLetsWrds.delete(0, END)
                for i in lst:
                    if len(i) == 8:
                        eightLetsWrds.insert(END, i)
                        
            
            self.c.create_image(0, 0, anchor=NW, image=bgimage)

            # code for the info button
            
            def infoenter(event):
                self.c.itemconfig(infoBtn, fill='blue')
                self.c.move(infoBtn, 1, -1)
                self.c.move(infoTxt, 1, -1)
                
            def infoleave(event):
                self.c.itemconfig(infoBtn, fill=from_rgb(0, 68, 136))
                self.c.move(infoBtn, -1, 1)
                self.c.move(infoTxt, -1, 1)
            
            infoBtn = round_rect(10, 675, 160, 735, fill=from_rgb(0, 68, 136))
            infoTxt = self.c.create_text(85, 707, text='Info', font='helvetica 48', fill='white')
            self.c.tag_bind(infoBtn, '<ButtonPress-1>', info)
            self.c.tag_bind(infoTxt, '<ButtonPress-1>', info)
            self.c.tag_bind(infoBtn, '<Enter>', infoenter)
            self.c.tag_bind(infoTxt, '<Enter>', infoenter)
            self.c.tag_bind(infoBtn, '<Leave>', infoleave)
            self.c.tag_bind(infoTxt, '<Leave>', infoleave)
            
            # code for the exit button
            
            def exitenter(event):
                self.c.itemconfig(exitBtn, fill='blue')
                self.c.move(exitBtn, 1, -1)
                self.c.move(exitTxt, 1, -1)
                
            def exitleave(event):
                self.c.itemconfig(exitBtn, fill=from_rgb(0, 68, 136))
                self.c.move(exitBtn, -1, 1)
                self.c.move(exitTxt, -1, 1)
            
            exitBtn = round_rect(1135, 675, 1295, 735, fill=from_rgb(0, 68, 136))
            exitTxt = self.c.create_text(1215, 707, text='Exit', font='helvetica 48', fill='white')
            self.c.tag_bind(exitBtn, '<ButtonPress-1>', quit)
            self.c.tag_bind(exitTxt, '<ButtonPress-1>', quit)
            self.c.tag_bind(exitBtn, '<Enter>', exitenter)
            self.c.tag_bind(exitTxt, '<Enter>', exitenter)
            self.c.tag_bind(exitBtn, '<Leave>', exitleave)
            self.c.tag_bind(exitTxt, '<Leave>', exitleave)
            
            self.c.create_text(165, 55, text='UNSCRAMBLE', font=('Bookman Old Style', 32), fill='white')
            
            entryBoxBg = round_rect(330, 10, 930, 110, fill=from_rgb(0, 68, 136))
            
            entryBox = Entry(font=('Century Gothic', 55), bg=from_rgb(0, 68, 136), textvariable=userEntry)
            entryBox.configure(width=14, relief='flat', fg='white')
            entryBox_window = self.c.create_window(340, 15, anchor=NW, window=entryBox)
            
            
            def uscenter(event):
                self.c.itemconfig(uscBtn, fill='blue')
                self.c.move(uscBtn, 1, -1)
                self.c.move(uscTxt, 1, -1)
                
            def uscleave(event):
                self.c.itemconfig(uscBtn, fill=from_rgb(0, 68, 136))
                self.c.move(uscBtn, -1, 1)
                self.c.move(uscTxt, -1, 1)
            
            uscBtn = round_rect(945, 30, 1295, 90, fill=from_rgb(0, 68, 136))
            uscTxt = self.c.create_text(1122, 60, text='Unscramble', font='helvetica 48', fill='white')
            self.c.tag_bind(uscBtn, '<ButtonPress-1>', unscramble)
            self.c.tag_bind(uscTxt, '<ButtonPress-1>', unscramble)
            self.c.tag_bind(uscBtn, '<Enter>', uscenter)
            self.c.tag_bind(uscTxt, '<Enter>', uscenter)
            self.c.tag_bind(uscBtn, '<Leave>', uscleave)
            self.c.tag_bind(uscTxt, '<Leave>', uscleave)
            
            allWordsbg = round_rect(945, 150, 1295, 650, fill=from_rgb(0, 68, 136))
            allWordsTxt = self.c.create_text(1128, 168, text='All Words', font='helvetica 23', fill='white')
            
            allWordsfrm = Frame()
            allWords = Listbox(allWordsfrm, width=36, height=23, relief='flat', bg=from_rgb(0, 68, 136) , font='helvetica 13', fg='white', highlightthickness=0)
            allWords.pack(side=LEFT)
            allWordsScroll = Scrollbar(allWordsfrm, bg=from_rgb(0, 68, 136))
            allWordsScroll.pack(side=RIGHT, fill='y')
            allWords.config(yscrollcommand=allWordsScroll.set)
            allWordsScroll.config(command=allWords.yview)
            allWordsfrm_window = self.c.create_window(952, 188, anchor=NW, window=allWordsfrm)
            
            threeLetsWrdsbg = round_rect(10, 150, 310, 392.5, fill=from_rgb(0, 68, 136))
            threeLetsWrdsTxt = self.c.create_text(160, 170, text='Three Letter Words', font='helvetica 23', fill='white')
            
            threeLetsWrdsfrm = Frame()
            threeLetsWrds = Listbox(threeLetsWrdsfrm, width=30, height=10, relief='flat', bg=from_rgb(0, 68, 136), font='helvetica 13', fg='white', highlightthickness=0)
            threeLetsWrds.pack(side=LEFT)
            threeLetsWrdsScroll = Scrollbar(threeLetsWrdsfrm, bg=from_rgb(0, 68, 136))
            threeLetsWrdsScroll.pack(side=RIGHT, fill='y')
            threeLetsWrds.config(yscrollcommand=threeLetsWrdsScroll.set)
            threeLetsWrdsScroll.config(command=threeLetsWrds.yview)
            threeLetsWrdsfrm_window = self.c.create_window(21, 191, anchor=NW, window=threeLetsWrdsfrm)
            
            # create the fourLetsWrds listbox
            fourLetsWrdsbg = round_rect(320, 150, 620, 392.5, fill=from_rgb(0, 68, 136))
            fourLetsWrdsTxt = self.c.create_text(470, 170, text='Four letter Words', font='helvetica 23', fill='white')
            
            fourLetsWrdsfrm = Frame()
            fourLetsWrds = Listbox(fourLetsWrdsfrm, width=30, height=10, relief='flat', bg=from_rgb(0, 68,  136), font='helvetica 13', fg='white', highlightthickness=0)
            fourLetsWrds.pack(side=LEFT)
            fourLetsWrdsScroll = Scrollbar(fourLetsWrdsfrm, bg=from_rgb(0, 68, 136))
            fourLetsWrdsScroll.pack(side=RIGHT, fill='y')
            fourLetsWrds.config(yscrollcommand=fourLetsWrdsScroll.set)
            fourLetsWrdsScroll.config(command=fourLetsWrds.yview)
            fourLetsWrdsfrm_window = self.c.create_window(331, 191, anchor=NW, window=fourLetsWrdsfrm)
            
            # create the fiveLetsWrds listbox
            fiveLetsWrdsbg = round_rect(630, 150, 930, 392.5, fill=from_rgb(0, 68, 136))
            allWordsTxt = self.c.create_text(780, 170, text='Five Letter Words', font='helvetica 23', fill='white')
            
            fiveLetsWrdsfrm = Frame()
            fiveLetsWrds = Listbox(fiveLetsWrdsfrm, width=30, height=10, relief='flat', bg=from_rgb(0, 68,  136), font='helvetica 13', fg='white', highlightthickness=0)
            fiveLetsWrds.pack(side=LEFT)
            fiveLetsWrdsScroll = Scrollbar(fiveLetsWrdsfrm, bg=from_rgb(0, 68, 136))
            fiveLetsWrdsScroll.pack(side=RIGHT, fill='y')
            fiveLetsWrds.config(yscrollcommand=fiveLetsWrdsScroll.set)
            fiveLetsWrdsScroll.config(command=fiveLetsWrds.yview)
            fiveLetsWrdsfrm_window = self.c.create_window(641, 191, anchor=NW, window=fiveLetsWrdsfrm)
            
            # create the sixLetsWrds listbox
            sixLetsWrdsbg = round_rect(10, 407.5, 310, 650, fill=from_rgb(0, 68, 136))
            sixWrdsTxt = self.c.create_text(160, 427.5, text='Six Letter Words', font='helvetica 23', fill='white')
            
            sixLetsWrdsfrm = Frame()
            sixLetsWrds = Listbox(sixLetsWrdsfrm, width=30, height=10, relief='flat', bg=from_rgb(0, 68,    136), font='helvetica 13', fg='white', highlightthickness=0)
            sixLetsWrds.pack(side=LEFT)
            sixLetsWrdsScroll = Scrollbar(sixLetsWrdsfrm, bg=from_rgb(0, 68, 136))
            sixLetsWrdsScroll.pack(side=RIGHT, fill='y')
            sixLetsWrds.config(yscrollcommand=sixLetsWrdsScroll.set)
            sixLetsWrdsScroll.config(command=sixLetsWrds.yview)
            sixLetsWrdsfrm_window = self.c.create_window(21, 447.5, anchor=NW, window=sixLetsWrdsfrm)
            
            # create the sevenLetsWrds listbox
            sevenLetsWrdsbg = round_rect(320, 407.5, 620, 650, fill=from_rgb(0, 68, 136))
            eightWrdsTxt = self.c.create_text(470, 427.5, text='Seven Letter Words', font='helvetica 23', fill='white')
            
            sevenLetsWrdsfrm = Frame()
            sevenLetsWrds = Listbox(sevenLetsWrdsfrm, width=30, height=10, relief='flat', bg=from_rgb(0, 68, 136), font='helvetica 13', fg='white', highlightthickness=0)
            sevenLetsWrds.pack(side=LEFT)
            sevenLetsWrdsScroll = Scrollbar(sevenLetsWrdsfrm, bg=from_rgb(0, 68, 136))
            sevenLetsWrdsScroll.pack(side=RIGHT, fill='y')
            sevenLetsWrds.config(yscrollcommand=sevenLetsWrdsScroll.set)
            sevenLetsWrdsScroll.config(command=sevenLetsWrds.yview)
            sevenLetsWrdsfrm_window = self.c.create_window(331, 447.5, anchor=NW, window=sevenLetsWrdsfrm)
            
            
            # create the eightLetsWrds listbox
            eightLetsWrdsbg = round_rect(630, 407.5, 930, 650, fill=from_rgb(0, 68, 136))
            eightWrdsTxt = self.c.create_text(780, 427.5, text='Eight Letter Words', font='helvetica 23', fill='white')
            
            eightLetsWrdsfrm = Frame()
            eightLetsWrds = Listbox(eightLetsWrdsfrm, width=30, height=10, relief='flat', bg=from_rgb(0, 68, 136), font='helvetica 13', fg='white',highlightthickness=0)
            eightLetsWrds.pack(side=LEFT)
            eightLetsWrdsScroll = Scrollbar(eightLetsWrdsfrm, bg=from_rgb(0, 68, 136))
            eightLetsWrdsScroll.pack(side=RIGHT, fill='y')
            eightLetsWrds.config(yscrollcommand=eightLetsWrdsScroll.set)
            eightLetsWrdsScroll.config(command=eightLetsWrds.yview)
            eightLetsWrdsfrm_window = self.c.create_window(641, 447.5, anchor=NW, window=eightLetsWrdsfrm)
                
        firstWindow()
      
            
      
root = Tk()
bgimage = PhotoImage(file='starry.png')
userEntry = StringVar(root)

ex4 = Window(root)


root.title('Unscramble')


root.mainloop()        