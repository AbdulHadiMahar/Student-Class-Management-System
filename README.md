# 🎓 Student Management System

A command-line **Student Management System** built with Python. This project allows users to manage student records, view student details, search students by roll number, update subject marks, calculate academic results, and remove student records.

It uses **Object-Oriented Programming (OOP)** to represent students and JSON file handling to store student information locally between program sessions.

## ✨ Features

- ➕ **Add Students:** Register students with their name, roll number, and subject marks.
- 👥 **View All Students:** Display the details of all registered students.
- 🔍 **Search Students:** Find a student using their roll number.
- ✏️ **Update Marks:** Modify marks in Maths, Physics, or Computer Science.
- 📊 **Calculate Results:** Calculate total marks and percentage out of 300.
- 🗑️ **Remove Students:** Remove a student from the class records using their roll number.
- 💾 **Save Data:** Store student records in a local JSON-formatted text file.
- 🔄 **Load Saved Data:** Load previously saved student records when the program starts.
- 🖥️ **Menu-Driven Interface:** Perform different operations through a simple command-line menu.

## 🛠️ Technologies Used

- **Python 3**
- `os` module — checks file existence and displays the file path.
- `json` module — saves and loads student records.
- **Object-Oriented Programming (OOP)** — uses a `Student` class and methods.
- **File Handling** — reads and writes student data.
- **Match-Case Statements** — handles menu options.

## 📋 Student Information

Each student record contains:

| Field | Description |
|---|---|
| Name | Student's full name |
| Roll Number | Unique student identifier |
| Maths Marks | Marks out of 100 |
| Physics Marks | Marks out of 100 |
| Computer Marks | Marks out of 100 |
| Total Marks | Sum of all three subjects |
| Percentage | Overall percentage out of 300 |

## 🚀 Getting Started

### Prerequisites

Install **Python 3.10 or newer** because the program uses `match-case` statements.

Check your Python version:

```bash
python --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Management-System.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Folder

```bash
cd Student-Management-System
```

### 3. Run the Program

If your Python file is named `main.py`, execute:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

No third-party libraries are required.

## 🎮 How to Use

When the program starts, a menu appears with the following options:

| Option | Action |
|---|---|
| `1` | Add a student |
| `2` | View all students |
| `3` | Search for a student by roll number |
| `5` | Update a student's subject marks |
| `6` | Calculate and display a student's result |
| `9` | Remove a student by roll number |
| `0` | Save student records and exit |

### Example: Adding a Student

Enter the student's name, roll number, and marks in Maths, Physics, and Computer.

### Example: Calculating Results

The program calculates the total marks and percentage using these formulas:

**Total Marks**

```text
Total = Maths + Physics + Computer
```

**Percentage**

```text
Percentage = (Total Marks / 300) × 100
```

For example, if a student scores 80 in Maths, 75 in Physics, and 90 in Computer:

- Total Marks: 245 out of 300
- Percentage: 81.67%

## 💾 Data Storage

The program stores student records in a file named `Studentclass.txt`.

Although the extension is `.txt`, the file contains JSON-formatted data. It is created or updated when the user selects option `0` to save and exit.

On the next launch, the program attempts to load the saved records automatically.

Example data structure:

```json
{
    "Ali": {
        "name": "Ali",
        "roll": 101,
        "mmarks": 80,
        "pmarks": 75,
        "cmarks": 90
    }
}
```

## 📂 Project Structure

```text
Student-Management-System/
├── main.py
├── Studentclass.txt
└── README.md
```

`Studentclass.txt` is generated when the program saves student records. You can include a sample data file in your repository if you want to demonstrate how persistence works.

## 🧠 Concepts Practiced

This project demonstrates practical use of:

- Classes and objects.
- Constructors and instance attributes.
- Methods for displaying student details and results.
- Dictionaries and lists.
- Loops and conditional statements.
- Pattern matching with `match-case`.
- Exception handling.
- JSON serialization and deserialization.
- File reading and writing.
- Basic record management and calculations.

## 🔮 Future Improvements

- Validate marks to ensure they are between 0 and 100.
- Prevent duplicate student names and roll numbers.
- Add stronger input validation for invalid numbers.
- Save changes automatically after adding, updating, or removing a student.
- Fix menu and search edge cases.
- Add sorting and filtering options.
- Include grades and pass/fail status.
- Create a graphical user interface (GUI).
- Add a database such as SQLite for more reliable data management.

## 👨‍💻 Author

Developed as a Python learning project to practice Object-Oriented Programming, file handling, JSON, and menu-driven applications.

## 📄 License

This project is available for educational and personal learning purposes. Add an open-source license, such as the MIT License, if you want to formally permit others to use, modify, and distribute the code.
