import matplotlib.pylab as plt
import random
from tkinter import *
from tkinter import messagebox, Frame
from tkinter import colorchooser


def plot(*args):
    entry2.config(state='disabled')
    plt.plot(x_point, y_point, )
    plt.show()


def choice_color():
    global pri_c, sec_c
    x = messagebox.askyesno("background color", "do you want to chang background color for the program ?? ")
    if x:
        x = colorchooser.askcolor()
        pri_c = x[1]
        item = [welcome_label, m, root, button_frame, home_frame, info_label, first_frame]
        for i in item:
            i.config(bg=pri_c)

    else:
        x2 = messagebox.askyesno("button color", "do you want to chang primary color for the program ?? ")
        if x2:
            try:
                c = colorchooser.askcolor()
                sec_c = c[1]
                item = [start_btn, color_btn, start_btn, btn_1, btn_2, btn_3, btn_4]
                for i in item:
                    i.config(bg=sec_c)

                word = [welcome_label, label1, label2]
                for i in word:
                    i.config(fg=sec_c)
                entry1.config(highlightcolor=sec_c)
                entry2.config(highlightcolor=sec_c)
            except:
                pass


def home():
    global start_btn, home_frame, button_frame, info_label, color_btn

    item_frame.destroy()
    root.bind("<Return>", "")
    home_frame = Frame(first_frame, bg=pri_c)
    info_label = Label(home_frame, text=my_text, font=font(14), bg=pri_c, fg='white')

    button_frame = Frame(home_frame, bg=pri_c)
    start_btn = Button(button_frame, text='Back', font=font(18), command=sc_fr_ge, bg=sec_c, fg='black', width=12,
                       activeforeground=sec_c, activebackground='#222222')
    color_btn = Button(button_frame, text='Color choice', font=font(18), command=choice_color, bg=sec_c, fg='black',
                       width=12,
                       activeforeground=sec_c, activebackground='#222222')

    home_frame.pack()
    info_label.pack(pady=50, anchor='center')
    button_frame.pack()
    start_btn.grid(row=1, column=1, padx=10)
    color_btn.grid(row=1, column=2, padx=10)


def restart():
    global x_point, y_point, count
    x_point, y_point = [], []

    entry1.config(state='normal')
    entry2.config(state='normal')
    entry1.delete(0, END)
    entry2.delete(0, END)
    count = 0

    messagebox.showinfo("Restart", "restart complete you can start from the beginning")
    root.bind("<Return>", show)
    btn_1.config(command=show, text='Next point')


def show(*args):
    global count
    try:
        if int(entry1.get()) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return messagebox.showerror("error", 'inter only positive integer number more than 1 \nin number of point')

        try:
            num = entry2.get().split(',')
            if len(num) != 2:
                messagebox.showerror("error", 'inter only two number with \n'
                                              'x and y axis')
            else:
                entry1.config(state='disabled')
                x_point.append(eval(num[0]))
                y_point.append(eval(num[1]))
                count += 1
                entry2.delete(0, END)
                if count == int(entry1.get()):
                    entry2.config(state='disabled')
                    btn_1.config(text='Show', command=plot)
                    root.bind("<Return>", plot)

        except SyntaxError:
            messagebox.showerror("invalid input", 'pleas inter the correct input in his form')

        except ValueError:
            messagebox.showerror("error", "inter only number in the x , y axis")
    except ValueError:
        messagebox.showerror("error", 'inter only positive integer number more than 1 \nin number of point')


def sc_fr_ge():
    global sec_frame, entry1, entry2, x_point, info_label, start_btn2, wel_frame, home_frame, btn_1
    global btn_2, btn_3, btn_4, y_point, count, btn_1, label1, label2, item_frame

    def grid_item(it, r, c):
        return it.grid(row=r, column=c)

    x_point, y_point, count = [], [], 0
    wel_frame.destroy()
    try:
        home_frame.destroy()

    except:
        pass

    item_frame = Frame(first_frame, bg=pri_c)
    label1 = Label(item_frame, text='how many point you want ', font=font(20), fg=sec_c, bg=pri_c, padx=20, pady=10)
    entry1 = Entry(item_frame, width=7, font=font(20), highlightcolor=sec_c, highlightthickness=4)
    label2 = Label(item_frame, text='x & y for the point like 7 , 8', fg=sec_c, font=font(18), bg=pri_c, padx=20,
                   pady=10)
    entry2 = Entry(item_frame, width=7, font=font(20), highlightcolor=sec_c, highlightthickness=4)

    btn_1 = Button(item_frame, width=15, text='Next point', font=font(17), command=show, bg=sec_c,
                   activeforeground=sec_c, activebackground='#222222')
    btn_2 = Button(item_frame, width=15, text='Exit', font=font(17), command=root.destroy, bg=sec_c,
                   activeforeground=sec_c, activebackground='#222222')
    btn_3 = Button(item_frame, width=15, text='Restart', font=font(17), command=restart, bg=sec_c,
                   activeforeground=sec_c, activebackground='#222222')
    btn_4 = Button(item_frame, width=15, text='Home', font=font(17), command=home, bg=sec_c, activeforeground=sec_c,
                   activebackground='#222222')

    item_frame.pack(pady=70)
    grid_item(label1, 1, 1)
    grid_item(entry1, 1, 2)
    grid_item(label2, 2, 1)
    grid_item(entry2, 2, 2)
    root.bind("<Return>", show)
    btn_1.grid(row=3, column=1, pady=30)
    btn_2.grid(row=3, column=2, pady=30)
    btn_3.grid(row=4, column=1, pady=5)
    btn_4.grid(row=4, column=2, pady=5)


pri_c = 'black'
sec_c = 'green'
my_text = 'Hi my name is haider and i\'m the designer of this program \n' \
         '  this program have writen with python language \n' \
         '  this program will generate a plot with matplotlib library have \n' \
         '  a number of point you will deside how many \n' \
         '  then will insert the number of point in the x & y axis , mack \n' \
         '  sure you will follow the step correctly:\n' \
         'first \\\ inter the int number of how many point you want to draw in the plot \n' \
         f'second \\\ inter the number in x and y axis for every point like  {random.randrange(0, 10)} , {random.randrange(0, 10)} \n and press next point or <enter> with your keyboard.\n' \
         'third \\\ press the show button to see the plot !\n \n' \
         'you can press Restart to start a gene or Exit to close the program !!'

wel_text = 'Welcome every one , i hope you will enjoy in this program \n' \
           'mack sure to contact me to develop it !!'

x_point = []
y_point = []
count = 0


def font(s):
    return "consolas", s, "bold"


root = Tk()
root.config(bg=pri_c)
root.geometry('800x600')
root.title("matplotlib designer !!")
root.resizable(False,False)

welcome_label = Label(root, text="Welcome", font=font(55), fg=sec_c, bg=pri_c)
m = Message(root, text=wel_text, width=800, font=font(18), bg=pri_c, fg='white')
welcome_label.pack(pady=10)
m.pack(anchor='center')

first_frame = Frame(root, bg=pri_c)
wel_frame = Frame(first_frame, bg=pri_c)
start_btn = Button(wel_frame, text='Start', font=font(24), command=sc_fr_ge, bg='green', fg='black', width=6,
                   activeforeground=sec_c, activebackground='#222222')

first_frame.pack()
wel_frame.pack(pady=20, anchor='center')
start_btn.pack()

root.mainloop()
