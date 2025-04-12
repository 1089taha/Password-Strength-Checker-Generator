# 🔐 Password Strength Checker & Generator

[![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)

A sleek and interactive web application to evaluate password strength and generate secure passwords. Built with Python and Streamlit, this tool empowers users to enhance their online security with ease.

## ✨ Features

- **Password Strength Analysis**: Checks passwords for:
  - Length (≥8 characters)
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- **Visual Feedback**: Displays strength via a progress bar (Weak, Medium, Strong).
- **Improvement Suggestions**: Offers actionable tips to strengthen weak passwords.
- **Password Generator**: Creates secure, randomized passwords based on user input.
- **User-Friendly Interface**: Clean design with masked password input for privacy.
- **Responsive**: Works seamlessly on desktop and mobile browsers.

## 🛠️ Tech Stack

- **Python 3.8+**: Core language for logic and processing.
- **Streamlit**: Framework for building the interactive web UI.
- **Standard Python Libraries**:
  - `random`: For generating random characters.
  - `string`: For character sets (letters, digits, punctuation).
  - `re`: For potential regex-based validation (extensible).
- **Git**: Version control for project management.

## 🔍 How It Works

### Password Strength Checker
- Evaluates your password against five criteria, assigning a score from 0 to 5.
- Provides a progress bar and color-coded feedback:
  - 🔴 Weak (0–2)
  - 🟡 Medium (3–4)
  - 💪 Strong (5)
- Lists suggestions if the password needs improvement (e.g., "Add numbers").

### Password Generator
- Takes your input password as a base (optional).
- Adds missing character types to meet all strength criteria.
- Ensures a minimum length of 8 characters.
- Randomly shuffles characters to produce a secure password.

## 🖥️ Installation

Get the app running locally in just a few steps!

### Prerequisites
- Python 3.8 or higher
- Git
- A terminal or command prompt

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/1089taha/Password-Strength-Checker-Generator.git
   cd Password-Strength-Checker-Generator

2. **Set Up a Virtual Environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:
   ```bash
   pip install streamlit

4. Run the Application:
   ```bash
   streamlit run app.py

5. Open the App:

Navigate to http://localhost:8501 in your browser.