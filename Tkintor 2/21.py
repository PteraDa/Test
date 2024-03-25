from calendar import c
import tkinter as tk
window = tk.Tk()

frame_q = tk.Frame(master = window, width = 800, height = 200)
frame_q.pack(fill=tk.BOTH)

frame_w = tk.Frame(master = window, width = 800, height = 200)
frame_w.pack(fill=tk.BOTH)


frame_1 = tk.Frame(master = frame_q, width = 400, height = 200, bg = "white smoke")
frame_1.pack(fill=tk.BOTH,side=tk.LEFT)

def click1():
    window1 = tk.Toplevel()
    window1.title("Зима")
    window1.geometry("450x200")
    label=tk.Label(window1, text="Зима́ — одно из четырёх времён года, между осенью и весной.",font='Times 12')
    label.pack(anchor="n", expand=1)
    window1.grab_set()
    def click11():
        window1.destroy()
    
    button11 = tk.Button(master = window1,
                        font='Times 14',
                        text = "Назад",
                        width=20,
                        height=1,
                        bg="white",
                        fg="black",
                        command = click11)
    button11.pack(anchor="s", expand=1)
    

    
button1 = tk.Button(master = frame_1,
   font='Times 14',
   text = "Зима",
   width=20,
   height=1,
   bg="white",
   fg="black",
   command = click1)
button1.place(x=95,y=75)

frame_2 = tk.Frame(master = frame_q, width = 400, height = 200, bg = "white smoke")
frame_2.pack(fill=tk.BOTH,side=tk.RIGHT)

def click2():
    window2 = tk.Toplevel()
    window2.title("Весна")
    window2.geometry("450x200")
    label=tk.Label(window2, text="Весна́ — одно из четырёх времён года, между зимой и летом.",font='Times 12')
    label.pack(anchor="n", expand=1)
    window2.grab_set()
    def click21():
        window2.destroy()
    
    button21 = tk.Button(master = window2,
                        font='Times 14',
                        text = "Назад",
                        width=20,
                        height=1,
                        bg="white",
                        fg="black",
                        command = click21)
    button21.pack(anchor="s", expand=1)

button2 = tk.Button(master = frame_2,
   font='Times 14',
   text = "Весна",
   width=20,
   height=1,
   bg="white",
   fg="black",
   command = click2)
button2.place(x=95,y=75)

frame_3 = tk.Frame(master = frame_w, width = 400, height = 200, bg = "white smoke")
frame_3.pack(fill=tk.BOTH,side=tk.LEFT)

def click3():
    window3 = tk.Toplevel()
    window3.title("Лето")
    window3.geometry("450x200")
    label=tk.Label(window3, text="Ле́то — одно из четырёх времён года, между весной и осенью.",font='Times 12')
    label.pack(anchor="n", expand=1)
    window3.grab_set()
    def click31():
        window3.destroy()
    
    button31 = tk.Button(master = window3,
                        font='Times 14',
                        text = "Назад",
                        width=20,
                        height=1,
                        bg="white",
                        fg="black",
                        command = click31)
    button31.pack(anchor="s", expand=1)

button3 = tk.Button(master = frame_3,
   font='Times 14',
   text = "Лето",
   width=20,
   height=1,
   bg="white",
   fg="black",
   command = click3)
button3.place(x=95,y=75)

frame_4 = tk.Frame(master = frame_w, width = 400, height = 200, bg = "white smoke")
frame_4.pack(fill=tk.BOTH,side=tk.RIGHT)

def click4():
    window4 = tk.Toplevel()
    window4.title("Осень")
    window4.geometry("450x200")
    label=tk.Label(window4, text="Осень - одно из четырёх времён года, между летом и зимой.",font='Times 12')
    label.pack(anchor="n", expand=1)
    window4.grab_set()
    def click41():
        window4.destroy()
    
    button41 = tk.Button(master = window4,
                        font='Times 14',
                        text = "Назад",
                        width=20,
                        height=1,
                        bg="white",
                        fg="black",
                        command = click41)
    button41.pack(anchor="s", expand=1)

button4 = tk.Button(master = frame_4,
   font='Times 14',
   text = "Осень",
   width=20,
   height=1,
   bg="white",
   fg="black",
   command = click4)
button4.place(x=95,y=75)





window.mainloop()
