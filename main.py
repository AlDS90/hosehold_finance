import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sq


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.add_img = tk.PhotoImage(file='img/add.png').subsample(15, 15)
        btn_open_dilog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dilog, bg='#d7d8e0', bd=0,
                                   compound=tk.TOP, image=self.add_img)
        btn_open_dilog.pack(side=tk.LEFT)
        self.tree = ttk.Treeview(columns=('id', 'description', 'costs', 'total'), height=15, show='headings')
        self.tree.column('id', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)
        self.tree.heading('id', text='id')
        self.tree.heading('description', text='наименование')
        self.tree.heading('costs', text='Статья дохода/расхода')
        self.tree.heading('total', text='Сумма')
        self.tree.pack()

    def open_dilog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Добавить доходы/расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = ttk.Label(self, text='Наименование:')
        label_description.place(x=50, y=50)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        label_combobox = ttk.Label(self, text='Статья дохода/расхода')
        label_combobox.place(x=50, y=80)
        self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        label_money = ttk.Label(self, text='Сумма')
        label_money.place(x=50, y=110)
        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Household finance')
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    app.mainloop()
