from tkinter import *
from tkinter.messagebox import *
from math import sin, cos, pi, exp


def Final(event):
    ''' Завершаем работу '''
    window_deleted()


def window_deleted():
    ''' Завершаем работу по [X]'''
    if askyesno("Выход", "Завершить работу?"):
        root.destroy()


def showXY(event):
    global ID1, ID2
    x = event.x
    y = event.y
    ent0.delete(0, END)
    ent0.delete(0, END)
    ent0.insert(0, str(round(Xmin + x/Kx, 2)))
    ent1.insert(0, str(round(Ymin + (MaxY - y)/Ky, 2)))
    cv.delete(ID1)
    cv.delete(ID2)
    ID1 = cv.create_line(0, y, MaxX, y, dash=(3, 5))
    ID2 = cv.create_line(x, 0, x, MaxY, dash=(3, 5))


if __name__ == "__main__":
    root = Tk()
    root.title("Графика")

    root.protocol('WM_DELETE_WINDOW', window_deleted)
    root.resizable(False, False)

    Kp = 0.7
    MaxX = root.winfo_screenwidth() * Kp
    MaxY = root.winfo_screenheight() * Kp

    cv = Canvas(root, width=MaxX, height=MaxY, bg="white")
    cv.grid(row=0, columnspan=9)
    cv.bind("<Button-1>", showXY)

    Xmin = -10.0
    Xmax = 10.0
    Ymin = -5.0
    Ymax = 5.0
    Xmid = 0
    Ymid = 0

    dY = 1.0
    dX = 1.0

    ID1 = 0
    ID2 = 0

    Kx = MaxX / abs((Xmax - Xmin))
    Ky = MaxY / abs((Ymax - Ymin))

    lba0 = Label(root, text="X:", width=10, fg="blue", font="Ubutu, 12")
    lba0.grid(row=1, column=0, sticky='e')
    ent0 = Entry(root, width=5, font="Ubuntu, 12")
    ent0.grid(row=1, column=1, sticky='w')
    ent0.insert(0, 0)
    lba1 = Label(root, text="Y:", width=10, fg="blue", font="Ubutu, 12")
    lba1.grid(row=2, column=0, sticky='e')
    ent1 = Entry(root, width=5, font="Ubuntu, 12")
    ent1.grid(row=2, column=1, sticky='w')
    ent1.insert(0, 0)
    lba2 = Label(root, text="Xmin:", width=10, fg="blue", font="Ubutu, 12")
    lba2.grid(row=1, column=2, sticky='e')
    ent2 = Entry(root, width=5, font="Ubuntu, 12")
    ent2.grid(row=1, column=3)
    ent2.insert(0, Xmin)
    lba3 = Label(root, text="Xmax:", width=10, fg="blue", font="Ubutu, 12")
    lba3.grid(row=1, column=4, sticky='e')
    ent3 = Entry(root, width=5, font="Ubuntu, 12")
    ent3.grid(row=1, column=5)
    ent3.insert(0, Xmax)
    lba4 = Label(root, text="Ymin:", width=10, fg="blue", font="Ubutu, 12")
    lba4.grid(row=2, column=2, sticky='e')
    ent4 = Entry(root, width=5, font="Ubuntu, 12")
    ent4.grid(row=2, column=3)
    ent4.insert(0, Ymin)
    lba5 = Label(root, text="Ymax:", width=10, fg="blue", font="Ubutu, 12")
    lba5.grid(row=2, column=4, sticky='e')
    ent5 = Entry(root, width=5, font="Ubuntu, 12")
    ent5.grid(row=2, column=5)
    ent5.insert(0, Ymax)
    lba6 = Label(root, text="Шаг меток:", width=10, fg="blue", font="Ubutu, 12")
    lba6.grid(row=1, column=6, sticky='e')
    ent6 = Entry(root, width=5, font="Ubuntu, 12")
    ent6.grid(row=1, column=7)
    ent6.insert(0, dX)
    lba7 = Label(root, text="Смещение:", width=10, fg = "blue", font = "Ubutu, 12")
    lba7.grid(row=2, column=6, sticky='e')
    ent7 = Entry(root, width=5, font="Ubuntu, 12")
    ent7.grid(row=2, column=7)
    ent7.insert(0, dY)
    btn1 = Button(root, width=20, bg="#ccc", text="Рисовать")
    btn1.grid(row=1, column=8)
#    btn1.bind("<Button-1>", Draw)
    btn2 = Button(root, width=20, bg="#ccc", text="Выход")
    btn2.grid(row=2, column=8)
    btn2.bind("<Button-1>", Final)

#    cv.create_arc(Xmin, Ymin, Xmax, Ymax, start=0, extent=359, outline="#f11", fill="#1f1", width=2)

    root.mainloop()
