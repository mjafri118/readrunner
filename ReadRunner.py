#!/usr/bin/env python
# coding: utf-8

# In[216]:


# Import dem libraries.
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from newspaper import Article


# In[218]:


def getLeft(word):
    length = len(word)
    
    if length == 1:
        return ""
    
    if length == 2:
        return ""
    
    leftHalf = word[0:length//2]
    return leftHalf

def getMiddle(word):
    length = len(word)
    
    if length == 0:
        return ""
    
    if length == 1:
        return word
    
    if length == 2:
        return word[0]
    
    centerChar = word[length//2]
    return centerChar

def getRight(word):
    length = len(word)
    
    if length == 1:
        return ""
    
    if length == 2:
        return word[1]
    
    
    rightHalf = word[length//2 + 1:]
    return rightHalf


# In[219]:


def genVid(words, WPM):
    # ----- Set up Plotting Area -----
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set(xlim=(-3, 3), ylim=(-1, 1))
    plt.xticks([])
    plt.yticks([])
    ax.set(xlim=(-1, 1), ylim=(-1, 1))

    # ----- TUNABLE PARAMETERS -----
    CLOSENESS = .05
    FONTSIZE = 25
    WPM = WPM

    # ----- TEXT INITIALIZATION -----
    logo = ax.text(-.95,
                      .95,
                      "ReadRunner",
                      ha='left', 
                      va='top',
                      color = "purple",
                      fontsize=15)
    
    wpm = ax.text(.95, 
                  .95,
                  str(WPM) + " WPM",
                  ha='right', 
                  va='top',
                  color = "red",
                  fontsize=10)

    leftText = ax.text(-CLOSENESS,
                      0,
                      "left",
                      ha='right', 
                      va='center',
                      fontsize=FONTSIZE)

    middleText = ax.text(0, 
                    0, 
                    "left center",
                    ha='center', 
                    va='center',
                    fontsize=FONTSIZE,
                    color='red')

    rightText = ax.text(CLOSENESS,
                      0,
                      "right",
                      ha='left', 
                      va='center',
                      fontsize=FONTSIZE)
    

    # ----- Function to update -----
    def animate(i):
        leftText.set_text(getLeft(words[i]))
        middleText.set_text(getMiddle(words[i]))
        rightText.set_text(getRight(words[i]))

    # ----- Animation call -----
    frames = len(words)
    interval = (1000)*(60/frames)*(frames)/(WPM)
    anim = FuncAnimation(
        fig, animate, interval=interval, frames=frames)

    # ----- Show the Animation -----
    return(HTML(anim.to_html5_video()))

    # ----- Save the Animation -----
#     anim.save('speedread.mp4')

    fig.withdraw()
    ax.withdraw()
    fig.close()
    
    plt.close()


    print("Speed read saved!")
#     anim.save('filename.gif', writer='imagemagick')


# In[ ]:


# Parse Words 
def parseURL(url):
    article = Article(url)
    article.download()
    article.parse()
    text = article.text.strip()
    return(text)

# Processing
def parseWords(rawText):
    rawText = rawText.replace("\r", " ")
    rawText = rawText.replace("\n", " ")
    
    words = rawText.split(" ")
    return words


# In[246]:


def readRunner(url, WPM):
    return genVid(parseWords(parseURL(url)), WPM = WPM)


# In[257]:


def readRunners(hi="4"):
    # Generate video
    print("Welcome to ReadRunner! \r\n Making reading quicker than ever.")
    rawText = input("Enter news article: ")
    WPM = int(input("Enter WPM: "))
    return readRunner(rawText, WPM)

#readRunnerNB()


# In[ ]:





# In[ ]:




