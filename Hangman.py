import random
import string

def word_length_fix():
    while True:
        length = input("Please enter fix length of word(min 4  and max 10 letters) you want the game to start: ")
        try:
            length = int(length)
            if 4<= length <=10:
                print("Word to be guesses will have fix {} letters".format(length))
                return length
            else:
                print("You haven't entered right length of letters in the word")
        except ValueError:
            print("Please enter a valid length of letters in the word")

length = word_length_fix()

def word_random(length1):
    import random
    word_list = []
    with open('/users/deven/sowpods.txt','r') as fil:
        word_list = list(fil)
    short_list = []
    for word in word_list:
        if (len(word)-1)== (length1):
            short_list.append(word.strip())
    print("shortlisted list of words has total: "+str(len(short_list)))
    return (random.choice(short_list)).lower()

choosen_word = word_random(length)
print("The choosen word was %s" %choosen_word)

def min_attempts(word1):
    no_repeat = []
    for i in word1:
        if i not in no_repeat: no_repeat.append(i)
    word_no_repeat = ("".join(no_repeat)).strip()
    print("Choosen word without repeatition of letters: " + word_no_repeat)
    return len(word_no_repeat)

attempt_low = min_attempts(choosen_word)
print("Min attempts required is %d" %attempt_low)
      
        
def attempts(min_attempt1):
    while True:
        attempts1 = input("In how many attempts(min %d and max %d) you wish to finish the game: " %(min_attempt1, min_attempt1+6))
        try:
            attempts1 = int(attempts1)
            if min_attempt1<= attempts1 <= (min_attempt1+6):
                print(" You have to guess the word in %d attempts" %attempts1)
                return attempts1
            else:
                print("Please enter correct no of attempts you need")
        except ValueError:
            print("This is not a valid no of attempts")


attempt = attempts(attempt_low)

def display_word(letter1,word1):
    length1 = len(choosen_word)
    list_word = list(word1)
    for i in range(length1):
        if letter1 == choosen_word[i]: list_word[i]=letter1
    return ("".join(list_word))

counter = 1
new_word = "*"*len(choosen_word)
while counter <= attempt :
    while True:
        guess = input("\nPlease guess your letter for attempt no-%d:   " %counter)
        guess = (str(guess)).lower()
        if guess in string.ascii_lowercase: break
        else: print("Please enter a valid letter between (a-z)")

    new_word = display_word(guess,new_word)
    print("word after revealing the right guess: "+ new_word+"\n")
    if "*" not in new_word:
        print("Congratulations! You have won and right word was %s" %new_word)
        break
    elif counter<attempt:
        print("You have %d attempts left to guess the word \n" %(attempt - counter))
    else: print("Sorry! You have lost the game")
    counter+=1
        
            
                
            







##a_string = "abc !? 123"
##alphanumeric = ""
##Initialize result string
##
##
##for character in a_string:
##    if character.isalnum():
##        alphanumeric += character
##print(alphanumeric)
    
