import tkinter as tk
from tkinter import font
from random import shuffle
import pygame
import threading

# load sound effects 
sound_1 = pygame.mixer.Sound('sounds/background audio.mp3')

# Play sound effects
pygame.time.delay(4000)
sound_1.play()
# Time Delay 
pygame.time.delay(2000)
sound_1.play()



class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Game")

    
        custom_font = font.Font(family="Helvetica", size=14)

    
        self.questions = [
            {
                "question": "1) What is the primary function of an adder circuit?",
                "options": ["Logical manipulation", "Electrical transmission", "Multiplication of digits", "Addition of digits"],
                "answer": "Addition of digits"
            },
            {
                "question": "2) Which component of the CPU extensively uses adders?",
                "options": ["GPU", "ALU", "RAM", "Cache"],
                "answer": "ALU"
            },
            {
                "question": "3) What type of addition do the majority of adders handle?",
                "options": ["Decimal additiion", "Binary addition", "Hexadecimal addition", "Octal addition"],
                "answer": "Binary addition"
            },
            {
                "question": "4) What is the output of the carry bit in a half-adder when both inputs are 1??",
                "options": ["0", "1", "Depends on the implementation", "Cannot be determined"],
                "answer": "0"
            },
            {
                "question": "5) How many binary inputs and outputs does a half-adder have?",
                "options": [" 1 input, 1 output", " 2 inputs, 1 output", "2 inputs, 2 outputs", " 1 input, 2 outputs"],
                "answer": "2 inputs, 1 output"
            },
            {
                "question": "6) What is the basic component used in a full adder to calculate the sum?",
                "options": ["OR gate", "AND gate", "XOR gate", "NOT gate"],
                "answer": "XOR gate"
            },
            {
                "question": "7) How many inputs does a full adder have?",
                "options": ["2", "3", "4", "1"],
                "answer": "3"
            },
            {
                "question": "8) What is the function of a decoder in a digital circuit?",
                "options": ["Performs addition", " Detects specific bit patterns", "Generates carry bits", "Converts binary to decimal"],
                "answer": "Detects specific bit patterns"
            },
            {
                "question": "9)What is the primary purpose of a look-ahead carry adder?",
                "options": [" Minimize output carry delay", "Maximize output carry delay", " Reduce the number of gates", "Increase the ripple delay"],
                "answer": " Minimize output carry delay"
            },
            {
                "question": "10) How many output lines does a 4-bit decoder have?",
                "options": ["2", "4", "8", "16"],
                "answer": "16"
            },
        ]

        self.score = 0
        self.current_question = 0

       
        self.question_label = tk.Label(self.root, text="", font=custom_font, wraplength=600)
        self.question_label.pack(pady=20)

        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=custom_font, width=40, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        
        self.score_label = tk.Label(self.root, text="Score: 0", font=custom_font)
        self.score_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            options = question["options"]
            shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            self.end_game()

    def check_answer(self, selected_option):
        question = self.questions[self.current_question]
        selected_answer = question["options"][selected_option]
        correct_answer = question["answer"]

        if selected_answer == correct_answer:
            self.score += 1
            result_message = "You are correct!"
        else:
            result_message = f"Wrong! The correct answer is: {correct_answer}"

        result_label = tk.Label(self.root, text=result_message)
        result_label.pack()

        self.current_question += 1
        self.score_label.config(text="Score: {}".format(self.score))

        # Destroy the result message label after 3 seconds
        self.root.after(3000, result_label.destroy)
        self.next_question()

    def end_game(self):
        # Display final score
        score_message = "Final Score: {}/{}".format(self.score, len(self.questions))
        self.question_label.config(text=score_message)

        # Disable option buttons
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

        # Play Again button
        play_again_button = tk.Button(self.root, text="Play Again", font=("Arial", 12), command=self.play_again)
        play_again_button.pack(pady=10)

    def play_again(self):
        self.score = 0
        self.current_question = 0
        self.score_label.config(text="Score: 0")
        self.next_question()

        # Re-enable option buttons
        for button in self.option_buttons:
            button.config(state=tk.NORMAL)



# Create the main application window
root = tk.Tk()


# Start playing background audio

# Create an instance of the QuizGame class
quiz_game = QuizGame(root)

# Start the Tkinter event loop
root.mainloop()
