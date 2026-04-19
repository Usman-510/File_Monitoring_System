import hashlib
import time
import threading
import tkinter as tk
from tkinter import filedialog

selected_file = ""
running = False


def get_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    file_label.config(text=selected_file)

def start_monitoring():
    global running

    if not selected_file:
        log_box.insert(tk.END, "Please select a file first\n")
        return

    running = True
    log_box.insert(tk.END, "Monitoring started...\n")

    threading.Thread(target=monitor_file, daemon=True).start()

def stop_monitoring():
    global running
    running = False
    log_box.insert(tk.END, "Monitoring stopped\n")

def monitor_file():
    global running

    try:
        old_hash = get_hash(selected_file)
    except:
        log_box.insert(tk.END, "File not found or cannot read\n")
        return

    while running:
        try:
            new_hash = get_hash(selected_file)

            if new_hash != old_hash:
                log_box.insert(tk.END, "⚠ FILE CHANGED!\n")
                old_hash = new_hash
            else:
                log_box.insert(tk.END, "✔ File safe\n")

            time.sleep(3)

        except:
            log_box.insert(tk.END, "File not found\n")
            break


root = tk.Tk()
root.title("File Integrity Monitor")
root.geometry("600x500")  
root.configure(bg="black")


try:
    root.iconbitmap("logo.ico")
except:
    print("Icon not found")

title = tk.Label(
    root,
    text="FILE INTEGRITY MONITOR",
    bg="black",
    fg="white",
    font=("Arial", 22, "bold")   
)
title.pack(pady=15)

file_label = tk.Label(
    root,
    text="No file selected",
    bg="black",
    fg="gray",
    font=("Arial", 12)
)
file_label.pack(pady=5)

btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=15)

tk.Button(
    btn_frame,
    text="SELECT FILE",
    command=select_file,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    height=2
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="START",
    command=start_monitoring,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    height=2
).grid(row=0, column=1, padx=10)

tk.Button(
    btn_frame,
    text="STOP",
    command=stop_monitoring,
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    height=2
).grid(row=0, column=2, padx=10)

log_box = tk.Text(
    root,
    bg="black",
    fg="green",
    font=("Consolas", 11)   
)
log_box.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()