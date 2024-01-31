import os
import ast
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def is_skyline_candidate(current_point, skyline_points):
    """Ελέγχει αν ένα σημείο είναι υποψήφιο για την λίστα skyline."""
    for point in skyline_points:
        if all(x <= y for x, y in zip(point, current_point)):
            return False
    return True

def update_skyline(skyline_points, new_point):
    """Ενημερώνει την λίστα skyline με ένα νέο σημείο."""
    skyline_points[:] = [point for point in skyline_points if not all(x >= y for x, y in zip(point, new_point))]
    skyline_points.append(new_point)

def is_dominated_by_window(point, window):
    """Ελέγχει αν ένα σημείο κυριαρχείται από κάποιο σημείο στο window."""
    return any(all(x <= y for x, y in zip(point, window_point)) for window_point in window)

def update_window(window, new_point):
    """Ενημερώνει το window με ένα νέο σημείο, αφαιρώντας τα σημεία που κυριαρχούνται."""
    window[:] = [point for point in window if not all(x >= y for x, y in zip(point, new_point))]
    if not is_dominated_by_window(new_point, window):
        window.append(new_point)   

def process_window(window, data_file):
    """Διαχειρίζεται τα σημεία του window και αποθηκεύει τα επιπλέον σημεία στο αρχείο data_file."""
    with open(data_file, 'a') as file:
        for point in window:
            file.write(f"{point}\n")
    window.clear()


def read_data_from_file(data_file):
    """Διαβάζει σημεία από ένα αρχείο και τα επιστρέφει ως λίστα."""
    data = []
    with open(data_file, 'r') as file:
        for line in file:
            data.append(ast.literal_eval(line.strip()))
    return data

def compute_skyline(data, window_size=3, temp_file='w.txt'):
    """Υπολογίζει τα σημεία skyline από ένα σύνολο δεδομένων."""
    skyline_points = []
    window = []

    for point in data:
        print("Εξετάζοντας το σημείο:", point)
        if is_skyline_candidate(point, skyline_points):
            update_skyline(skyline_points, point)
            update_window(window, point)
            if len(window) >= window_size:
                process_window(window, temp_file)

    # Διαχείριση των πλειάδων από το προσωρινό αρχείο
    if os.path.exists(temp_file):
        extra_data = read_data_from_file(temp_file)
        for point in extra_data:
            if is_skyline_candidate(point, skyline_points):
                update_skyline(skyline_points, point)

        os.remove(temp_file)  # Διαγραφή του προσωρινού αρχείου

    return skyline_points

def plot_data_with_skyline(data, skyline_points):
    # Δημιουργία λιστών για τις συντεταγμένες X και Y
    x_all, y_all = zip(*data)
    x_skyline, y_skyline = zip(*skyline_points)

    plt.figure(figsize=(10, 6))

    # Εμφάνιση όλων των σημείων
    plt.scatter(x_all, y_all, color='black', label='Όλα τα non-Skyline points')

    # Εμφάνιση των σημείων του skyline
    plt.scatter(x_skyline, y_skyline, color='red', label='Skyline points')

    # Προσθήκη οριζόντιων και κάθετων γραμμών
    for x, y in skyline_points:
        plt.axhline(y=y, color='blue', linestyle='dashed', linewidth=0.5)
        plt.axvline(x=x, color='blue', linestyle='dashed', linewidth=0.5)


    plt.title('Skyline Visualization')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.legend()
    plt.show()
