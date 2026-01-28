import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Pexeso Alpha")
geometry_x, geometry_y = 600, 600
root.geometry(f"{geometry_x}x{geometry_y}")
frame = tk.Frame(root, bg="black")
frame.place(relheight=1, relwidth=1)

# Function will choose NxN cords and then create 2N cards
coordinates_2x2 = [(geometry_x/2-30, geometry_y/2-30), (geometry_x/2+30, geometry_y/2-30),
                   (geometry_x/2-30, geometry_y/2+30), (geometry_x/2+30, geometry_y/2+30)]
first_card = PhotoImage(file="imgs/1.png")
second_card = PhotoImage(file="imgs/2.png")

first_card_button = tk.Button(frame, image=first_card, bd=0, bg="red", activebackground="red").place(
    anchor="center", x=coordinates_2x2[0][0], y=coordinates_2x2[0][1])
first_card_copy_button = tk.Button(frame, image=first_card, bd=0, bg="red", activebackground="red").place(
    anchor="center", x=coordinates_2x2[3][0], y=coordinates_2x2[3][1])
second_card_button = tk.Button(frame, image=second_card, bd=0, bg="blue", activebackground="blue").place(
    anchor="center", x=coordinates_2x2[1][0], y=coordinates_2x2[1][1])
second_card_copy_button = tk.Button(frame, image=second_card, bd=0, bg="blue", activebackground="blue").place(
    anchor="center", x=coordinates_2x2[2][0], y=coordinates_2x2[2][1])

root.mainloop()
