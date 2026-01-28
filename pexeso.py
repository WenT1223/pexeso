import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Pexeso Alpha 2.0")
geometry_x, geometry_y = 600, 600
root.geometry(f"{geometry_x}x{geometry_y}")
frame = tk.Frame(root, bg="black")
frame.place(relheight=1, relwidth=1)
previous_card = None
current_card = None
card_is_activated = False

def activate_card(color_of_card, name_of_button):
    global previous_card, current_card, card_is_activated
    if card_is_activated == False:
        name_of_button.config(state="disabled", image=get_image_by_color(color_of_card), bg=color_of_card, activebackground=color_of_card)
        card_is_activated = True
        previous_card = [color_of_card, name_of_button]
    elif card_is_activated == True:
        name_of_button.config(state="disabled", image=get_image_by_color(color_of_card), bg=color_of_card, activebackground=color_of_card)
        current_card = [color_of_card, name_of_button]
        card_is_activated = False
        compare_cards(previous_card, current_card)


def compare_cards(previous_card, current_card):
    if previous_card[0] == current_card[0]:
        for i in range(1, 101):
            previous_card[1].place(y=previous_card[1].winfo_y() + i)
            current_card[1].place(y=current_card[1].winfo_y() + i)
            root.update()
            root.after(10)
        destroy_cards(previous_card[1], current_card[1])
    else:
        root.after(1000, lambda: flip_cards_back(previous_card[1], current_card[1]))


def destroy_cards(destroy_1, destroy_2):
    destroy_1.destroy()
    destroy_2.destroy()

def flip_cards_back(card_1, card_2):
    card_1.config(state="normal", image=cover_card, bg="green", activebackground="green")
    card_2.config(state="normal", image=cover_card, bg="green", activebackground="green")

def get_image_by_color(color_of_card):
    if color_of_card == "red":
        return red_card
    elif color_of_card == "blue":
        return blue_card
    else:
        return None


coordinates_2x2 = [(geometry_x/2-30, geometry_y/2-30), (geometry_x/2+30, geometry_y/2-30),
                   (geometry_x/2-30, geometry_y/2+30), (geometry_x/2+30, geometry_y/2+30)]
red_card = PhotoImage(file="imgs/red.png")
blue_card = PhotoImage(file="imgs/blue.png")
cover_card = PhotoImage(file="imgs/green.png")

red_card_button = tk.Button(frame, image=cover_card, bd=0, bg="green",
                              activebackground="green", command=lambda: activate_card("red", red_card_button))
red_card_copy_button = tk.Button(
    frame, image=cover_card, bd=0, bg="green", activebackground="green", command=lambda: activate_card("red", red_card_copy_button))
blue_card_button = tk.Button(
    frame, image=cover_card, bd=0, bg="green", activebackground="green", command=lambda: activate_card("blue", blue_card_button))
blue_card_copy_button = tk.Button(
    frame, image=cover_card, bd=0, bg="green", activebackground="green", command=lambda: activate_card("blue", blue_card_copy_button))

red_card_button.place(
    anchor="center", x=coordinates_2x2[0][0], y=coordinates_2x2[0][1])
red_card_copy_button.place(
    anchor="center", x=coordinates_2x2[3][0], y=coordinates_2x2[3][1])
blue_card_button.place(
    anchor="center", x=coordinates_2x2[1][0], y=coordinates_2x2[1][1])
blue_card_copy_button.place(
    anchor="center", x=coordinates_2x2[2][0], y=coordinates_2x2[2][1])

root.mainloop()
