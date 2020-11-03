import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    gues = "_"*(len(word))
    i = random.randint(0, len(word) - 1)
    l = list(word)
    k = list(gues)
    k[i] = l[i]
    start = "".join(k)
    return start


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    i = original_word.count(char)
    j = answer_word.count(char)
    
    if i > j:
        return True
    else:
        return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    og = list(original_word)
    aw = list(answer_word)
    for i in range(len(original_word)):
        if og[i] == char and aw[i] == "_":
            aw[i] = og[i]
            break
    ans = "".join(aw)
    return ans


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("/----")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_______")
    if number_guesses == 3:
        print("/----")
        print("|   0")
        print("|")
        print("|")
        print("|")
        print("_______")
    if number_guesses == 2:
        print("/----")
        print("|   0")
        print("|  /|\\")
        print("|")
        print("|")
        print("_______")
    if number_guesses == 1:
        print("/----")
        print("|   0")
        print("|  /|\\")
        print("|   |")
        print("|")
        print("_______")
    if number_guesses == 0:
        print("/----")
        print("|   0")
        print("|  /|\\")
        print("|   |")
        print("|  / \\")
        print("_______")


# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    count = 5
    while count >= 0 and word != answer:
     if count != 0:
         guess = get_user_input()
     if guess == "exit" or guess == "quite":
         print("Bye!")
         return 0
     if count == 0:
         print("Sorry, you are out of guesses. The word was: " + word)
         return 0
     if is_missing_char(word, answer, guess):
         answer = do_correct_answer(word, answer, guess)
     else:
         count -= 1
         do_wrong_answer(answer, count)
    


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

