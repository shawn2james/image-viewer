#! /media/shawn/new-volume/anaconda3/bin/python 
import os
import tkinter as tk
from PIL import ImageTk,Image
import tkinter.font
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', required=False, help= 'the images of which directory is to be displayed.')
args = parser.parse_args()


os.chdir(args.p) # to change directory to argument passed for '--path'

# ROOT SETTINGS
root = tk.Tk()
root.title("Image Viewer")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("{}x{}".format(width,height))
root.resizable(0,0)
# FRAME SETTINGS
frame = tk.Frame(root, width=width, height=height, bg="coral")
frame.grid(row=0, column=0, columnspan=3, rowspan=3)

# OPENING WINDOW
title_font = tkinter.font.Font(family="system", size=60)
title = tk.Label(root, text="IMAGE VIEWER", font=title_font, bg="coral", fg="lightblue")
title.grid(column=0, row=0, columnspan=3)

loading_font = tkinter.font.Font(family="system", size=30)
loading = tk.Label(root, text="Loading . . . .", font=loading_font, bg='gray')
loading.grid(column=0, row=1, columnspan=3, ipadx=30, ipady=20)

# ACCESSING IMAGES
current_img_num = 0
image_list = []
for file in os.listdir():
    if file.lower().endswith(('.jpg','.png','.ico')):
        image_list.append(file)


# IMAGE LABEL
img_name = tk.Label(frame, text=image_list[0], fg="black")
first_image = Image.open(image_list[0])
aspect_ratio = first_image.width / first_image.height
new_height=500
new_width = int(new_height*aspect_ratio)
first_img = ImageTk.PhotoImage(first_image.resize((new_width,new_height)))
img_place = tk.Label(image=first_img)

# BUTTONS
btn_previous = tk.Button(frame, text="<<< Previous", height=2, width=16, state="disabled")
btn_rotate = tk.Button(frame, text="Quit", height=2, width=15, command=root.quit)
btn_next = tk.Button(frame, text="Next >>>", height=2, width=16, command=lambda:next(1))

#---------------------------------------------------------------------------------------

# BUTTON FUNCTIONS
def previous(image_num):
    global img_place
    global btn_previous
    global btn_next
    global current_img_num
    global img_name

    current_img_num = image_num + 1
    img_place.configure(image="")
    next_image = Image.open(image_list[image_num])
    aspect_ratio = next_image.width / next_image.height
    new_height=500
    new_width = int(new_height*aspect_ratio)

    next_img = ImageTk.PhotoImage(next_image.resize((new_width,new_height), Image.ANTIALIAS))
    img_place.image = next_img
    img_place.config(image = next_img)

    img_name.destroy()
    next_img_name = tk.Label(frame, text=image_list[image_num], fg="black")
    next_img_name.place(anchor="center", x=670, y=10)

    btn_previous.destroy()
    btn_previous = tk.Button(frame, text="<<< Previous", height=2, width=16, command=lambda:previous(image_num-1))
    btn_previous.place(anchor="center",x=500, y=620)

    btn_next.destroy()
    btn_next = tk.Button(frame, text="Next >>>", height=2, width=16, command=lambda:next(image_num))
    btn_next.place(anchor="center",x=840, y=620)

    if (image_num == 0):
        btn_previous.configure(state="disabled")



def next(image_num):
    global img_place
    global btn_next
    global btn_previous
    global current_img_num

    current_img_num = image_num - 1
    img_place.configure(image="")
    next_image = Image.open(image_list[image_num])
    aspect_ratio = next_image.width / next_image.height
    new_height=500
    new_width = int(new_height*aspect_ratio)

    next_img = ImageTk.PhotoImage(next_image.resize((new_width,new_height), Image.ANTIALIAS))
    img_place.image = next_img
    img_place.config(image = next_img)

    next_img_name = tk.Label(frame, text=image_list[image_num], fg="black")
    next_img_name.place(anchor="center", x=670, y=10)

    btn_next.destroy()
    btn_next = tk.Button(frame, text="Next >>>", height=2, width=16, command=lambda:next(image_num+1))
    btn_next.place(anchor="center",x=840, y=620)

    btn_previous.destroy()
    btn_previous = tk.Button(frame, text="<<< Previous", height=2, width=16, command=lambda:previous(image_num-1))
    btn_previous.place(anchor="center",x=500, y=620)

    if (image_num==len(image_list)-1):
        btn_next.configure(state="disabled")


#----------------------------------------------------------------------------

# IMAGE VIEWER FUNCTION
def image_viewer () :
    title.destroy()

    img_name.place(anchor="center", x=670, y=10)
    img_place.place(anchor="center", x=675, y=300)
    btn_previous.place(anchor="center",x=500, y=620)
    btn_rotate.place(anchor="center",x=670, y=620)
    btn_next.place(anchor="center",x=840, y=620)
#----------------------------------------------------------------------------


root.after(2000, image_viewer)

root.mainloop()
