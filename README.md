# 🔐 My Password Manager

Welcome to the Password Manager! This is a secure, private vault that locks your passwords away on your own computer using strong encryption.

You don't need to be a computer programmer to get this running. Just follow the simple recipes below step-by-step!

---

## 🛠️ First-Time Setup Instructions

Before running the app for the very first time, you need to do a quick 3-minute setup to prepare your computer.

### Step 1: Open your Terminal

- **On a Mac:** Press `Command + Space`, type `Terminal`, and press Enter.
- **On Windows:** Click the Start menu, type `cmd` or `Command Prompt`, and press Enter.
- Navigate to this project folder (e.g., type `cd ` followed by dragging and dropping your project folder into the terminal window, then press Enter).

### Step 2: Create a Virtual Environment (The Python Box)

Think of this as setting up a clean, isolated workspace just for this app so it doesn't mess with any other files on your computer. Run this command:

```bash
python3 -m venv .venv
```

### Step 3: Turn on the Workplace

Now, tell your computer to start using that isolated workspace.

- **On Mac / Linux:** Run this command:

```bash
  source .venv/bin/activate

```

- **On Windows:** Run this command:

```bash
  .venv\Scripts\activate

```

_(You will know it worked if you see `(.venv)` appear at the very beginning of your terminal line!)_

### Step 4: Install the Helper Tools

Run this command to automatically install the extra tools the app needs to scramble and protect your passwords:

```bash
pip install -r requirements.txt

```

---

## 🔑 How to Set Your Master Password

Your **Master Password** is the master key to your vault. If anyone else gets ahold of your project, they won't be able to open it without this key.

Because of security rules, your real password is hidden away in a secret folder file that Git completely ignores. Here is how to create yours on a new machine:

1. Look at the files inside this project folder and find a file named **`.env.example`**.
2. **Duplicate** that file (Copy and Paste it).
3. **Rename** the copy to exactly **`.env`** (Make sure there is a dot `.` at the front, and no `.txt` or `.example` at the end).
4. Open that new `.env` file with any text editor (like Notepad, TextEdit, or VS Code).
5. Change the line to your custom password. **Do not use spaces or quotation marks.**

It should look exactly like this(Make sure it is in very first line):

MASTER_PASSWORD=YourSecretPassword123!

6. **Save and close** the file.

---

## 🚀 How to Launch the App

Whenever you want to use your password manager in the future, just open your terminal to this folder and run:

```bash
python3 passwordManager.py

```

1. Type in your **Master Password** when prompted.
2. Type `add` to save a new password, or `view` to retrieve your saved passwords!
3. Type `q` when you are ready to lock up and quit.

⚠️ **Important Note:** A file named `src.txt` will automatically appear once you save your first password. This is your encrypted vault. **Do not delete it**, or your saved passwords will be lost!

```

```
