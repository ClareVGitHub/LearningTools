# wortschatz is a learning aid for learning german as a foreign language. You can choose to add words and thier translation 
# to a sqlite database using sqlalchemy or you can choose the play mode which will cyce through your words to help you 
# memorize them.

# Open in the terminal with >>> python3 wortschatz_2.2.py

# requirements: You need to have installed python3 and sqlalchemy

import sqlalchemy

from sqlalchemy import create_engine
engine = create_engine('sqlite:///ws.db')

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Setting up table

from sqlalchemy import Column, Integer, Numeric, String

class Wortschatz(Base):
  __tablename__ = 'wortschatz'

  word_id = Column(Integer, primary_key = True)
  germanWord = Column(String(100), index = True)
  englishWord = Column(String(100), index = True)
  wordType = Column(String(50), index = True)
  score = Column(Integer)
  attempts = Column(Integer)

# persisting the table

Base.metadata.create_all(engine)

# words = session.query(Wortschatz).all()
# for word in words:
    # print(word.germanWord)

from sqlalchemy import update

# adding a word
y = True
addWs = y
add = ()
play = ()
words = session.query(Wortschatz).all()
correctAnswer = False
answer = ()
skip = ()
mode = ()

print ('Type add to add new words OR play to play Wortschatz')
mode = input()

if mode == 'add':

    while addWs:
        print('Add German word')
        GW = input()
        print ('Add English word')
        EW = input()
        print ('Add word type')
        WT = input()
        cc_word = Wortschatz(germanWord = GW,
                            englishWord = EW,
                            wordType = WT,
                            score = 0,
                            attempts = 0)
        session.add(cc_word)
        session.commit()
        print('type y to add another word OR press enter to quit')
        keepGoing = input()
        if keepGoing != 'y':
            addWs = False

    print ('session ended')

elif mode == 'play':
    play = True
    for word in words:
        correctAnswer = False
        while correctAnswer == False and play == True:
            print('Give the English for'+' '+(word.germanWord), 'OR enter skip or quit')
            answer = input()
            if answer == word.englishWord:
                correctAnswer = True
                word.score = word.score + 1
                session.commit()
                word.attempts = word.attempts + 1
                session.commit()
                print ('Correct!'+' '+ str(word.score)+' '+'correct out of'+' '+str(word.attempts)+' '+'attempts')
            elif answer == "skip":
                print ('the correct answer is:'+' '+(word.englishWord))
                correctAnswer = True
            elif answer == 'quit':
                print('session ended')
                play = False
                break
            else:
                print('sorry wrong answer, try again')
                word.attempts = word.attempts + 1
                session.commit()
                print (str(word.attempts)+' '+'attempts')

    for word in words:
        correctAnswer = False
        while correctAnswer == False and play == True:
            print('Give the German for'+' '+(word.englishWord), 'OR enter skip or quit')
            answer = input()
            if answer == word.germanWord:
                correctAnswer = True
                word.score = word.score + 1
                session.commit()
                word.attempts = word.attempts + 1
                session.commit()
                print ('Correct!'+' '+ str(word.score)+' '+'correct out of'+' '+str(word.attempts)+' '+'attempts')
            elif answer == 'skip':
                print('the correct answer is:'+' '+(word.germanWord))
                correctAnswer = True
            elif answer == 'quit':
                print('session ended')
                play = False
                break
            else:
                print('sorry wrong answer, try again')
                word.attempts = word.attempts + 1
                session.commit()
                print (str(word.attempts)+' '+'attempts')
