# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 17:37:29 2021

@author: lajamu
"""

import openpyxl
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import os

def process_file(input_file, output_file):
    letters = []
    for i in range(65, 91):
        letters.append(chr(i))

    for i in range(6):
        letters.append(letters[0] + letters[i])

    plate1536 = []

    for i in range(1, 49):
        for letter in letters:
            plate1536.append(letter + str(i))

    wb = openpyxl.load_workbook(filename=input_file)
    ws = wb.active

    vals = []

    for col in ws.iter_cols(max_row=32):
        for cell in col:
            vals.append(cell.value)

    source_dict = {1: "A1", 2: "A2", 3: "A3", 4: "B1", 5: "B2", 6: "B3"}

    transfers = [["Source Well", " Destination Well", "Transfer Volume"]]

    for s, d in zip(vals, plate1536):
        if s != None:
            transfers.append([source_dict[s], d, 250])

    with open(output_file, "w", newline="") as outputcsv:
        echoWriter = csv.writer(outputcsv, delimiter=",")
        for t in transfers:
            echoWriter.writerow(t)

def on_drop(event):
    file_path = event.data
    # Remove curly braces if present (Windows drag-drop format)
    if file_path.startswith('{') and file_path.endswith('}'):
        file_path = file_path[1:-1]

    if not file_path.endswith('.xlsx'):
        messagebox.showerror("Error", "Please drop an .xlsx file")
        return

    # Generate default output filename
    base_name = os.path.basename(file_path)[:-5]  # Remove .xlsx
    default_output = base_name + "_ECHO.csv"

    # Ask user where to save
    output_file = filedialog.asksaveasfilename(
        defaultextension=".csv",
        initialfile=default_output,
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    if output_file:
        try:
            process_file(file_path, output_file)
            messagebox.showinfo("Success", f"File saved to:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process file:\n{str(e)}")

# Create GUI
root = TkinterDnD.Tk()
root.title("ECHO Paint CSV Generator")
root.geometry("400x200")

label = tk.Label(root, text="Drag and drop .xlsx file here",
                 font=("Arial", 14),
                 bg="lightgray",
                 relief="solid",
                 borderwidth=2)
label.pack(expand=True, fill="both", padx=20, pady=20)

# Enable drag and drop
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_drop)

root.mainloop()