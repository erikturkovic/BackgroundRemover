from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import secrets

def select_image():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if file_path:
        label_image.config(text="Selected Image: " + file_path)
        root.file_path = file_path

def select_output_directory():
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if output_dir:
        label_output.config(text="Output Directory: " + output_dir)
        root.output_dir = output_dir

def generate_random_string(length):
    return secrets.token_hex(length // 2)[:length]

def process_image():
    if hasattr(root, 'file_path') and hasattr(root, 'output_dir'):
        random_string = generate_random_string(8)
        input_image = root.file_path
        output_image = f"{root.output_dir}/{random_string}.png"
        input = Image.open(input_image)
        output = remove(input)
        output.save(output_image)
        label_status.config(text=f"Image saved to: {output_image}")
    else:
        label_status.config(text="Please select both an image and an output directory.")

root = tk.Tk()
root.title("BGremover")
root.geometry("400x200")

label_image = tk.Label(root, text="Selected Image:")
label_image.pack(pady=5)

select_image_button = tk.Button(root, text="Select Image", command=select_image)
select_image_button.pack(pady=5)

label_output = tk.Label(root, text="Output Directory:")
label_output.pack(pady=5)

select_output_button = tk.Button(root, text="Select Output Directory", command=select_output_directory)
select_output_button.pack(pady=5)

process_button = tk.Button(root, text="Process Image", command=process_image)
process_button.pack(pady=5)

label_status = tk.Label(root, text="")
label_status.pack(pady=10)

root.mainloop()

#test