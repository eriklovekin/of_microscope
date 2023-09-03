#!/usr/bin/env python3

import tkinter as tk
import cv2
import serial
import pygame

# # Initialize PySerial for Arduino communication
arduino = serial.Serial('/dev/ttyUSB1', 9600)  # Replace with the correct port

# # Initialize Pygame for keystrokes
# pygame.init()

# Initialize OpenCV for camera
cap = cv2.VideoCapture(0)  # Use the appropriate camera index


img_span_row = int(10)
img_span_col = int(10)
# # Function to send commands to Arduino
def send_command(command):
    arduino.write(command.encode())
    print(command)

# # Function to capture an image
def capture_image():
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('captured_image.jpg', frame)

# Create the GUI
root = tk.Tk()
root.title("OpenFlexure Microscope")
root.geometry("450x350")

# # Motor control buttons
x_pos_btn = tk.Button(root, text="X+", command=lambda: send_command("x_pos_btn"),bg="RED",fg="WHITE")
x_neg_btn = tk.Button(root, text="X-", command=lambda: send_command("x_neg_btn"),bg="RED",fg="WHITE")
y_pos_btn = tk.Button(root, text="Y+", command=lambda: send_command("y_pos_btn"),bg="GREEN",fg="WHITE")
y_neg_btn = tk.Button(root, text="Y-", command=lambda: send_command("y_neg_btn"),bg="GREEN",fg="WHITE")
z_out_btn = tk.Button(root, text="OUT", command=lambda: send_command("z_out_btn"),bg="BLUE",fg="WHITE")
z_in_btn = tk.Button(root, text="IN", command=lambda: send_command("z_in_btn"),bg="BLUE",fg="WHITE")

# # Camera Buttons
snap_btn = tk.Button(root, text="Capture Image", command=capture_image)

# # Button Positioning
x_pos_btn.grid(row=3,column=5+img_span_col,columnspan=2,sticky='EW')
x_neg_btn.grid(row=3,column=1+img_span_col,columnspan=2,sticky='EW')
y_pos_btn.grid(row=2,column=3+img_span_col,columnspan=2,sticky='EW')
y_neg_btn.grid(row=4,column=3+img_span_col,columnspan=2,sticky='EW')
z_out_btn.grid(row=1,column=4+img_span_col,columnspan=3,sticky='EW')
z_in_btn.grid(row=1,column=1+img_span_col,columnspan=3,sticky='EW')
snap_btn.grid(row=5,column=1+img_span_col,columnspan=6,sticky='EW')

# Create a label for displaying the camera feed
camera_label = tk.Label(root)
camera_label.grid(row=1,column=1,rowspan=img_span_row,columnspan=img_span_col,sticky='NESW')

# Main loop to update the camera feed
def update_camera():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(frame, (640, 480))
        img = tk.PhotoImage(data=img.tostring())
        camera_label.config(image=img)
        camera_label.img = img
        root.after(10, update_camera)  # Update every 10ms

# update_camera()

# Keystroke handling
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_a:
#                 send_command("A")
#             elif event.key == pygame.K_b:
#                 send_command("B")
#             # Add more key mappings as needed

# Start the GUI main loop
root.mainloop()
