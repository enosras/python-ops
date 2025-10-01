import tkinter as tki
from time import sleep
import dbm as db_conn


def on_button_click():
    """Function to be called when the button is clicked."""
    label.config(text="Button was clicked!")
def exit_trial():
    #print(f'welcome and goodbye {namae} ')

    #sleep(3)
    exit()
def clear_label():
    label.config(text=" ")
    entry_widget.delete(0, tki.END)
    selected_option.set(options [0])
def save_trial ():
    name_variable = entry_widget.get()

    if name_variable == "":
        label.config(text=f' Enter the name please')
    else:
        label.config(text=f' Bye {name_variable} , your money is coming')
        sleep(2)

# Create the main application window
root = tki.Tk()
root.title("Simple GUI Example")
root.configure(bg="#FFBF00")
root.geometry("400x380") # Set window size

#name_variable= tk.StringVar()

#data entry
label = tki.Label(root, text= "Enter Name", fg="white", bg="#FFBF00")
label.pack(pady=10) # Add padding for better spacing

entry_widget = tki.Entry(root, width=10,bg="white", fg="green")
entry_widget.pack(pady=10)

#data entry 2
label = tki.Label(root, text= "Enter gender", fg="white",bg="#FFBF00")
label.pack(pady=20) # Add padding for better spacing

options = ["Male", "Female", "Non-binary"]

selected_option = tki.StringVar(root)
selected_option.set(options[0])  # Set default value

dropdown = tki.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=10)


# Create a label widget
label = tki.Label(root, text= "Karibu", bg="#FFBF00")
label.pack(pady=20) # Add padding for better spacing

# Create a button widget
button = tki.Button(root, text="Click Me", command=on_button_click, fg='blue')
#if on_button_click() = true
    #print("welcome")
button.pack()

button2 = tki.Button(root, text="Clear", command=clear_label, fg="blue")
#if on_button_click() = true
    #print("welcome")
button2.pack()

button1 = tki.Button(root, text="Exit", command=exit_trial, fg="blue", bg="#FFBF00")
#if on_button_click() = true
    #print("welcome")
button1.pack()

button3 = tki.Button(root, text="Save", command=save_trial, fg="blue", bg="#FFBF00")
#if on_button_click() = true
    #print("welcome")
button3.pack()

# Start the Tkinter event loop
root.mainloop()
