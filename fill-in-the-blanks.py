
#easy-mode
driver_knowledge_test = ["When you're going to drive it is important to always put on your ___1___, including your passengers.",
                        "If there are no lanes marked on the road, you should drive in the ___2___ side of the road.",
                        "It's getting dark and the sun is fading, you should turn on the ___3___.",
                        "Before driving on a freeway, you should make sure you have enough ___4___, oil, water and the correct tyre pressure."]
answer_1 = ['seatbelts', 'left', 'light', 'fuel']


#medium-mode
general_food_test = ["All fruits have ___1___ in them. That's what makes them different from vegetables.",
                    "You shouldn't drink coffee or ___2___ when you're going to sleep. It keeps you up at night.",
                    "It is not safe to eat ___3___ undercooked. It might be contaminated with a bacteria called Salmonella.",
                    "The essentials to make a cake are flour, ___4___, vanilla extract, unsalted butter and egg."]
answer_2 = ['seeds', 'tea', 'chicken', 'sugar']

#hard-mode
general_health_test = ["An ___1___ a day, keeps the doctor away.",
                        "Too much dietary intake of health-supplemnets can be ___2___ for you. However, it is unlikely.",
                        "You can check your pulse on the wrist, ___3___, and thigh.",
                        "The averag amount of ___4___ adults need is 7-9 hours."]
answer_3 = ['apple', 'harmful', 'neck', 'sleep']

blank_space = ["___1___", "___2___", "___3___", "___4___"]



#Inputs raw_input's name
#Outputs introduction with user's name
def Intro(name_of_player):
    print "Hello " + name_of_player + ", we are going to play fill-in-the-blanks! Topics revolve around our everyday live, so don't worry if you didn't study much."
    print "Please note the game is case-sensitive. i.e. all capslock must be disabled."
    print "Let's get started, pick a difficulty."

#returns user's choice of list
def beginning_of_game(player_difficulty):
    #while True: #unnecessary
    if player_difficulty == "easy":
        print "You chose 'easy'\n"
        return driver_knowledge_test, answer_1 #use return function
    elif player_difficulty == "medium":
        print "You chose 'medium'\n"
        return general_food_test, answer_2
    elif player_difficulty == "hard":
        print "You chose 'hard'\n"
        return general_health_test, answer_3



#checks user input correct answer, and print out their progress. If user input incorrect, prompts to re-try
# CUTTING CODES: are my old codes commented out. I'd like to keep a reminder what I went wrong or how
#All index add-on at the same time, so I use 'global_index' to represent all
# I made my codes more efficient. You can just ignore it.
def answer_check(answer, sentence, blank_space):
    new_list = []
    global_index = 0
    #index = 0
    #sentence_index = 0
    #answer_index = 0
    #blank_index = 0
    # CUTTING CODES - answered_list_index = 0
    total_of_sentence = 4 #the number of elements in the sentence list.
    while global_index < total_of_sentence: #for iindex
        print sentence[global_index] #for sentence_index
        player_answer = raw_input("\nType your answer for " + blank_space[global_index] + " \n>>>") #for blank_index
        if player_answer.lower() == answer[global_index]: #for answer_index
            # CUTTING CODES - new_list.append(sentence[sentence_index])
            # CUTTING CODES - new_list.append(answered_list[answered_list_index])
            #current fill-in-the-blanks that's been already answered
            print sentence[global_index].replace(blank_space[global_index], answer[global_index]) #for sente, blank_index, answer_index
            # CUTTING CODES - new_list.append(sentence[sentence_index])
            #n CUTTING CODES - ew_list[sentence_index].replace(blank_space[blank_index], answer[answer_index])
            new_list.append(sentence[global_index].replace(blank_space[global_index], answer[global_index])) #for sentence_index, blank_index, answer_index
            # CUTTING CODES - answered_list_index += 1
            #answer_index += 1
            #sentence_index += 1
            #index += 1
            #blank_index += 1
            global_index += 1
            print "\nCCORRECT! \n"
        else:
            print "Wrong! Try again. :) \n"
    print new_list
    return "\nCongratulation! You completed the game!"




#inputs None
#Outputs whole program-functions
def fill_in_the_blanks():
    name_of_player = raw_input("enter your name \n>>>")
    Intro(name_of_player)

    difficulty_selection = raw_input("\nselect from easy, medium, or hard \n>>>")

    while difficulty_selection not in ["easy", "medium", "hard"]:
        difficulty_selection = raw_input("\nselect from easy, medium, or hard \n>>>")
        #if difficulty_selection != "easy" or difficulty_selection != "medium" or difficulty_selection != "hard":
        print "The difficulty does not exist. Try again."

    sentence, answers = beginning_of_game(difficulty_selection)
    print sentence

    answer_check(answers, sentence, blank_space)



    print "\nThank you for playing!"









#initiate game from here.
fill_in_the_blanks()
