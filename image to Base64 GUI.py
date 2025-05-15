import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
import base64
import pyperclip

def convert_to_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

def on_drop(event):
    file_path = event.data.strip("{}")  # Remove curly braces from the path
    base64_string = convert_to_base64(file_path)
    output_field.config(state=tk.NORMAL)
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, base64_string)
    output_field.config(state=tk.DISABLED)
    copy_button.config(state=tk.NORMAL)
    confirm_label.config(text="")

def copy_to_clipboard():
    base64_string = output_field.get(1.0, tk.END).strip()
    pyperclip.copy(base64_string)
    confirm_label.config(text="✔ Copied!", fg="green")

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        base64_string = convert_to_base64(file_path)
        output_field.config(state=tk.NORMAL)
        output_field.delete(1.0, tk.END)
        output_field.insert(tk.END, base64_string)
        output_field.config(state=tk.DISABLED)
        copy_button.config(state=tk.NORMAL)
        confirm_label.config(text="")

# Initialize TkinterDnD window
root = TkinterDnD.Tk()
root.title("Image to Base64 Converter")

# Drag and drop area
drop_area = tk.Label(root, text="Drag and drop an image here or click 'Browse'", width=50, height=10, bg="lightgray")
drop_area.pack(pady=10)
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind("<<Drop>>", on_drop)

# Browse button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

# Output field
output_field = tk.Text(root, height=10, width=50, state=tk.DISABLED)
output_field.pack(pady=10)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

# Confirmation label
confirm_label = tk.Label(root, text="", fg="green")
confirm_label.pack()

# Run the application
root.mainloop()