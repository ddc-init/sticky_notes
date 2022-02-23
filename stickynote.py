from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
# from tkinter import font

notes_quantity = 1
width = 500
height = 300


class StickyNotes(Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.xclick = 0
        self.yclick = 0

        # master (root) window
        self.overrideredirect(True)
        global notes_quantity
        self.geometry(str(width) + 'x' + str(height) + '+' + str(1000 + notes_quantity * (-30)) + '+' + str(
            100 + notes_quantity * 20))
        # self.geometry('300x300+' + str(1000+notes_quantity*(-30)) + '+' + str(100 + notes_quantity*20))
        self.config(bg='#838383')
        self.attributes('-topmost', 'true')
        self.resizable(True, True)

        # titlebar
        self.titlebar = Frame(self, bg='#F8F796', relief='flat', bd=2)
        self.titlebar.bind('<Button-1>', self.get_pos)
        self.titlebar.bind('<B1-Motion>', self.move_window)
        self.titlebar.pack(fill=X, expand=1, side=TOP)

        self.closebutton = Label(self.titlebar, text='X', bg='#F8F7B6', relief='flat')
        self.closebutton.bind('<Button-1>', self.quit_window)
        self.closebutton.pack(side=RIGHT)

        self.newbutton = Label(self.titlebar, text='^', bg='#F8F7B6', relief='flat')
        self.newbutton.pack(side=RIGHT)
        self.newbutton.bind('<Button-1>', self.reduce_window_to_title)

        self.newbutton = Label(self.titlebar, text='+', bg='#F8F7B6', relief='flat')
        self.newbutton.pack(side=LEFT)
        self.newbutton.bind('<Button-1>', self.another_window)

        # main text area
        self.mainarea = tkst.ScrolledText(self, bg='#FDFDCA', font=('Comic Sans MS', 14, 'italic'), relief='flat',
                                          padx=5, pady=10)
        self.mainarea.pack(fill=BOTH, expand=1)

        # frames to introduce shadows
        self.shadow = Frame(self).pack(side=BOTTOM)
        self.shadow = Frame(self).pack(side=RIGHT)

        notes_quantity += 1

    def get_pos(self, event):
        self.xclick = event.x
        self.yclick = event.y

    def move_window(self, event):
        self.geometry('+{0}+{1}'.format(event.x_root - self.xclick, event.y_root - self.yclick))

    def another_window(self, event):
        sticky = StickyNotes(root)

    def reduce_window_to_title(self, event):
        self.geometry(str(width) + 'x' + str(height) + '+' + str(1000 + notes_quantity * (-30)) + '+' + str(
            100 + notes_quantity * 20))

    def enlarge_window(self, event):
        self.geometry('100x100+' + str(1000 + notes_quantity * (-30)) + '+' + str(100 + notes_quantity * 20))

    def quit_window(self, event):
        self.topWindow = Toplevel(root)
        self.closebutton.config(relief='flat', bd=0)
        if messagebox.askyesno('Delete Note?', 'Are you sure you want to delete this note?', parent=self):
            global notes_quantity
            self.destroy()
            notes_quantity -= 1
            if notes_quantity == 1:
                root.destroy()
            return
        self.closebutton.config(relief='flat', bd=0, bg='#F8F7B6')


root = Tk()
root.withdraw()
# make the first note.
sticky = StickyNotes(root)
root.mainloop()
