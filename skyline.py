from funcs import *

import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Ορίζουμε την κλάση SkylineApp που είναι υποκλάση της tk.Tk
class SkylineApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Εφαρμογή Οπτικοποίησης Skyline")
        self.geometry("800x600")
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close_window)
    
    def create_widgets(self):
        # Δημιουργούμε το κουμπί φόρτωσης αρχείου
        self.load_button = tk.Button(self, text="Φόρτωση Αρχείου Δεδομένων", command=self.load_file)
        self.load_button.pack()
        self.plot_canvas = None
    
    def close_window(self):
        self.destroy()  # Close the window
        self.quit()    # Terminate the program
    
    def load_file(self):
        # Επιλογή αρχείου δεδομένων
        file_path = filedialog.askopenfilename(filetypes=[("Αρχεία Κειμένου", "*.txt")])
        if file_path:
            data = read_data_from_file(file_path)
            skyline_points = compute_skyline(data)
            self.plot_data_with_skyline(data, skyline_points)

    def plot_data_with_skyline(self, data, skyline_points):
        # Δημιουργία γραφικής παράστασης
        fig, ax = plt.subplots(figsize=(10, 6))

        x_all, y_all = zip(*data)
        x_skyline, y_skyline = zip(*skyline_points)

        # Σημεία που δεν ανήκουν στο Skyline
        ax.scatter(x_all, y_all, color='black', label='Όλα τα μη-Σημεία Skyline')
        
        # Σημεία του Skyline
        ax.scatter(x_skyline, y_skyline, color='red', label='Σημεία Skyline')

        for x, y in skyline_points:
            # Διακεκομμένες γραμμές που δείχνουν το Skyline
            ax.axhline(y=y, color='blue', linestyle='dashed', linewidth=0.5)
            ax.axvline(x=x, color='blue', linestyle='dashed', linewidth=0.5)

        ax.set_title('Οπτικοποίηση Skyline')
        ax.set_xlabel('Άξονας X')
        ax.set_ylabel('Άξονας Y')
        ax.legend()

        if self.plot_canvas:
            self.plot_canvas.get_tk_widget().pack_forget()
        self.plot_canvas = FigureCanvasTkAgg(fig, master=self)
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

