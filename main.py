import tkinter as tk
from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        length = float(entry1.get())
        width = float(entry2.get())
        height = float(entry3.get())
        material = radiobutton_variable.get()
        density = 0

        if material == 1:
            density = 7.31
        elif material == 2:
            density = 11.35
        elif material == 3:
            density = 7.8
        elif material == 4:
            density = 0.92

        m = length * height * width * density
        result_label.config(text="Результат: " + str(m))

    except ValueError: 
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения для длины, ширины и высоты.")

root = tk.Tk()
root.title("ПР3")
root.geometry("500x250")

frame = tk.Frame(root)
frame.pack(expand=True)

label1 = tk.Label(frame, text="Длина:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

label2 = tk.Label(frame, text="Ширина:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)

label3 = tk.Label(frame, text="Высота:")
label3.grid(row=2, column=0)
entry3 = tk.Entry(frame)
entry3.grid(row=2, column=1)

radiobutton_variable = IntVar()
Radiobutton(frame, text="Олово",  variable=radiobutton_variable, value=1).grid(row=0, column=2, sticky='w')
Radiobutton(frame, text="Свинец", variable=radiobutton_variable, value=2).grid(row=1, column=2, sticky='w')
Radiobutton(frame, text="Сталь",  variable=radiobutton_variable, value=3).grid(row=2, column=2, sticky='w')
Radiobutton(frame, text="Лед",   variable=radiobutton_variable, value=4).grid(row=3, column=2, sticky='w')

button1 = tk.Button(frame, text="Рассчитать", command=calculate)
button1.grid(row=4, column=1)

result_label = tk.Label(frame, text="Результат: ")
result_label.grid(row=5, columnspan=3)

root.mainloop()
