from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy as np

root = Tk()
root.geometry("300x250")

def process_image(encrypt=True):
    # Ask user to select an image file
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg')])
    if file_path:
        key = int(entry1.get())  # Get the encryption/decryption key
        img = Image.open(file_path)
        img_array = np.array(img)  # Convert image to a NumPy array

        if encrypt:
            # Perform encryption by adding key
            processed_array = (img_array + key) % 256
            processed_img = Image.fromarray(processed_array.astype('uint8'))
            processed_img.save(file_path)  # Overwrite the file with the encrypted image
            print("Image encryption complete!")
        else:
            # Perform decryption by subtracting key
            processed_array = (img_array - key) % 256
            processed_img = Image.fromarray(processed_array.astype('uint8'))
            processed_img.save(file_path)  # Overwrite the file with the decrypted image
            print("Image decryption complete!")

def encrypt_image():
    process_image(encrypt=True)

def decrypt_image():
    process_image(encrypt=False)

# Create a frame to hold buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

# Create Encrypt and Decrypt buttons
b1 = Button(button_frame, text="Encrypt Image", command=encrypt_image)
b1.pack(side=LEFT, padx=10)

b2 = Button(button_frame, text="Decrypt Image", command=decrypt_image)
b2.pack(side=LEFT, padx=10)

# Create an entry field for the key
entry1 = Entry(root)
entry1.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
