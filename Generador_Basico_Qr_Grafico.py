import qrcode
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("QR Code Generator")
window.geometry("400x300")


url_label = Label(window, text="Enter URL or Data:")
url_label.pack(pady=10)

url_entry = Entry(window)
url_entry.pack()

filename_label = Label(window, text="File Name:")
filename_label.pack(pady=10)

filename_entry = Entry(window)
filename_entry.pack()


def generate_qr_code():
    url = url_entry.get()
    filename = filename_entry.get()

    if not url or not filename:
        error_label = Label(window, text="Please enter URL and filename.", fg="red")
        error_label.pack()
        return

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    success_label = Label(window, text="QR Code generated successfully!", fg="green")
    success_label.pack()

generate_button = Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)


window.mainloop()
