Keylogger
Project Overview
This project is a **basic educational keylogger** developed as part of **Task-04** for the ProDigy InfoTech internship.  
The purpose of this project is to demonstrate how keystroke logging works in a **controlled and ethical environment**.

The program records keyboard inputs **only after explicit user consent** and saves them into a log file.

---

**Ethical Disclaimer**
This project is developed **strictly for educational purposes**.  
It does **not run silently**, does **not hide itself**, and should **only be used with full user knowledge and permission**.

Any misuse of keylogging techniques is unethical and illegal.

---

## Features
- Explicit user consent before logging starts
- Logs keystrokes into a text file (`keylog.txt`)
- Handles common keys such as:
  - Letters
  - Space
  - Enter
  - Special keys (e.g., Ctrl, Shift)
- Timestamped logging start
- Can be safely stopped using `Ctrl + C`

---

## How to Run the Project

### Create and activate a virtual environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
pip install pynput
python3 keylogger.py
```


## Usage Instructions
Run the script.

Read the ethical notice displayed in the terminal.

Enter Y to provide explicit consent.

Start typing — keystrokes will be logged in keylog.txt.

Press Ctrl + C to safely stop the program.

Conclusion

This project provides a safe and ethical demonstration of keystroke logging concepts while maintaining transparency and explicit user consent, in alignment with cybersecurity best practices.

Author

Yazeed Alghamdi
Cybersecurity Intern – ProDigy InfoTech
