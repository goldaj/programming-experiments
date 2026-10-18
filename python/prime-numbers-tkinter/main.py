import tkinter as tk

def next_prime(n):
  if n <= 1:
    return 2
  if n == 2:
    return 3
  prime = n
  found = False
  while not found:
    prime += 2
    if prime % 6 != 1 and prime % 6 != 5:
      continue
    for i in range(5, int(prime ** 0.5) + 1, 6):
      if prime % i == 0 or prime % (i + 2) == 0:
        break
    else:
      found = True
  return prime

def get_input():
  n = int(entry.get())
  result = next_prime(n)
  label["text"] = "The next prime number is: " + str(result)

# create the main window
window = tk.Tk()
window.title("Next Prime Number")

# create a label and text entry widget
label = tk.Label(text="Enter a number:")
entry = tk.Entry()

# create a button widget that will run the get_input function when clicked
button = tk.Button(text="Calculate", command=get_input)

# use the grid layout manager to place the label, entry, and button
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, column=0, columnspan=2)

# start the event loop
window.mainloop()
