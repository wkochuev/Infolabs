import tkinter as ttk
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox 

def clear_extra_widgets():
    for widget in frame.winfo_children():
        if widget not in global_widgets:
            widget.destroy()

def selected(event):
    selection=combobox.get()
    if selection=='арендатор':
        method_arendat()
    elif selection=='арендодатель':
        method_arendodat()

def method_arendat():
    login_lbl=Label(
        frame,
        text='Введите логин:'
    )
    login_lbl.grid(row=3, column=1, pady=10)
    #Entry- это виджет, создающий поле для ввода
    login_ent=Entry(
        frame#,
        #state="disabled"- отключает поле ввода
    )
    login_ent.grid(row=3, column=2)
    #base_ent.focus()- позволяет автоматически установить фокус на конкретное поле, в данном случае base_ent

    password_lbl=Label(
        frame,
        text='Введите пароль:'
    )
    password_lbl.grid(row=4, column=1, pady=10)
    password_ent=Entry(
        frame
    )
    password_ent.grid(row=4, column=2)


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
combobox.bind('<<ComboboxSelected>>', selected)#1)--хз, 2) функция, которой передает результат Combobox при выборе метода
global_widgets = frame.winfo_children()

window.mainloop()