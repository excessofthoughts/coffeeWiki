import tkinter as tk
import file_connection
from tkinter import messagebox

species = file_connection.opening()
info = None

def reader():
    global info
    qwe = aaa.curselection()
    if qwe:
        titles = aaa.get(qwe)
        info = titles
        texts.delete(1.0, tk.END)
        texts.insert(tk.END, species[titles])
        megatitle.config(text=titles)
        megatitle.pack()
        texts.pack()
        btn_read.pack_forget()
        btn_add.pack_forget()
        btn_del.pack_forget()
        iacb.pack()
def back():
    global info
    info = None
    texts.delete(1.0, tk.END)
    megatitle.config(text='')
    megatitle.pack_forget()
    texts.pack_forget()
    iacb.pack_forget()
    aaa.pack(fill=tk.BOTH)
    btn_read.pack()
    btn_del.pack()
    btn_add.pack()
def deleting():
    global info, species, aaa
    qwe = aaa.curselection()
    if qwe:
        titles = aaa.get(qwe)
        info = titles
        warning = messagebox.askyesno('Удаление.','Действительно ли вы хотите удалить статью?')
        if warning:
            back()
            del species[titles]
            aaa.delete(qwe)
            file_connection.delete(titles)
def adding():
    global species
    def saving():
        new_qwe = name.get()
        new_ne_qwe = article.get('1.0', tk.END)
        if new_qwe and new_ne_qwe:
            if new_qwe in species:
                warn = messagebox.showerror('Ошибка!','Такое имя уже существует!')
                return
            species[new_qwe] = new_ne_qwe
            aaa.insert(0, new_qwe)
            file_connection.add(new_qwe, new_ne_qwe)
            new_win.destroy()
            reader()
    new_win = tk.Toplevel(win)
    new_win.title('Добавить статью')
    new_win.geometry('500x600')
    l = tk.Label(new_win, text='Введите название статьи (название специи):')
    name = tk.Entry(new_win)
    arts = tk.Label(new_win, text='Введите статью:')
    article = tk.Text(new_win, wrap=tk.WORD)
    btn_save = tk.Button(new_win, text='Сохранить', command=saving)
    l.pack()
    name.pack()
    arts.pack()
    article.pack()
    btn_save.pack()

win = tk.Tk()
win.geometry('600x600')
win.title('CoffeeWiki')
win.config(bg='wheat')

megatitle = tk.Label(win, text='')
texts = tk.Text(win)
btn_read = tk.Button(win, text='Прочитать', command=reader)
btn_add = tk.Button(win, text='Добавить', command=adding)
btn_del = tk.Button(win, text='Удалить', command=deleting)
iacb = tk.Button(win, text='<--', command=back)
aaa = tk.Listbox(win)
for i in species:
    aaa.insert(tk.END, i)
label = tk.Label(win, text='')
megatitle.pack()
megatitle.pack_forget()
label.pack()
aaa.pack(fill=tk.BOTH)
texts.pack()
texts.pack_forget()
btn_read.pack()
iacb.pack()
iacb.pack_forget()
btn_add.pack()
btn_del.pack()
win.mainloop()
