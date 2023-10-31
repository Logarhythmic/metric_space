import tkinter
import customtkinter
from distancefunction import wdistance

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("700x700")
app.title("Word Metric")

# Adding UI Elements
inputbox = customtkinter.CTkLabel(app, text="Input two words.")
inputbox.pack(padx=10, pady=10)

# Function to refresh variables
def click():
    global outputbox
    output="The distance between " + word1_var.get() + " and " + word2_var.get() + " is " + str(wdistance(word1_var.get(),word2_var.get()))
    outputbox = customtkinter.CTkLabel(app,
                                     height=40,
                                     width=350,
                                     font=("default",24),
                                    text=output)
    calculate_button.configure(state="disabled")
    outputbox.pack()

# Function to clear history
def clear():
    outputbox.pack_forget()
    calculate_button.configure(state="normal")


#Data Input
word1_var=customtkinter.StringVar(value="Test")
word1 = customtkinter.CTkEntry(app,
                     height=40,
                     width=350,
                     font=("default",24),
                     textvariable=word1_var)
word1.pack(padx=10,pady=10)

word2_var=customtkinter.StringVar(value="Me")
word2 = customtkinter.CTkEntry(app,
                     height=40,
                     width=350,
                     font=("default",24),
                     textvariable=word2_var)
word2.pack(padx=10,pady=10)

# Calculate Button
calculate_button = customtkinter.CTkButton(app, text="Calculate Distance", font=("default",24), command=click)
calculate_button.pack()

# Clear History Button

clearbutton = customtkinter.CTkButton(app, text="Clear History", font=("default",24), command=clear)
clearbutton.pack(padx=10,pady=10)


# Run App
app.mainloop()