import tkinter as tk
from time import sleep


def on_button_click():
    """Function to be called when the button is clicked."""
    label.config(text="Button was clicked!")
def exit_trial():
    #print(f'welcome and goodbye {namae} ')
    label.config(text="welcome", textvariable=namae)
    sleep(5)
    exit()

# Create the main application window
root = tk.Tk()
root.title("Simple GUI Example")
root.geometry("400x200") # Set window size

namae= tk.StringVar()

#data entry
label = tk.Label(root, text= "Enter Name" )
label.pack(pady=20) # Add padding for better spacing

entry_widget = tk.Entry(root, width=10, textvariable=namae,bg="white", fg="green")
entry_widget.pack(pady=5)
name=entry_widget.get()


# Create a label widget
label = tk.Label(root, text= "Karibu" )
label.pack(pady=20) # Add padding for better spacing

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
#if on_button_click() = true
    #print("welcome")
button.pack()

button1 = tk.Button(root, text="Exit", command=exit_trial, fg="blue", bg="white")
#if on_button_click() = true
    #print("welcome")
button1.pack()



# Start the Tkinter event loop
root.mainloop()
