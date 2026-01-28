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
        if card_color == "red":
            img = red_card
        elif card_color == "blue":
            img = blue_card
        else:
            img = cover_card
        button_name.config(state="disabled", image=img, bg=card_color, activebackground=card_color)
    elif card_color == card_color_compare:
        card_color_compare = ""
        for i in range(1, 51):
            last_button_name.place(y=last_button_name.winfo_y() + i)
            button_name.place(y=last_button_name.winfo_y() + i)
            root.update()
            root.after(10)
        last_button_name.destroy()
        button_name.destroy()
    else:
        card_color_compare = ""
        last_button_name.config(state="normal")
    last_button_name = button_name


# Function will choose NxN cords and then create 2N cards
coordinates_2x2 = [(geometry_x/2-30, geometry_y/2-30), (geometry_x/2+30, geometry_y/2-30),
                   (geometry_x/2-30, geometry_y/2+30), (geometry_x/2+30, geometry_y/2+30)]
red_card = PhotoImage(file="imgs/red.png")
blue_card = PhotoImage(file="imgs/blue.png")
cover_card = PhotoImage(file="imgs/green.png")

red_card_button = tk.Button(frame, image=cover_card, bd=0, bg="green",
                              activebackground="green", command=lambda: activate_card("red", red_card_button))
red_card_copy_button = tk.Button(
    frame, image=red_card, bd=0, bg="red", activebackground="red", command=lambda: activate_card("red", red_card_copy_button))
blue_card_button = tk.Button(
    frame, image=blue_card, bd=0, bg="blue", activebackground="blue", command=lambda: activate_card("blue", blue_card_button))
blue_card_copy_button = tk.Button(
    frame, image=blue_card, bd=0, bg="blue", activebackground="blue", command=lambda: activate_card("blue", blue_card_copy_button))

red_card_button.place(
    anchor="center", x=coordinates_2x2[0][0], y=coordinates_2x2[0][1])
red_card_copy_button.place(
    anchor="center", x=coordinates_2x2[3][0], y=coordinates_2x2[3][1])
blue_card_button.place(
    anchor="center", x=coordinates_2x2[1][0], y=coordinates_2x2[1][1])
blue_card_copy_button.place(
    anchor="center", x=coordinates_2x2[2][0], y=coordinates_2x2[2][1])

# for i in range(len(coordinates_2x2)):
#     cover_card_i = tk.Label(frame, image=cover_card, height=40, width=40)
#     cover_card_i.place(anchor="center", x=coordinates_2x2[i][0], y=coordinates_2x2[i][1])

root.mainloop()
