
#easy-mode
driver_knowledge_test = ["When you're going to drive it is important to always put on your ___1___, including your passengers.",
                        "If there are no lanes marked on the road, you should drive in the ___2___ side of the road.",
                        "It's getting dark and the sun is fading, you should turn on the ___3___.",
                        "Before driving on a freeway, you should make sure you have enough ___4___, oil, water and the correct tyre pressure."]
answer_1 = ['seatbelts', 'left', 'light', 'fuel']
answered_list_1 = ["When you're going to drive it is important to always put on your seatbelts, including your passengers.",
                    "If there are no lanes marked on the road, you should drive in the left side of the road.",
                    "It's getting dark and the sun is fading, you should turn on the light. ",
                    "Before driving on a freeway, you should make sure you have enough fuel, oil, water and the correct tyre pressure."]

#medium-mode
general_food_test = ["All fruits have ___1___ in them. That's what makes them different from vegetables."
                    "You shouldn't drink coffee or ___2___ when you're going to sleep. It keeps you up at night."
                    "It is not safe to eat ___3___ undercooked. It might be contaminated with a bacteria called Salmonella."
                    "The essentials to make a cake are flour, ___4___, vanilla extract, unsalted butter and egg."]
answer_2 = ['seeds', 'tea', 'chicken', 'sugar']
answered_list_2 = ["All fruits have seeds in them. That's what makes them different from vegetables."
                    "You shouldn't drink coffee or tea when you're going to sleep. It keeps you up at night."
                    "It is not safe to eat chicken undercooked. It might be contaminated with a bacteria called Salmonella."
                    "The essentials to make a cake are flour, sugar, vanilla extract, unsalted butter and egg."]

#hard-mode
general_health_test = ["An ___1___ a day, keeps the doctor away."
                        "Too much dietary intake of can be ___2___ for you. However, it is unlikely."
                        "You can check your pulse on the wrist, ___3___, and thigh."
                        "The averag amount of ___4___ adults need is 7-9 hours."]
anwser_3 = ['apple', 'harmful', 'neck', 'sleep']
answered_list_3 = ["An apple a day, keeps the doctor away."
                        "Too much dietary intake of can be harmful for you. However, it is unlikely."
                        "You can check your pulse on the wrist, neck, and thigh."
                        "The averag amount of sleep adults need is 7-9 hours."]

blank_space = ["___1___", "___2___", "___3___", "___4___"]



#Inputs raw_input's name
#Outputs introduction with user's name
def Intro(name_of_player):
    print "Hello " + name_of_player + ", we are going to play fill-in-the-blanks! Topics revolve around our everyday live, so don't worry if you didn't study much."
    print "Please note the game is case-sensitive. i.e. all capslock must be disabled."
    print "Let's get started, pick a difficulty."

#returns user's choice of list
def beginning_of_game(player_difficulty):
    while True:
        if player_difficulty == "easy":
            print "You chose 'easy'"
            return driver_knowledge_test, answer_1, answered_list_1 #use return function
        elif player_difficulty == "medium":
            print "You chose 'medium'"
            return general_food_test, answer_2, answered_list_2
        elif player_difficulty == "hard":
            print "You chose 'hard'"
            return general_health_test, answer_3, answered_list_3
        else:
            print "The following difficulty does not exist. Try again!"

#checks user input correct answer, and print out their progress.
def answer_check(answer, sentence, blank_space, answered_list):
    new_list = []
    index = 0
    sentence_index = 0
    answer_index = 0
    blank_index = 0
    answered_list_index = 0
    while index < 4: # '4' is the number of elements in the sentence list.
        print sentence[sentence_index]
        player_answer = raw_input("\nType your answer for " + blank_space[blank_index] + " \n>>>")
        if player_answer.lower() == answer[answer_index]:
            #new_list.append(sentence[sentence_index])
            new_list.append(answered_list[answered_list_index])
            print new_list
            answered_list_index += 1
            answer_index += 1
            sentence_index += 1
            index += 1
            blank_index += 1
            #print replace_the_blank(answer, sentence, blank)
            print "CCORRECT! \n"
        else:
            print "Wrong! Try again. :) \n"
    return "Congratulation! You completed the game!"




#inputs None
#Outputs whole program-functions
def fill_in_the_blanks():
    name_of_player = raw_input("enter your name \n>>>")
    Intro(name_of_player)

    difficulty_selection = raw_input("\nselect from easy, medium, or hard \n>>>")

    if difficulty_selection == "easy" or difficulty_selection == "medium" or difficulty_selection == hard:
        sentence, answers, answered_sentence = beginning_of_game(difficulty_selection)
        print sentence

        answer_check(answers, sentence, blank_space, answered_sentence)

        print "\nThank you for playing!"









#initiate game from here.
fill_in_the_blanks()
