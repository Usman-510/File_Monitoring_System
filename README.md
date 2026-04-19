# File_Monitoring_System
File Integrity Monitoring System using SHA256
# Project Overview
This is a Python-based **File Integrity Monitoring System that detects unauthorized changes in files using **SHA256 hashing**.
It continuously monitors a selected file and alerts the user if any modification is detected.
This project is built for **cybersecurity learning purposes** and demonstrates how hashing can be used for data integrity verification.
 Problem Statement
Files stored in a computer system can be modified, corrupted, or tampered with by viruses, malware, or unauthorized users.
There is a need for a simple system that can detect such changes in real time.
Objectives
* Monitor file integrity in real time
* Detect unauthorized file changes
* Understand SHA256 hashing in cybersecurity
* Implement a simple security monitoring tool using Python
# Technologies Used
* Python 
* Tkinter (GUI) 
* hashlib (SHA256 hashing) 
* threading (background monitoring) 
* time module 
## ⚙️ Working Principle
1. User selects a file
2. System generates SHA256 hash of the file
3. Hash is stored as reference
4. File is continuously monitored in the background
5. New hash is generated at intervals
6. If hash changes → file is modified
7. System shows an alert to the user
## Features
* Simple and user-friendly GUI
* Real-time file monitoring
* Secure SHA256-based integrity checking
* Background processing using threading
* Instant alert system for file changes
## 🔐 Security Concept

This project uses **SHA256 hashing**, a cryptographic function that converts file data into a fixed-length string.
Even a small change in the file produces a completely different hash, making it ideal for integrity checking.
## 👨‍💻 Author
**Muhammad Usman**
Roll No: BITF24A015
Punjab University College of Information Technology
## 📌 Note

This project is developed for educational purposes to understand file integrity monitoring and basic cybersecurity concepts.
