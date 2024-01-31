# Skyline Visualization Application

This Python project is an interactive application for visualizing and computing skyline points from a dataset. Utilizing the Tkinter GUI library and Matplotlib for plotting, the application allows users to load datasets, compute skyline points, and visualize them graphically.

## 🌟 Key Features

- 🗓️ Compute and visualize skyline points from a given dataset.
- 🖼️ Interactive GUI built with Tkinter for easy navigation and operation.
- 📊 Graphical representation of skyline points using Matplotlib.
- 📁 Supports loading data from text files for processing.

## 🔧 Technical Requirements

- 🐍 Python 3.x.
- 🎨 Tkinter library for the GUI interface.
- 📈 Matplotlib for plotting skyline visualizations.
- Additional dependencies listed in `requirements.txt`.

## 🚀 Installation and Setup

Make sure Python, Tkinter, and the required libraries are installed. To install dependencies:

```bash
pip install -r requirements.txt
```

## 🖱️ Usage
1. Clone or download the repository.
2. Navigate to the application directory.
3. Run the application:
   ```bash
   python app.py
   ```

## 📄 Code Overview
- `funcs.py`: Contains core functions for computing skyline points and plotting.
  - Functions like `is_skyline_candidate`, `update_skyline`, and others for skyline computation.
  - `plot_data_with_skyline` for visualizing the skyline and non-skyline points.

- `skyline.py`: Defines the `SkylineApp` class for the GUI application.
  - Methods for loading data, running skyline computations, and updating the plot.

- `app.py`: Entry point of the application.
  - Instantiates and runs the `SkylineApp`.

## 📋 Requirements
- All the necessary Python packages are listed in `requirements.txt`.

## 📁 Test Data
- Sample data for testing is provided in the `data.txt` file.
- The format includes pairs of coordinates, representing points in the dataset.

## 🖼️ Screenshots
- (Screenshots of the application in action would be included here)

## Contact 📧
Panagiotis Moschos - panagmosx@hotmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos
</p>
