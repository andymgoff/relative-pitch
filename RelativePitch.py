import winsound
import random
import time

notes = {"c4" : 261, "d4" : 293, "e4" : 329, "f4" : 349, "g4" : 392, "a4" : 440, "b4" : 493, "c5" : 523}

#play anchor note of C4
winsound.Beep(notes["c4"], 1000)
time.sleep(3)

#set the number of attempts
attempts = 10

# set loop index and player score to 0
i = 0
score = 0

# start looping through the attempts
while i < attempts:
    # get a random note name and frequency from the list pair
    note, freq = random.choice(list(notes.items()))
    # play the randmon note
    winsound.Beep(freq, 1000)
    # ask for an answer
    answer = input("Enter answer: ")
    # get the first character of note name, we don't need the octave number
    note_name = note[0]
    # check if the entered answer matches the note name
    if answer == note_name:
        result = "Correct"
        # increment the score by 1
        score += 1
    else:
        result = "False"
    #print the answer and the result
    print(str(i) + " " + note_name.upper() + " - " + result)
    #increment the loop counter
    i += 1

#decide what advice to give the player at the end of the round
if score < 3: advice = "Learn your intervals and try again"
if score >= 3 and score < 6: advice = "Not bad but try again"
if score >= 6 and score < 10: advice = "Your powers are strong but you're not a legend yet"
if score == 10 : advice = "Legendary! It's time to take it to the next level"

#print the result and the advice
print("You scored " + str(score) + " out of " + str(attempts) + " - " + advice)
