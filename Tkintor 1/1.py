import tkinter as tk
window = tk.Tk()
frame_M = tk.Frame(master = window, width = 400, height = 200, bg = "white smoke")
frame_M.pack()

label = tk.Label(master = frame_M,text="Конвектор валют",
                 font='Times 14',
                 fg="black",
                 bg="white smoke",
              width = 20,
              height = 1)
label.place(x=100,y=0)

label1 = tk.Label(master = frame_M, text = "укажите курс", bg = "white smoke")
label1.place(x=110,y=50)

label2 = tk.Label(master = frame_M, text = "1 Р =          ¥", bg = "white smoke")
label2.place(x=210,y=50)

label3 = tk.Label(master = frame_M, text = "Р       =          ¥", bg = "white smoke")
label3.place(x=160,y=100)

entry = tk.Entry(master = frame_M,width=3)
entry.place(x=245, y=50)
entry.insert(0,"0")

entry1 = tk.Entry(master = frame_M,width=9)
entry1.place(x=100, y=100)
entry1.insert(0,"0")

entry2 = tk.Entry(master = frame_M,width=9,state=tk.DISABLED)
entry2.place(x=240, y=100)

def but():
    entry2.configure(state="normal") 
    entry2.delete(0, tk.END)
    kof = float(entry.get())
    kol = float(entry1.get())
    entry2.insert(0,str(kof*kol))
    entry2.configure(state="disabled")

button = tk.Button(master = frame_M,
   text = "расчитать",
   width=20,
   height=1,
   bg="white",
   fg="black",
   command = but)
button.place(x = 123,y = 140)

window.mainloop()
