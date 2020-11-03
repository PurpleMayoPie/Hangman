#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    f = open(file_name, "r")
    wlist = f.readlines()
    
    """
    TODO: Step 1 - open file and read lines as words
    """
    return (wlist)


def select_random_word(words):
    i = random.randint(0, len(words) - 1)
    word = words[i]
    j = random.randint(0, len(word) - 2)
   
    wlist = list(word)
    wlist[j] = '_'
    word = "".join(wlist)
    print("Guess the word: " +word )
    """
    TODO: Step 2 - select random word from list of file
    """
    return words[i]



def get_user_input():
    ans = input("Guess the missing letter: ")
    """
    TODO: Step 3 - get user input for answer
    """
    return (ans)


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: ' +word)


if __name__ == "__main__":
    run_game('short_words.txt')

