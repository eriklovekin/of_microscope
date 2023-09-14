#!/usr/bin/env python3

import tkinter as tk
import cv2
import serial
import pygame
from PIL import Image, ImageTk
import time

# # Initialize PySerial for Arduino communication
arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Replace with the correct port

# # Initialize Pygame for keystrokes
# pygame.init()

# Initialize OpenCV for camera
cap = cv2.VideoCapture(0)  # Use the appropriate camera index
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


cap_span_row = int(10)
cap_span_col = int(10)
# # Function to send commands to Arduino
def send_command(command):
    arduino.write(command.encode())
    print(command)

# # Function to capture an image
def capture_image():
    ret, frame = cap.read()
    now = time.strftime("%Y%m%d%H%M%S")
    im_name = "ofcapture" + now
    im_path = "./media/"
    im_type = ".jpg"
    print(now)
    print(im_name)
    if ret:
        cv2.imwrite(im_path+im_name+im_type, frame)

# Create the GUI
root = tk.Tk()
root.title("OpenFlexure Microscope")
root.geometry("800x500")
control_panel = tk.Frame(root,width=100)
control_panel.grid(row=0,column=1,sticky='NESW')

# # Motor control buttons
x_pos_btn = tk.Button(control_panel, text="X+", command=lambda: send_command("x_pos_btn"),bg="RED",fg="WHITE")
x_neg_btn = tk.Button(control_panel, text="X-", command=lambda: send_command("x_neg_btn"),bg="RED",fg="WHITE")
y_pos_btn = tk.Button(control_panel, text="Y+", command=lambda: send_command("y_pos_btn"),bg="GREEN",fg="WHITE")
y_neg_btn = tk.Button(control_panel, text="Y-", command=lambda: send_command("y_neg_btn"),bg="GREEN",fg="WHITE")
z_out_btn = tk.Button(control_panel, text="OUT", command=lambda: send_command("z_out_btn"),bg="BLUE",fg="WHITE")
z_in_btn = tk.Button(control_panel, text="IN", command=lambda: send_command("z_in_btn"),bg="BLUE",fg="WHITE")

# # Camera Buttons
snap_btn = tk.Button(control_panel, text="Capture Image", command=capture_image)

# # Button Positioning
x_pos_btn.grid(row=3,column=5+cap_span_col,columnspan=2,sticky='EW')
x_neg_btn.grid(row=3,column=1+cap_span_col,columnspan=2,sticky='EW')
y_pos_btn.grid(row=2,column=3+cap_span_col,columnspan=2,sticky='EW')
y_neg_btn.grid(row=4,column=3+cap_span_col,columnspan=2,sticky='EW')
z_out_btn.grid(row=1,column=4+cap_span_col,columnspan=3,sticky='EW')
z_in_btn.grid(row=1,column=1+cap_span_col,columnspan=3,sticky='EW')
snap_btn.grid(row=5,column=1+cap_span_col,columnspan=6,sticky='EW')

# Create a label for displaying the camera feed
camera_label = tk.Label(root)
camera_label.grid(row=0,column=0,sticky='NESW')
# camera_label.pack(expand=True, fill="both")

# camera_label.grid(row=1,column=1,rowspan=cap_span_row,columnspan=cap_span_col,sticky='NESW')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Main loop to update the camera feed
# def update_camera():
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = cv2.resize(frame, (640, 480))
#         img = tk.PhotoImage(data=img.tostring())
#         camera_label.config(image=img)
#         camera_label.img = img
#         root.after(10, update_camera)  # Update every 10ms

# update_camera()

# def update_camera():
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = cv2.resize(frame, (640, 480))

#         # Convert the image to PhotoImage format using PIL (Python Imaging Library)
#         img = Image.fromarray(img)
#         img = ImageTk.PhotoImage(image=img)

#         camera_label.config(image=img)
#         camera_label.image = img  # Keep a reference to avoid garbage collection

#     root.after(10, update_camera)  # Update every 10ms

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

def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    camera_label.imgtk = imgtk
    camera_label.configure(image=imgtk)
    camera_label.after(1, video_stream) 


video_stream()
root.mainloop()