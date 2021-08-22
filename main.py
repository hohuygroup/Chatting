# Nhập thư viện
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import sys
sys.path.append("Server/")
from Server import server
from tkinter import messagebox
import openpyxl


# Khai báo biến
so = 2
y1 = 98
vi_tri = 0
press = 0
x = 0
y = 120
listLabel = []
name_and_ip = {}

# Mở file lưu trữ bạn bè
wb = openpyxl.load_workbook("Temp/Friend.xlsx")
sheet = wb['Data']

# Tạo kết nối
server = server(str(sheet["B2"].value))

# Tạo cửa sổ và thiết lập
window = Tk()
window.title("Chatting")
window.geometry('1000x500')
window.iconbitmap("image\Icon.ico")
window.resizable(0, 0)

# Xử lí ảnh
image_1 = Image.open("image/Background.jpg")
image_background = ImageTk.PhotoImage(image_1)
image_2 = Image.open("image/Hide.png")
image_Hide = ImageTk.PhotoImage(image_2)
image_3 = Image.open("image/Nút.png")
image_Button = ImageTk.PhotoImage(image_3)

# Định nghĩa hàm
def avatars(envent):
    menu = Menu(window, tearoff=0)
    menu.add_command(label='Đăng xuất')
    menu.post(envent.x_root-20, envent.y_root)

def gettext_tk(envent):
    so = 2
    y1 = 100
    trung = []


    hide = Label(window, image=image_Hide, background="white")
    hide.place(x=0, y=100)
    while True:
        o = "A" + str(so)
        value = sheet[o].value
        if value == None:
            break
        if value == txt.get():
            trung.append(value)

        so += 1
    x = 0
    y1 = 98
    y2 = 120
    for xy in trung:       
        lbls = Label(window, text=xy, background="white", font=("Mundo Sans Std Medium", 14))
        lbls.place(x=10, y=y1)
        for xx in range(4):
            canvas = Label(window, text="━━━━", background="white")
            canvas.place(x=x, y=y2)
            x += 85

        y1 += 40
        x = 0
        y2 += 40

def delete_tk(envent):
    if txt.get() == "Tìm kiếm":
        txt.delete(0,'end')
def gettext_chat(envent):
    global server
    server.chat_client(str(txts.get()))
def delete_chat(envent):
    if txts.get() == "Nhập để chat":
        txts.delete(0,'end')
def get(envent):
    global press
    if press == 0:
        press += 1
    elif press == 1:
        a = combo.get()
        txts.insert(INSERT, a)
        press = 0
        print(a)
def on_closing():
    if messagebox.askokcancel("Quit", "Bạn có muốn tắt?"):
        try:
            server.close()
        except:
            pass
        window.destroy()
def chat(envent):
    global server
    from Server import server
    name = listLabel[envent].cget("text")
    server = server(name_and_ip[name])
def restart():
    global server
    from Server import server
    for x in name_and_ip:
        servers = server(name_and_ip[x])
    background.after(1, restart)


# Đặt background
background = Label(window, image=image_background, background="white")
background.place(x=0, y=0)
restart()

# Thanh tìm kiếm
txt = Entry(window,width=30, background="white")
txt.place(x=75, y=60)
txt.insert(INSERT,'Tìm kiếm')
txt.bind("<Return>", gettext_tk)
txt.bind("<Button-1>", delete_tk)

#Thanh chat
txts = Entry(window,width=80, background="white")
txts.place(x=400, y=470)
txts.insert(INSERT,'Nhập để chat')
txts.bind("<Return>", gettext_chat)
txts.bind("<Button-1>", delete_chat)

# Nút gửi tin nhắn
bt = Label(window, image=image_Button, background="white")
bt.place(x=955, y=459)
bt.bind("<Button-1>", gettext_chat)

# Chọn hình biểu cảm
combo = Combobox(window)
combo['values']= ("Hình biểu cảm", "😉", "♒", "♊", "✌", "☀", "☁", "☔", "⚡", "✨", "⭐", "✳", "⛄", "☕", "♨", "⛵", "⛽", "✈", "⛲", "⛺", "⛪", "☎", "✉", "✂", "🚽", "🛀", "👙", "💄", "👕", "👘", "👗", "👢", "👠", "👡", "💼", "👜", "👔", "🎩", "👒", "👑", "💍", "🚭", "⚽", "⚾", "⛳", "🏈", "🏀", "🎾", "🎱", "🎯", "🎿", "🎌", "🏁", "🏆")
combo.current(0)
combo.place(x=810, y=470)
combo.bind("<Button-1>", get)

# Tạo Label
lbl = Label(window, text="Tìm kiếm:", background="white")
lbl.place(x=10, y=60)
avatar = Label(window, text="Tài khoản", background="#5980df")
avatar.place(x=10, y=15)
avatar.bind("<Button-1>", avatars)

# Hiển thị bạn bè


while True:
    o = "A" + str(so)
    value = sheet[o].value
    if value == None:
        break
    else:
        values = sheet["B" + str(so)].value
    
    lbls = Label(window, text=value, background="white", font=("Mundo Sans Std Medium", 14))
    lbls.place(x=10, y=y1)
    lbls.bind("<Button-1>", lambda aa, jj=vi_tri: chat(jj))
    for xx in range(4):
        canvas = Label(window, text="━━━━━", background="white")
        canvas.place(x=x, y=y)
        x += 85
    listLabel.append(lbls)
    name_and_ip[value] = values

    so += 1
    y1 += 40
    x = 0
    y += 40
    vi_tri += 1

y = 55
# Vẽ
for xx in range(22):
    canvas = Label(window, text="│", background="white")
    canvas.place(x=300, y=y)
    y += 20

canvas = Label(window, text="━━━━━━━━━━━━━━━━━━━━━━━━━", background="white")
canvas.place(x=0, y=80)

# Xử lý sự kiện đóng cửa sổ
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()