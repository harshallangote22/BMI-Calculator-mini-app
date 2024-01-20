from tkinter import *
import customtkinter as ct
from PIL import Image
from tkinter import messagebox

# set the theme 
ct.set_appearance_mode('dark')
ct.set_default_color_theme("dark-blue")
# -----------------------------------------
root = ct.CTk()
root.title("BMI Calculator")
# root.iconbitmap("logo.ioc")
root.geometry("400x500")
root.resizable(False,False) 
# ---------------------------------------------
# Images Meter Code 
my_image = ct.CTkImage(light_image=Image.open("BMI_Calculator/images/bmi_img.png"),
                       size=(400,100))
my_lbl = ct.CTkLabel(root,text='',image=my_image)
my_lbl.pack(pady=10)
# --------------------------------------------------

# calculate btn code
def Calculate_Bmi():
    try:
        name = Name_entry.get()
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        # Convert height from feet to meters Code
        height_in_meters = height * 0.3048

        # Calculate BMI Code
        bmi = weight / (height_in_meters ** 2)

        if bmi>0:
             if(bmi<18.5):
                  category = 'Underweight'
             elif (bmi<=24.9):
                 category = 'Normal weight.'
             elif (bmi<=29.9):
                 category =  'you are Overweight.'
             elif (bmi<=34.9):
                 category =" you are obese. "
             elif (bmi<=39.9):
                 category = "you are severely obese. "
             else:
                 print( " you are morbidly obese. ")
        else:
             pass

        # Display result in the Tkinter window
        result.configure(text=f"Hello, {name}!\nYour BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for height and weight.")

#  Clear btn code 
def clear():
    Name_entry.delete(0, END)
    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    result.configure(text='')

# -----------------------------------------------------------
# Entry 
Name_entry = ct.CTkEntry(root,placeholder_text="Enter Your Nmae",
                width=300,height=30,border_width=1,
                corner_radius=20,)
Name_entry.pack(pady=10)

height_entry = ct.CTkEntry(root,placeholder_text="Height In Feet",
                width=300,height=30,border_width=1,
                corner_radius=20,)
height_entry.pack(pady=10)

weight_entry = ct.CTkEntry(root,placeholder_text="Weight In kg",
                width=300,height=30,border_width=1,
                corner_radius=20,)
weight_entry.pack(pady=10)
# --------------------------------------------------------------
# Button
Button_1 = ct.CTkButton(root,text="Calculate BMI",
                        width=200,height=30,command=Calculate_Bmi,corner_radius=20,
                        fg_color="#1f90bb",hover_color="#23a1d1")
Button_1.pack(pady=10)

Button_2 = ct.CTkButton(root,text="Clear Screen",
                        width=200,height=30,command=clear,corner_radius=20,
                        fg_color='#D35B58',hover_color='#C77C78')
Button_2.pack(pady=10)
# ----------------------------------------------------
# Result 
result = ct.CTkLabel(root,text="",font=('Consolas',20))
result.pack(pady=20)

# Run code / hold 
root.mainloop()