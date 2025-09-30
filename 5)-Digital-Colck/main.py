# Digital clock -- GUI-

# import modules --
import tkinter as tk
from time import strftime

# display and title -
root = tk.Tk()
root.title('Digital Clock')

# 
frame = tk.Frame(root, bg="black", bd=10, relief="ridge")
frame.pack(padx=20, pady=20)

def time():
    string = strftime('%H : %M : %S %p\n %A, %d %B %Y')
    label.config(text=string)
    label.after(1000, time)

#
label = tk.Label(frame, font=('calibri', 40, 'bold'),
                 background='skyblue', foreground='black',
                 padx=20, pady=20)
label.pack(anchor='center')

time()
root.mainloop()
 