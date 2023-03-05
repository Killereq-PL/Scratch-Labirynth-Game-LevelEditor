from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

SavingImages = ["wall", "empty", "lava", "player", "win"]

Saved = ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"]

file = None

def browseFiles():
    if ErrorLabelVariable.get() == "ERROR: Cannot have more than one player at the same time!":
        ErrorLabelVariable.set("")
    global file
    global Saved
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("All files",
                                                        "*.*")))
    file = open(filename, "r")
    file_data = file.read()
    Saved = file_data.splitlines()
    for col in range(10):
        for row in range(8):
            i = col * 8 + row + 1  # calculate button number
            i -= 1
            img = TKimages[SavingImages.index(Saved[i])]
            buttons[i].config(image=img)

def get_button(t): # button press
    global ErrorLabelVariable
    button_index = int(t) - 1
    x = buttons[button_index].cget("image")
    if x == "pyimage2":
     buttons[button_index].config(image=TkEmptyImage)
     Saved[button_index] = "empty"
    elif x == "pyimage3":
     buttons[button_index].config(image=TkLavaImage)
     Saved[button_index] = "lava"
    elif x == "pyimage4":
     if Saved.count("player") > 0:
         ErrorLabelVariable.set("ERROR: Cannot have more than one player at the same time!")
         buttons[button_index].config(image=TkPlayerImage)
         Saved[button_index] = "player"
     else:
         buttons[button_index].config(image=TkPlayerImage)
         Saved[button_index] = "player"
    elif x == "pyimage5":
     if Saved.count("player") > 1:
         ErrorLabelVariable.set("")
     buttons[button_index].config(image=TkWinImage)
     Saved[button_index] = "win"
    elif x == "pyimage6":
     buttons[button_index].config(image=TkWallImage)
     Saved[button_index] = "wall"

def new_file():
    if ErrorLabelVariable.get() == "ERROR: Cannot have more than one player at the same time!":
        ErrorLabelVariable.set("")
    global Saved
    Saved = ["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"]
    for x in buttons:
        x.config(image=TkWallImage)

def save_file():
    if Saved.count("player") > 1:
        messagebox.showerror(title="Error detected", message="Error saving: Cannot have more than one player at the same time!")
    else:
        f = asksaveasfile(initialfile = 'CustomLevel.txt', 
                          defaultextension=".txt",
                          filetypes=[("Text Files","*.txt")])
        f.mode = 'a'              
        for y in range(len(Saved)):  
            if y != 0:
                f.write('\n')        
            f.write(Saved[y])

root = Tk()
root.iconphoto(False, PhotoImage(file='Assets\\icon.png'))

root.title('Level Editor')
root.resizable(0, 0)
root.geometry("475x425")

root.config(background = "white")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=browseFiles)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

WallImage = Image.open("Assets/wall.png").convert("RGBA")
WallImage = WallImage.resize((42, 42), Image.Resampling.BILINEAR)
TkWallImage = ImageTk.PhotoImage(WallImage)

EmptyImage = Image.open("Assets/empty.png").convert("RGBA")
EmptyImage = EmptyImage.resize((42, 42), Image.Resampling.BILINEAR)
TkEmptyImage = ImageTk.PhotoImage(EmptyImage)

LavaImage = Image.open("Assets/lava.png").convert("RGBA")
LavaImage = LavaImage.resize((42, 42), Image.Resampling.BILINEAR)
TkLavaImage = ImageTk.PhotoImage(LavaImage)

PlayerImage = Image.open("Assets/player.png").convert("RGBA")
PlayerImage = PlayerImage.resize((42, 42), Image.Resampling.BILINEAR)
TkPlayerImage = ImageTk.PhotoImage(PlayerImage)

WinImage = Image.open("Assets/win.png").convert("RGBA")
WinImage = WinImage.resize((42, 42), Image.Resampling.BILINEAR)
TkWinImage = ImageTk.PhotoImage(WinImage)

TKimages = [TkWallImage, TkEmptyImage, TkLavaImage, TkPlayerImage, TkWinImage]

ErrorLabelVariable = StringVar()
ErrorLabel = Label(root, textvariable=ErrorLabelVariable, bg="white").pack()

ButtonFrame = Frame(root)
ButtonFrame.pack()

buttons = []
for col in range(10):
    for row in range(8):
        i = col * 8 + row + 1  # calculate button number
        button = Button(ButtonFrame, image=TkWallImage, highlightthickness=0, command=lambda t=str(i): get_button(t)) # button = Button(ButtonFrame, image=TkWallImage, highlightthickness=0, command=lambda b=button, t=str(i): get_button(b, t))
        button.grid(column=col, row=row, sticky=N)
        buttons.append(button)

ButtonFrame.place(relx=0.5, rely=0.525, anchor=CENTER)

root.config(menu=menubar)
root.mainloop()