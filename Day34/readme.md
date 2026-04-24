# Quizzler: Intelligent Trivia Engine 🧠

A dynamic, GUI-based trivia application built with Python that fetches real-time questions from the Open Trivia Database. This project serves as a showcase for advanced Object-Oriented Programming (OOP) and the integration of desktop graphical interfaces with remote web APIs.

## 📌 Project Overview
Quizzler is built on a modular architecture designed for scalability and maintainability. The application pulls fresh trivia content via an API, sanitizes HTML-encoded strings in real-time, and provides a polished user experience through a custom-built Tkinter interface.

## 🚀 Key Features
* **Dynamic API Integration:** Automatically fetches a fresh set of 10 random True/False questions per session via the Open Trivia Database.
* **Robust OOP Architecture:** Implements a strict "Separation of Concerns" by decoupling the User Interface from the core Logic.
* **Interactive GUI:** Features a custom Tkinter interface with real-time score tracking and visual feedback (color transitions) for user interactions.
* **Data Sanitization:** Utilizes the `html` library to unescape complex strings (e.g., converting `&quot;` to `"`) for a clean UI.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **GUI Framework:** Tkinter
* **Networking:** `requests` library
* **Data Source:** Open Trivia Database (OpenIDB)
* **Design Pattern:** Object-Oriented Programming (OOP)

## 📁 Project Architecture
The project is structured into distinct modules to ensure a clean codebase:

* **`main.py`**: The central entry point. It initializes the data, creates the question bank, and launches the application.
* **`ui.py`**: The View layer. Contains the `QuizInterface` class, managing all canvas elements, buttons, and visual feedback loops.
* **`quiz_brain.py`**: The Controller/Logic layer. Manages the internal state, score tracking, question indexing, and answer validation.
* **`question_model.py`**: The Data Model. Defines the blueprint for individual Question objects.
* **`data.py`**: The Data Fetcher. Handles the initial API request and returns the raw JSON results.

## ⚙️ Setup & Execution

### 1. Prerequisites
Ensure you have Python 3.x installed on your system. This project requires the `requests` library:

```bash
pip install requests

### 2. Running the Application
Navigate to the project directory and execute the main file:

```bash
python main.py