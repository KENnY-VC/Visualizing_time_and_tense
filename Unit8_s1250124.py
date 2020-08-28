# Visualizing time and tense
# Unit8 Activity 6: Prototype draft submission
# s1250124 Kentaro Yumita

# command for running:
# python Unit8_s1250124.py

# how to use:
# Please enter English sentences.
# If you push the "analyze" button, you can find all past tense verbs by list on the console and color label.
# It finds regular verb and irregular verb.

# references:
# Python Basics: https://www.javadrive.jp/python/
# NLTK 3.5 documentation: https://www.nltk.org/
# GUI programming by tkinter: https://python.keicode.com/advanced/tkinter.php


# GUI
from tkinter import *
from tkinter import ttk
from tkinter import font

# NLTK
import nltk

# regular expression
import re

# list of labels(word list)
labels = []

# list of found instances
list1 = []
list2 = []

# update the lower text(result of analysis)
def updateText():
  # initialize labels
  global labels
  for lb in labels:
    lb.grid_forget()
  labels = []

  # initialize instances
  global list1
  global list2
  list1 = []
  list2 = []
  
  # nltk analysis
  tokens = nltk.word_tokenize(textbox1.get(1.0, 'end -1c'))
  pos = nltk.pos_tag(tokens)
  
  # for each words
  i = 0
  while i<len(pos):
    word = pos[i][0]
    tag = pos[i][1]

    # past tense verb
    if tag == 'VBD':
      match = re.search('ed$',word)
      color = '#ffffff'
      
      # end with `ed`(Regular form)
      if match != None:
        list1.append(word)
        color = '#ffffaa'

      # don't end with 'ed'(Irregular form)
      else:
        list2.append(word)
        color = '#aaffaa'

      # draw with color label
      # and register an instance
      f = font.Font(root,family='System', size=10, underline=True)
      labels.append(Label(message1, text=word, font=f, bg=color))
      labels[len(labels)-1].grid(column=i%10, row=i//10, sticky=W, padx=2, pady=2)
      i += 1

    # otherwise, this word doesn't label
    else:
      f = font.Font(root,family='System', size=10, underline=False)
      labels.append(Label(message1, text=word, font=f))
      labels[len(labels)-1].grid(column=i%10, row=i//10, sticky=W, padx=2, pady=2)
      i += 1
  
  # display all instances on console
  list1.sort()
  print('<--Regular verbs-->')
  for li in list1:
    print(li)
  print()

  list2.sort()
  print('<--Irregular verbs-->')
  for li in list2:
    print(li)
  print()


# making window
root = Tk()
root.title('Unit 7 Activity 6: Problem solving: NLTK pipeline in Python')	

# making widget
frame1 = ttk.Frame(root, padding=16)

label1 = Label(frame1, text='Past tense colorizer')
label2 = Label(frame1, text='')
label2_0 = Label(label2, text='Regular form', bg='#ffffaa')
label2_1 = Label(label2, text='Irregular form', bg='#aaffaa')
message1 = Message(frame1, text='', width=500, relief='sunken')

t = StringVar()
txt = "I don't speak Japanese.\n" \
+ "I worked for Microsoft.\n" \
+ "We will eat in ten minutes.\n" \
+ "He is studying to become a dentist.\n" \
+ "Yesterday evening we were watching the game so we couldn't come.\n" \
+ "It will be raining the entire week.\n" \
+ "I have been to Tokyo.\n" \
+ "I lost so much weight because I had begun exercising.\n" \
+ "She will have gotten ready by the time they leave the house.\n" \
+ "They read the book."
textbox1 = Text(frame1, height=10, width=70, wrap=WORD)
textbox1.insert(1.0, txt)

button1 = ttk.Button(frame1, text='Analyze')
button1['command'] = updateText

# layout
frame1.pack()
label1.grid(column=0, row=0, sticky=W, padx=5, pady=10)
label2.grid(column=0, row=3, sticky=W, padx=5, pady=10)
label2_0.grid(column=0, row=3, sticky=W, padx=5, pady=10)
label2_1.grid(column=1, row=3, sticky=W, padx=5, pady=10)
message1.grid(column=0, row=4, sticky=W, padx=5, pady=10)
textbox1.grid(column=0, row=1, sticky=W, padx=5, pady=10)
button1.grid(column=0, row=2, sticky=W, padx=5, pady=10)

# start window display
root.mainloop()