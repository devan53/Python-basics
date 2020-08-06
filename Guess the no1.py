from random import randint
def choosen_num():
    while True:
        num = input("Enter the highest no(between 10 and 30) within which you want to guess the no: ")
        try:
            num = int(num)
            if 10 <= num <= 30:
                print("Guess should lie between 1 and {}".format(num))
                break
            else:
                print("{} is not between 10 and 30".format(num))
        except ValueError:
            print("{} is not a number between 10 and 30".format(num))
    random_num = randint(1,num)
    return random_num

random_num = choosen_num()
print(random_num)

def num_attempts():
    while True:
        attempts = input("Enter the no of attempts (max5) you want to make: ")
        try:
            attempts = int(attempts)
            if 1 <= attempts <= 5:
                print("You have to guess the no in {} attempts".format(attempts))
                break
            else:
                print("{} attempts is outside allowed 5 attempts".format(attempts))
        except ValueError:
            print("{} is not a valid attempt under 5".format(attempts))
            
    return attempts

attempts = num_attempts()

guess_list =[]
for i in range(attempts):
    guess = input("Please tell us your guess no. %d: " %(i+1))
    try:
        guess = int(guess)
        print(guess_list)
        if guess == random_num:
            print("Congrats! You guessed it right. The no. is %d" %guess)
            break
        else:
            if i < (attempts - 1):
                if guess in guess_list:
                    print("You have already guessed %d" %guess)
                else:
                    if guess < random_num:
                        print("You guess is smaller than the choosen no")
                        guess_list.append(guess)
                    else:
                        print("You guess is bigger than the choosen no")
                        guess_list.append(guess)
            else:
                print("Sorry! you lost the game. The right no was %d" %random_num)
    except ValueError:
        print("Thats not a no.. Please enter only nos.")
    

        
