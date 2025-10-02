from question_model import Question
from quiz_brain import QuizBrain
import requests
import tkinter as tk
import ui
import html
params={
    "amount":10 , 
    "type":"boolean",
}

#build the quiz interface
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x500")
root.config(background=ui.THEME_COLOR)

#score tracker
score_label = tk.Label(root , text="Score: 0" , bg=ui.THEME_COLOR, fg="white", font=("Arial", 14, "bold"))
score_label.pack(pady=20)

#question label (create once and reuse)
question_label = tk.Label(root, text="Loading questions..." , font=("Arial", 16, "italic"), wraplength=300, justify="center", bg="white", fg=ui.THEME_COLOR, padx=20, pady=20)
question_label.pack(expand=True)

#create buttons
true_image = tk.PhotoImage(file="./images/true.png")
false_image = tk.PhotoImage(file="./images/false.png")

# Create a frame for buttons at the bottom
button_frame = tk.Frame(root, bg=ui.THEME_COLOR)
button_frame.pack(side="bottom", pady=20)

true_button = tk.Button(button_frame, image=true_image, text="True", highlightthickness=0)
false_button = tk.Button(button_frame, image=false_image, text="False", highlightthickness=0)

true_button.pack(side="left", padx=20)
false_button.pack(side="right", padx=20)



#get the questions from the API
response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
question_data = response.json()["results"]

# print(question_data)
question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])  # Decode HTML entities
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

def update_display():
    """Update the question display and score"""
    if quiz.still_has_questions():
        quiz.next_question()  # Move to next question and set current_question
        question_label.config(text=quiz.current_question.text, fg=ui.THEME_COLOR)  # Reset color
        score_label.config(text=f"Score: {quiz.score}")
        # Enable buttons
        true_button.config(state="normal")
        false_button.config(state="normal")
    else:
        # Quiz finished
        question_label.config(text="You've completed the quiz!", fg=ui.THEME_COLOR)
        score_label.config(text=f"Final Score: {quiz.score}/{quiz.question_number}")
        # Disable buttons
        true_button.config(state="disabled")
        false_button.config(state="disabled")

def answer_question(user_answer):
    """Handle answer selection"""
    if quiz.current_question:
        # Disable buttons temporarily
        true_button.config(state="disabled")
        false_button.config(state="disabled")
        
        # Process the answer
        is_correct = quiz.check_answer(user_answer)
        
        # Show feedback briefly (optional)
        if is_correct:
            question_label.config(text="Correct! ✓", fg="green")
        else:
            question_label.config(text=f"Wrong! ✗\nCorrect answer: {quiz.current_question.answer}", fg="red")
        
        # Update display after a short delay
        root.after(1500, update_display)

# Configure button commands
true_button.config(command=lambda: answer_question("True"))
false_button.config(command=lambda: answer_question("False"))

# Start the quiz by displaying first question
update_display()

root.mainloop()
