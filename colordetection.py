# Import necessary libraries
import cv2
import numpy as np
from sklearn.cluster import KMeans
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk

# Create a modern-themed window
window = ThemedTk(theme="radiance")  
window.title("Image Color Detector")

# Function to open and process an image
def open_image():
    image_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpg")])
    if image_path:
        process_image(image_path)

# Function to process and display image color information
def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load the image.")
        return
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    reshaped_image = image_rgb.reshape(-1, 3)

    num_colors = 5
    kmeans = KMeans(n_clusters=num_colors, n_init=20)
    kmeans.fit(reshaped_image)
    dominant_colors = kmeans.cluster_centers_.astype(int)

    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Dominant Color Information:")
    for color in dominant_colors:
        print(f"RGB: {color[0]}, {color[1]}, {color[2]}")

# Create and style the Open Image button
style = ttk.Style()
style.configure("TButton", padding=10, font=("Arial", 12))

open_button = ttk.Button(window, text="Select an Image", command=open_image)
open_button.pack(padx=20, pady=10)

# Start the Tkinter main loop
window.mainloop()
