import os.path

import compress
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, file_path)
def clean_path():
    path_entry.delete(0, tk.END)
def get_path():
    path = path_entry.get()

    if os.path.exists(path):
        scr_dir = compress.proccess_image(path)
        messagebox.showinfo("Успешно!", f"Картинка сохранена в папке output: {scr_dir}")
    else:
        messagebox.showwarning('Ошибка', "Ошибка в указании пути!")


root = tk.Tk()
root.title("Сжатие картинки")
root.geometry("400x100")
txt = tk.Label(text='Введите путь к картинке')
txt.pack()

path_entry = tk.Entry(root, width=40)
path_entry.pack(pady=5, padx=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Обзор", command=browse_file).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="OK", command=get_path).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text='Очистить', command=clean_path ).pack(side=tk.LEFT, padx=5)
root.mainloop()



