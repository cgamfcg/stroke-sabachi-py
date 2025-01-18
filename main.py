# boot
# --------------

import tkinter as tk
import tkinter.ttk as ttk
import sys

def stroke():
    sys.stdout.write("stroked!\n")
    nextValue = strokedCount.get() + 1
    strokedCount.set(nextValue)
    canvas.delete("del")
    canvas.create_image(100,100,image=imageFiles[nextValue%len(imageFiles)], tag="del")

root = tk.Tk()

root.title("demo")
root.geometry("400x400")

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, padx=20, pady=10)

# images
canvas = tk.Canvas(frame, bg="white", width=200, height = 200)
#canvas.place(x=0,y=0)
canvas.pack()

imageFiles = [
    tk.PhotoImage(file="resources/images/s-1.gif"),
    tk.PhotoImage(file="resources/images/s-2.gif"),
    tk.PhotoImage(file="resources/images/s-3.gif"),
    tk.PhotoImage(file="resources/images/s-4.gif"),
    tk.PhotoImage(file="resources/images/s-5.gif")
]
canvas.create_image(100,100,image=imageFiles[0], tag="del")

# buttons

button = ttk.Button(frame, text=u"撫でる！", command=stroke)
#button = ttk.Button(frame, text="Stroke!", command=stroke)
button.pack()

# labels
strokedCount = tk.IntVar(frame)
strokedCount.set(0)
label = ttk.Label(frame, textvariable=strokedCount)
label.pack()

root.mainloop()
