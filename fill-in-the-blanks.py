
#easy-mode
driver_knowledge_test = ("When you're going to drive it is important to always put on your ___1___, including your passengers.",
                        "If there are no lanes marked on the road, you should drive in the ___2___ side of the road.",
                        "It's getting dark and the sun is fading, you should turn on the ___3___.",
                        "Before driving on a freeway, you should make sure you have enough ___4___, oil, water and the correct tyre pressure.")
answer_1 = ['seatbelts', 'left', 'light', 'fuel']
#medium-mode
general_food_test = ("All fruits have ___1___ in them. That's what makes them different from vegetables."
                    "You shouldn't drink coffee or ___2___ when you're going to sleep. It keeps you up at night."
                    "It is not safe to eat ___3___ undercooked. It might be contaminated with a bacteria called Salmonella."
                    "The essentials to make a cake are flour, ___4___, vanilla extract, unsalted butter and egg.")
answer_2 = ['seeds', 'tea', 'chicken', 'sugar']

#hard-mode
general_health_test = ("An ___1___ a day, keeps the doctor away."
                        "Too much dietary intake of can be ___2___ for you. However, it is unlikely."
                        "You can check your pulse on the wrist, ___3___, and thigh."
                        "The averag amount of ___4___ adults need is 7-9 hours.")
anwser_3 = ['apple', 'harmful', 'neck', 'sleep']

blank_space = ["___1___", "___2___", "___3___", "___4___"]

#This function checks if the sentence string has the substring you specify.


def beginning_of_game():
    while True:
        difficulty_selection = raw_input("easy/ medium/ hard >>>")
        if difficulty_selection == "easy":
            return driver_knowledge_test #use return function
        elif difficulty_selection == "medium":
            return general_food_test
        elif difficulty_selection == "hard":
            return general_health_test
        else:
            print "The following difficulty does not exist. Try again!"

#This should load the answer for the following difficulty.
def answer_for_difficulty():
    player_choice = beginning_of_game()
    if player_choice == driver_knowledge_test:
        return answer_1
    elif player_choice == general_food_test:
        return answer_2
    elif player_choice == general_health_test:
        return answer_3


def finding_blank(blank_space, type_of_quiz):
    for ea_substring in type_of_quiz:
        if ea_substring in answer:
            return ea_substring
    return None

def fill_in_the_blanks(blank_space, type_of_quiz, answer):
    print beginning_of_game()
    new_sentence = []
    index = 0
    blank_space_index = 0
    answer = answer_for_difficulty()
    #everytime you enter an answer, it will prompt for answer again until you get it right.
    while index < len(type_of_quiz):
        print type_of_quiz
        user_input = raw_input("Type in answer for" + blank_space[blank_space_index] + ": ")
        if user_input == answer:
            index += 1
            blank_space_index += 1
    else:
        print "Wrong! Try again!"

#replacing blank space with substring answer
#replacement = fill_in_the_blanks(blank_space, type_of_quiz, answer)
#if finding_blank(blank_space, type_of_quiz) != None:
#    word = word.replace(replacement, user_input)





#initiate game from here.
print "Hello"
name = raw_input("what is your name? ")
print "Hello " + name + ", we are going to play fill-in-the-blanks! Topics revolve around our everyday live, so don't worry if you didn't study much."
print "Please note the game is case-sensitive. i.e. all capslock must be disabled."
print "Let's get started, pick a difficulty."
print beginning_of_game()
