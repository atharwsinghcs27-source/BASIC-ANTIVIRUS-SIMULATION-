# 🛡️ Basic Antivirus Simulation

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Cyber Security](https://img.shields.io/badge/Cyber-Security-red?style=for-the-badge)
![Virus Scanner](https://img.shields.io/badge/Antivirus-Simulation-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

</p>

<p align="center">
A Python-based Basic Antivirus Simulation that scans files for suspicious patterns, detects potential threats using predefined malware signatures, and generates scan reports in a simple command-line interface.
</p>

---

# 📌 Project Overview

The **Basic Antivirus Simulation** is a beginner-friendly cybersecurity project developed in Python to demonstrate how antivirus software performs basic malware detection.

Instead of using complex machine learning or signature databases, this project scans files against predefined suspicious signatures to identify potential threats and classify files as **Safe** or **Infected**.

The project is designed for educational purposes and helps understand the fundamental concepts behind antivirus software.

---

# ✨ Features

- 🔍 Scan individual files
- 📁 Scan entire folders
- 🚨 Detect suspicious malware signatures
- ✅ Safe file identification
- 📄 Generate scan reports
- 📊 Display scan summary
- ⚡ Fast scanning
- 💻 Command Line Interface (CLI)
- 🛡️ Lightweight antivirus simulation
- 📂 Easy to extend with new signatures

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python 3 | Programming Language |
| OS Module | File Handling |
| Hashlib | File Hashing |
| Regular Expressions | Pattern Matching |
| VS Code | Development |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```
Basic_Antivirus_Simulation/
│
├── antivirus.py
├── scanner.py
├── signatures.py
├── report.txt
├── requirements.txt
├── README.md
├── LICENSE
│
├── test_files/
│   ├── safe_file.txt
│   ├── infected_file.txt
│   └── suspicious.exe
│
└── screenshots/
    ├── home.png
    ├── scanning.png
    └── report.png
```

---

# 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Basic-Antivirus-Simulation.git
```

### Navigate to the Project Folder

```bash
cd Basic-Antivirus-Simulation
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python antivirus.py
```

or

```bash
python main.py
```

(depending on your project structure)

---

# 💻 Usage

1. Launch the application.
2. Select a file or folder to scan.
3. The scanner checks files against predefined malware signatures.
4. Results are displayed in the terminal.
5. A scan report is generated automatically.

---

# 🔍 Detection Process

The antivirus simulation follows these steps:

1. Read file contents.
2. Compare against known malicious signatures.
3. Detect suspicious patterns.
4. Mark file as:
   - ✅ Safe
   - 🚨 Infected
5. Generate report.

---

# 📷 Screenshots

## Home Screen

```
screenshots/home.png
```

---

## Scanning Files

```
screenshots/scanning.png
```

---

## Scan Report

```
screenshots/report.png
```

---

# 📊 Sample Output

```
=============================
Basic Antivirus Simulation
=============================

Scanning...

File: test_files/sample.exe

Status:
Threat Detected

Malware Signature:
EICAR-Test-File

Action:
File Flagged Successfully

Scan Completed.
```

---

# 📈 Future Improvements

- 🧠 Machine Learning Detection
- 🔐 SHA-256 Hash Verification
- ☁️ VirusTotal API Integration
- 🗂️ Real-time File Monitoring
- 🛡️ Quarantine Folder
- 🗑️ Delete Infected Files
- 📊 GUI Dashboard
- 📧 Email Notifications
- ⚡ Scheduled Scans
- 🌐 Cloud Signature Database

---

# 🎯 Learning Outcomes

This project demonstrates:

- File Handling in Python
- Malware Signature Detection
- Pattern Matching
- Basic Cybersecurity Concepts
- Hashing Techniques
- Report Generation
- Command-Line Applications
- Python Modules
- Defensive Security Fundamentals

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 👨‍💻 Author

## Atharw Ansh Singh

**B.Tech Computer Science Engineering (Cyber Security)**

- 💻 GitHub: https://github.com/atharwsinghcs27-source
- 🔗 LinkedIn: https://linkedin.com/in/yourprofile
- 📧 Email: atharv482ansh@gmail.com

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and personal purposes.

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It motivates me to build more cybersecurity and Python projects.

---

<p align="center">

**Made with ❤️ by Atharw Ansh Singh**

</p>
