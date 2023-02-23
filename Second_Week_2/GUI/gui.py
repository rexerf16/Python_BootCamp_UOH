# *5
from tkinter import*

window = Tk()  # creating a window
window.geometry("420x420")  # window size
window.title("GUI")  # giving our GUI window a title
lable = Label(window,
              text="Hello World", font=(
                  'Arial', 40, 'bold'), fg='green', bg='black')  # custmizing lable
lable.pack()  # displaying lable on window
window.mainloop()  # making the window loop until closing
