import tkinter as ttk
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox 


window=Tk()
window.title('Registration')
window.geometry('700x450')
#Создание пространства в окне
frame=Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)#True--->занимает все пространство
#Создание копии класса Label--->1)где находится, 2)другие штуки, в данном случае текст
method_lbl=Label(
    frame,
    text='Выбери категорию пользователя: '
)
method_lbl.grid(row=1, column=1)#Размещение в окне
#Методы, которые принимает Combobox
methods=['арендатор',
         'арендодатель']
#'readonly' говорит о том, что пользователь не может менять методы
combobox=Combobox(frame, values=methods, width=30, state='readonly')
combobox.grid(row=2, column=1)
combobox.set('арендатор')#что стоит в окне по умолчанию
#combobox.bind('<<ComboboxSelected>>', selected)#1)--хз, 2) функция, которой передает результат Combobox при выборе метода










window.mainloop()
