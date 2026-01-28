import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Pexeso Alpha")
geometry_x, geometry_y = 600, 600
root.geometry(f"{geometry_x}x{geometry_y}")
frame = tk.Frame(root, bg="black")
frame.place(relheight=1, relwidth=1)
card_color_compare = ""


def activate_card(card_color, button_name):
    global card_color_compare, last_button_name
    if card_color_compare == "":
        card_color_compare = card_color
        button_name.config(state="disabled")
    elif card_color == card_color_compare:
        print("match")
        card_color_compare = ""
        last_button_name.config(state="normal")
    else:
        print("no match")
        card_color_compare = ""
        last_button_name.config(state="normal")
    last_button_name = button_name


# Function will choose NxN cords and then create 2N cards
coordinates_2x2 = [(geometry_x/2-30, geometry_y/2-30), (geometry_x/2+30, geometry_y/2-30),
                   (geometry_x/2-30, geometry_y/2+30), (geometry_x/2+30, geometry_y/2+30)]
first_card = PhotoImage(file="imgs/1.png")
second_card = PhotoImage(file="imgs/2.png")

first_card_button = tk.Button(frame, image=first_card, bd=0, bg="red",
                              activebackground="red", command=lambda: activate_card("red", first_card_button))
first_card_copy_button = tk.Button(
    frame, image=first_card, bd=0, bg="red", activebackground="red", command=lambda: activate_card("red", first_card_copy_button))
second_card_button = tk.Button(
    frame, image=second_card, bd=0, bg="blue", activebackground="blue", command=lambda: activate_card("blue", second_card_button))
second_card_copy_button = tk.Button(
    frame, image=second_card, bd=0, bg="blue", activebackground="blue", command=lambda: activate_card("blue", second_card_copy_button))

first_card_button.place(
    anchor="center", x=coordinates_2x2[0][0], y=coordinates_2x2[0][1])
first_card_copy_button.place(
    anchor="center", x=coordinates_2x2[3][0], y=coordinates_2x2[3][1])
second_card_button.place(
    anchor="center", x=coordinates_2x2[1][0], y=coordinates_2x2[1][1])
second_card_copy_button.place(
    anchor="center", x=coordinates_2x2[2][0], y=coordinates_2x2[2][1])

root.mainloop()
