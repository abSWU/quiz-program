#Goal: Making an interactive program that simulates a multiple choice quiz.

class Question:
    def __init__(self,question,choices,answer):
        self.question = question
        self.choices = choices #Choices should be set with a list for multiple choice
        self.answer = answer

    
    def print_question(self):
        print(self.question)
        for c in self.choices: #Shows all the multiple choices
            print(c)

class Quiz:
    def __init__(self,topic,questions,score):
        self.topic = topic
        self.questions = questions
        self.score = score
    
    def start(self):
        print(f"Welcome to the {self.topic} quiz!")
        for q in self.questions:
            q.print_question()
            answer = input("What is the answer? (A/B/C/D): ").strip().upper() #Handles user input, watches out for formatting
            if(answer == q.answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
        
        print("Your score was", self.score,"/5!")
                
                


#Math question set
math_questions = [
                 Question("What is 5 x 5?",["A. 25", "B. 20", "C. 10", "D. 30"], "A"), 
                 Question("What is 60 / 5?",["A. 8", "B. 20", "C. 12", "D. 9"], "C"),
                 Question("What is (x^2 - 4) factored?",["A. (x+4)(x-1)", "B. (x-2)(x-2)", "C. (x+2)(x+2)", "D. (x+2)(x-2)"], "D"),
                 Question("What is the derivative of 3x^2 + 5x?",["A. 6x + 5", "B. x^3 + 5/2x^2", "C. 3x+5", "D. 5x+6"], "A"),
                 Question("What is 9+10?",["A. 19", "B. 21", "C. 10", "D. 30"], "B"),
                ]

#Science question set
science_questions = [
                 Question("What of the following is the smallest?",["A. Atoms", "B. Molecules", "C. Minerals", "D. Cells"], "A"), 
                 Question("What is the process of using sunlight as energy in plants called?",["A. Chlorophylisis ", "B. Necrosis", "C. Mitosis", "D. Photosynthesis"], "D"),
                 Question("When an atom is split into two, what is that process called?",["A. Nuclear Fusion", "B. Nucleic Dissolutin", "C. Nuclear Fission", "D. Nucleic Destruction "], "C"),
                 Question("What is the speed of light?",["A. 2.998 x 10^8 meters/s", "B. 6.626 x 10^26 meters/s", "C. 2.998 x 10^8 miles/s", "D. 6.022 x 10^8 miles/s"], "A"),
                 Question("What is the shape of the galaxy that Earth resides in?",["A. Peculiar", "B. Irregular", "C. Elliptical", "D. Spiral"], "D"),
                ]

#History question set
history_questions = [
                 Question("What was signed in 1776?",["A. The Treaty of Versailles", "B. The Declaration of Independence", "C. The Magna Carta", "D. The U.S. Constitution"], "B"), 
                 Question("Who were the major two nations involved in the Cold War?",["A. China and US", "B. USSR and Britain", "C. Vietnam and Japan", "D. US and USSR"], "D"),
                 Question("Which countries were the Axis Powers in World War 2?",["A. Japan, Italy, Germany", "B. US, USSR, Britain, France", "C. Italy, Germany, USSR", "D. Germany and Italy "], "A"),
                 Question("Which of the following inventions had the most impact on history?",["A. The Printing Press", "B. The Hot Air Balloon", "C. The Chainsaw", "D. The Axe"], "A"),
                 Question("Which two ideologies were the forefront of the Cold War?",["A. Democracy and Monarchs", "B. Monarchs and Communism", "C. Democracy and Communism", "D. Oligarchies and Communism"], "C"),
                ]




#In a loop so that if they put in a wrong input, they can do it again. Breaks from the loop if it is valid
while(True):
    while(True):

        #Select your mode/which quiz you want to do
        mode = input("Welcome! To start, pick which quiz you would like to do! (Math/Science/History)\n").capitalize().strip()

        #Put them into their respective quiz
        if (mode == "Math"):
            math = Quiz("Math",math_questions,0)
            math.start()
            break
        elif(mode == "Science"):
            science = Quiz("Science",science_questions,0)
            science.start()
            break
        elif(mode=="History"):
            history = Quiz("History",history_questions,0)
            history.start()
            break
        else:
            print("Please select a valid option!\n")
    
    #Ask if they want to go again
    go_again = input("Would you like to go again? (yes/no)\n").lower().strip()
    if(go_again =="yes"):
        continue 
    else:
        break 


