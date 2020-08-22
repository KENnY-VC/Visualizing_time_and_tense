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
    
    # past simple tense
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

label1 = Label(frame1, text='Please enter English sentence.')
label2 = Label(frame1, text='')
label2_0 = Label(label2, text='Past Simple(Regular form)', bg='#ffffaa')
label2_1 = Label(label2, text='Past Simple(Irregular form)', bg='#aaffaa')
message1 = Message(frame1, text='', width=500, relief='sunken')

t = StringVar()
txt = 'Two frogs, a father and his son, accidently fell into a bucket of milk. They started swimming for their lives. They swam for a long time, but there seemed no hope of their getting out. The father soon gave up and drowned. The son carried on swimming. During this time, the milk had begun to form a ball of butter. Using this island of butter as a platform, he managed to hop out of the bucket.'
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