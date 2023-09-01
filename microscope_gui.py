#!/usr/bin/env python3

import tkinter as tk
import cv2
import serial
import pygame

# # Initialize PySerial for Arduino communication
arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Replace with the correct port

# # Initialize Pygame for keystrokes
# pygame.init()

# Initialize OpenCV for camera
# cap = cv2.VideoCapture(0)  # Use the appropriate camera index



# # Function to send commands to Arduino
def send_command(command):
    arduino.write(command.encode())

# # Function to capture an image
# def capture_image():
#     ret, frame = cap.read()
#     if ret:
#         cv2.imwrite('captured_image.jpg', frame)

# Create the GUI
root = tk.Tk()
root.title("OpenFlexure Microscope")

# # Motor control buttons
x1_button = tk.Button(root, text="X+", command=lambda: send_command("1"))
# x2_button = tk.Button(root, text="X-", command=lambda: send_command("x2"))
# y1_button = tk.Button(root, text="Y+", command=lambda: send_command("y1"))
# y2_button = tk.Button(root, text="Y-", command=lambda: send_command("y2"))
# z1_button = tk.Button(root, text="IN", command=lambda: send_command("z1"))
# z2_button = tk.Button(root, text="OUT", command=lambda: send_command("z2"))

x1_button.pack()
# x2_button.pack()
# y1_button.pack()
# y2_button.pack()
# z1_button.pack()
# z2_button.pack()
# motor1_button.pack()
# motor2_button.pack()
# motor3_button.pack()

# # Image capture button
# capture_button = tk.Button(root, text="Capture Image", command=capture_image)
# capture_button.pack()

# Create a label for displaying the camera feed
# camera_label = tk.Label(root)
# camera_label.pack()

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
