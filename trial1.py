import tkinter as tki
from time import sleep


def on_button_click():
    """Function to be called when the button is clicked."""
    label.config(text="Button was clicked!")
def exit_trial():
    #print(f'welcome and goodbye {namae} ')
    name_variable=entry_widget.get()
    label.config(text=f' Bye {name_variable} , your money is coming')
    #sleep(3)
    exit()
def clear_label():
    label.config(text=" ")
    entry_widget.delete(0, tki.END)

# Create the main application window
root = tki.Tk()
root.title("Simple GUI Example")
root.geometry("400x250") # Set window size

#name_variable= tk.StringVar()

#data entry
label = tki.Label(root, text= "Enter Name" )
label.pack(pady=20) # Add padding for better spacing

entry_widget = tki.Entry(root, width=10,bg="white", fg="green")
entry_widget.pack(pady=5)



# Create a label widget
label = tki.Label(root, text= "Karibu" )
label.pack(pady=20) # Add padding for better spacing

# Create a button widget
button = tki.Button(root, text="Click Me", command=on_button_click)
#if on_button_click() = true
    #print("welcome")
button.pack()

button2 = tki.Button(root, text="Clear", command=clear_label)
#if on_button_click() = true
    #print("welcome")
button2.pack()

button1 = tki.Button(root, text="Exit", command=exit_trial, fg="blue", bg="white")
#if on_button_click() = true
    #print("welcome")
button1.pack()



# Start the Tkinter event loop
root.mainloop()
