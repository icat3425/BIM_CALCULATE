from tkinter import *  # yaptıgımızda tüm içeriğini kullanabiliriz
from tkinter import messagebox # import messagebox library
from tkinter import colorchooser # submodelcolor
window = Tk()
window.title("BIM CALCULATE")
window.minsize(width=300, height=200)
window.config(padx=0, pady=20)

# weight
my_weight = Label(text=" Enter Your Weight (kg)")
my_weight.config(padx=0, pady=5)
my_weight.pack()

# entry  weight
my_weight = Entry(width=10)
my_weight.pack()

# height
my_height = Label(text=" Enter Your Height (cm)")
my_height.config(padx=0, pady=10)
my_height.pack()

# entry height
my_height = Entry(width=10)
my_height.pack()


def calculateBim():
    try:
        weight = float(my_weight.get())
        height = float(my_height.get()) / 100

        if weight <= 0 or height <= 0:
            result_label.config(text="Hatalı deger girdiniz!")  # result_label
            messagebox.showinfo(title="This is info massagebox", message="You are a person")
            return
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your Status :{bmi:.2f}")


        # BIM degerlendirmesi
        if bmi < 18.5:
            status.config(text="Zayif")
        elif 18.5 <= bmi < 25:
            status.config(text="Normal")
        elif 25 <= bmi < 30:
            status.config(text="Kilolu")
        else:
            status.config(text="Obez")

    except ValueError:
        messagebox.showinfo(title="This is info massagebox", message="You are a person if you want to change back color")
        color = colorchooser.askcolor()
        colorHex = color[1]
        window.config(bg=colorHex)




def delete():
    my_weight.delete(0,END)
    my_height.delete(0,END)

# calculate
my_calculate = Button(text="Calculate", command=calculateBim)
my_calculate.config(padx=0, pady=10)
my_calculate.config(bg="#ff6200")
my_calculate.config(fg="#fffb1f")
my_calculate.config(activebackground="#FF0000")
my_calculate.config(activeforeground="#fffb1f")
my_calculate.pack()

delete = Button(window,text="delete",command=delete)
delete.config(bg="red")
delete.config(activebackground="cyan")
delete.pack(side = BOTTOM)


result_label = Label(text="")
result_label.pack()
status = Label(text="")
status.pack()

window.mainloop()