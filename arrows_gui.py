# GUI imports
# from cgitb import text
from email import message
import tkinter as tk
from tkinter import Tk, ttk
from tkinter import font
from PIL import Image, ImageTk

# encryptor / decryptor
import arrows

# Global GUI variables (for showing/hiding inputs)
OTP_selected = False
decrypt_selected = False
encrypt_selected = False
message_out = ""
key_out = ""


def main():
    def toggle_key_input():
        global OTP_selected
        if OTP_selected:
            key_text.grid()
            key_input.grid()
        else:
            key_text.grid_remove()
            key_input.grid_remove()
        OTP_selected = not OTP_selected

    def toggle_OTP_on_decrypt():
        global decrypt_selected
        global encrypt_selected
        global OTP_selected
        if decrypt_selected:
            if OTP_selected:    # incase OTP was selected before selecting decrypt
                key_text.grid_remove()
                key_input.grid_remove()
            otp_text.grid()
            otp_checkbox.grid()
        else:
            encrypt_selected = False

            otp_checkbox.deselect()
            OTP_selected = False

            otp_text.grid_remove()
            otp_checkbox.grid_remove()
            key_text.grid()
            key_input.grid()    # show key input incase otp was selected before selecting decrypt
        decrypt_selected = not decrypt_selected

    def toggle_OTP_on_encrypt():
        global encrypt_selected
        global decrypt_selected
        if decrypt_selected:
            otp_text.grid()
            otp_checkbox.grid()
        decrypt_selected = False
        encrypt_selected = not encrypt_selected

    def enter_onclick():
        global message_out
        global key_out

        result = ()
        key = key_input.get("1.0", tk.END).replace("\n", "")
        message = message_input.get("1.0", tk.END).replace("\n", "")
        message_output.config(text="")
        key_output.config(text="")

        if e_d_selection.get() == 0:
            user_return_message.config(text="Select Encrypt or Decrypt")
        elif not OTP_selected and key == "":
            user_return_message.config(
                text="Enter a key or select \'Generate OTP key\'")
        elif message == "":
            user_return_message.config(
                text="Enter a message to encrypt or decrypt")
        else:
            user_return_message.config(text="")
            if e_d_selection.get() == 1:
                if OTP_selected:
                    result = arrows.encryptor(
                        encrypt_decrypt=1, use_OTP=True, text=message)
                else:
                    result = arrows.encryptor(
                        encrypt_decrypt=1, use_OTP=False, key=key, text=message)
            elif e_d_selection.get() == 2:
                result = arrows.encryptor(
                    encrypt_decrypt=2, key=key, text=message)

            message_out = result[0]
            key_out = result[1]

            message_output.config(text=result[0])
            key_output.config(text=result[1])

    def copy_message():
        global message_out
        root.clipboard_clear()
        root.clipboard_append(message_out)
        root.update()  # text stays after the window is closed

    def copy_key():
        global key_out
        root.clipboard_clear()
        root.clipboard_append(key_out)
        root.update()

    root = tk.Tk()
    # root.configure(background="#C3C3C3")
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.grid(rowspan=30, columnspan=3)

    # logo
    logo = Image.open("img/arrows_logo.jpg")
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(row=0, column=0)

    encrypt_decrypt_text = tk.Label(
        root, text="Encrypt or Decrypt:", font="Raleway")
    encrypt_decrypt_text.grid(row=1, column=0)

    e_d_selection = tk.IntVar()
    e = tk.Checkbutton(root, text="Encrypt", variable=e_d_selection,
                       onvalue=1, command=toggle_OTP_on_encrypt)
    e.grid(row=1, column=1)
    d = tk.Checkbutton(root, text="Decrypt", variable=e_d_selection,
                       onvalue=2, command=toggle_OTP_on_decrypt)
    d.grid(row=1, column=2)

    OTP_selection = tk.IntVar()
    otp_text = tk.Label(root, text="Generate OTP key?", font="Raleway")
    otp_text.grid(row=3, column=0)

    otp_checkbox = tk.Checkbutton(
        root, text='OTP Key', variable=OTP_selection, onvalue=1, command=toggle_key_input)
    otp_checkbox.grid(row=3, column=1)

    key_text = tk.Label(root, text="Enter key:", font="Raleway")
    key_text.grid(row=4, column=0)

    key_input = tk.Text(root, height=3, width=30)
    key_input.grid(row=4, column=1)

    message_text = tk.Label(root, text="Enter message:", font="Raleway")
    message_text.grid(row=5, column=0)

    message_input = tk.Text(root, height=5, width=30)
    message_input.grid(row=5, column=1)

    enter = tk.Button(root, height=2, width=10,
                      text="Enter", command=enter_onclick)
    enter.grid(row=6, column=1)

    user_return_message = tk.Label(root, text="", fg="#ee3377")
    user_return_message.grid(row=7, column=1)

    message_output_text = tk.Label(
        root, text="Message output:", font="Raleway")
    message_output_text.grid(row=8, column=0)

    message_output = tk.Label(root, text="", fg="#ee3377", wraplength=250)
    message_output.grid(row=8, column=1)

    key_output_text = tk.Label(root, text="Key output:", font="Raleway")
    key_output_text.grid(row=9, column=0)

    key_output = tk.Label(root, text="", fg="#ee3377", wraplength=250)
    key_output.grid(row=9, column=1)

    cpy_msg_btn = tk.Button(root, height=1, width=5,
                            text="Copy", command=copy_message)
    cpy_msg_btn.grid(row=8, column=2)

    cpy_key_btn = tk.Button(root, height=1, width=5,
                            text="Copy", command=copy_key)
    cpy_key_btn.grid(row=9, column=2)

    root.columnconfigure(0, minsize=40)
    root.rowconfigure(0, pad=30)
    # root.grid_rowconfigure(2, pad=10)
    # root.grid_rowconfigure(3, pad=10)

    root.mainloop()


if __name__ == "__main__":
    main()
