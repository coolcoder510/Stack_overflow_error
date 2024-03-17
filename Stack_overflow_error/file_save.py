import tkinter as tk
from tkinter import messagebox
import os
# Create the main window

def close_program():
    root.destroy()

def save_text():
    code = code_text.get("1.0", "end-1c")
    file_path = r"C:\Users\hp\Downloads\Compressed\Stack_Overflow_Parser-master\Stack_overflow_error\test.py"
    
    try:
        with open(file_path, "w") as file:
            file.write(code)
        messagebox.showinfo("Success", "Text saved successfully!")
        close_program()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Save Text to File")

# Create a text box for entering code
code_text = tk.Text(root, height=10, width=50)
code_text.pack(pady=10)

# Create a button to save the text
save_button = tk.Button(root, text="Save", command=save_text)
save_button.pack()

# Run the Tkinter event loop
root.mainloop()
