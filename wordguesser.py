import requests
import random

def random_word(): #fetches a random word of 5 to 9 letters from api
  word_length=str(random.randint(5,9))
  link="https://random-word-api.vercel.app/api?words=1&length="+word_length
  word=requests.get(link).json()
  stuff=[word[0],word_length]
  return stuff #returns a list containing the word and its length

def hidden_word(word,length,mode):
  letters=""
  sample_space=list( range(0,length))
  hide_index=random.sample(sample_space,k=mode)
  for i in range(0,len(word)):
    if i in hide_index:
      letters+="_"
    else:
      letters+=word[i]
  
  word_and_index=[letters, hide_index]
  return word_and_index
    

#counters
high_score=score=games_played=w_guessed=w_skipped=count=0

#main program
active=True
print("SUBHOM's WORD GUESSER GAME")
while active:
  print("\nHigh Score: ",high_score, "\tGames Played: ",games_played)
  user_input=input("Select Mode:\n1. EASY (2 blanks)\n2. HARD (3 blanks) \n\nType easy/hard (q to quit): ")
  hint=10
  if user_input.lower()=="easy" or user_input.lower()=="hard":
    mode = 2 if user_input.lower()=="easy" else 3

    while True or hint==0:
      data=random_word() #data containts word and its length
      actual_word=data[0]
      actual_length=int(data[1])
      hidden_data=hidden_word(actual_word,actual_length,mode) #fetching hidden data
      the_word=hidden_data[0]

      print(f"\n<----- WORD NO {count+1} [SCORE: {score}] [MODE: {user_input.capitalize()}] ----->")
      print("\n\tYour word is: ",the_word)
      print(f"\tType h for hint! ({hint} remaining)")
      guess=input("\tEnter your guess: ")

      if guess.lower()==actual_word:
        print(f"\tCorrect! +{actual_length} Score!")
        score+=actual_length
        w_guessed+=1

      elif guess.lower()=="h":
        hint-=1
        hint_letter_index=random.choice(hidden_data[1])
        print(f"\tHINT ({hint} remaining): Letter {hint_letter_index+1} is {actual_word[hint_letter_index]}")
        new_guess=input("\tEnter your guess: ")
        if new_guess.lower()==actual_word:
          print(f"\tCorrect! +{actual_length} Score!")
          score+=actual_length
          w_guessed+=1
        else:
          print(f"\tWrong guess! The word was {actual_word}")
          break

      else:
        print(f"\tWrong guess! The word was {actual_word}")
        break
      
      count+=1
      games_played+=1
      if score>high_score:
        high_score=score

  elif user_input.lower()=="q":
    active=False
  else:
    print("\tInvalid option! Try again...")




