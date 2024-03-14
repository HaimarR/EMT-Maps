import tkinter as tk

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("EMT Maps Application")

        # Create and pack widgets
        self.label_city = tk.Label(self, text="Enter city name:")
        self.label_city.pack()

        self.entry_city = tk.Entry(self)
        self.entry_city.pack()

        self.search_button = tk.Button(self, text="Search")
        self.search_button.pack()

