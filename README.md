# Quiz App with Tkinter GUI

A modern, interactive quiz application built with Python and Tkinter that fetches trivia questions from an external API and provides a user-friendly graphical interface for answering questions.

## 🎯 Features

- **Dynamic Question Loading**: Fetches random boolean (True/False) trivia questions from the Open Trivia Database API
- **Interactive GUI**: Clean, modern interface built with Tkinter
- **Real-time Score Tracking**: Live score updates as you progress through the quiz
- **Visual Feedback**: Color-coded feedback for correct/incorrect answers
- **Responsive Design**: Well-organized layout with buttons positioned at the bottom
- **HTML Entity Decoding**: Properly handles special characters in questions
- **Question Navigation**: Automatic progression through 10 trivia questions

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** - GUI framework
- **Requests** - API communication
- **HTML** - Text decoding utilities
- **Open Trivia Database API** - Question source

## 📋 Project Structure

```
api-Tkinter/
├── main.py           # Main application entry point
├── ui.py             # UI constants and theme configuration
├── quiz_brain.py     # Quiz logic and question management
├── question_model.py # Question data model
├── data.py           # Data handling utilities
└── images/           # UI assets
    ├── true.png      # True button icon
    └── false.png     # False button icon
```

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/quiz-app-tkinter.git
   cd quiz-app-tkinter
   ```

2. **Install dependencies**:
   ```bash
   pip install requests
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. Launch the application
2. Questions are automatically loaded from the trivia API
3. Read each question carefully
4. Click the **True** or **False** button to answer
5. Get immediate feedback on your answer
6. Track your score as you progress
7. Complete all 10 questions to see your final score

## 🔧 Key Components

- **Question Model**: Structured data representation for trivia questions
- **Quiz Brain**: Core logic for question management and scoring
- **UI Module**: Theme and styling configuration
- **API Integration**: Real-time question fetching from external trivia database

## 🌟 Future Enhancements

- [ ] Multiple choice questions support
- [ ] Category selection
- [ ] Difficulty level options
- [ ] High score tracking
- [ ] Timer functionality
- [ ] Sound effects
- [ ] Question history

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

---

**Enjoy testing your trivia knowledge!** 🧠✨
