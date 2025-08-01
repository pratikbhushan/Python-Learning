# Day 8: Caesar Cipher Project 🔐

Welcome to Day 8 of my #100DaysOfCode journey!  
Today’s challenge was to build a **Caesar Cipher** encoder and decoder using Python.  
It’s a classic encryption technique and a great way to strengthen string manipulation and logic-building skills.

---

## 🧠 What I Learned

- How to define and reuse functions in Python
- Looping through strings and lists
- Using modular arithmetic to wrap around alphabets
- Handling edge cases like large shift values and non-alphabet characters
- Making the user experience interactive through the console

---

## 🛠️ How It Works

The Caesar Cipher is a type of substitution cipher. Each letter in the text is shifted a certain number of places down or up the alphabet.  
For example, with a shift of 1:  
`A → B`, `B → C`, `C → D`, ..., `Z → A`

### ▶️ Features:
- Encode messages with any shift value
- Decode messages with the same shift
- Handles characters beyond 'z' (wrap-around logic)
- Allows repeated use until the user quits

---

## 📂 File Structure

```bash
Day8/
├── caesar_cipher.py     # Main project script
├── README.md            # Project overview (you’re reading it!)
