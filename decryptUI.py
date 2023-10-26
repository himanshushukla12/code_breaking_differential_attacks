import tkinter as tk
from tkinter import ttk
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, DES
import base64

def rsa_decrypt(cipher_text, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(base64.b64decode(cipher_text))
    return decrypted_message.decode('utf-8')

def des_decrypt(cipher_text, key):
    des_cipher = DES.new(key.encode(), DES.MODE_ECB)
    decrypted_message = des_cipher.decrypt(base64.b64decode(cipher_text))
    return decrypted_message.decode('utf-8').rstrip('\0')

def vigenere_decrypt(cipher_text, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    cipher_text_int = [ord(i) for i in cipher_text]
    plain_text = ''
    
    for i in range(len(cipher_text_int)):
        value = (cipher_text_int[i] - key_as_int[i % key_length]) % 26
        plain_text += chr(value + 65)
    
    return plain_text

def decrypt_text():
    cipher_text = cipher_text_box.get("1.0", tk.END).strip()
    key_text = key_text_box.get("1.0", tk.END).strip()
    algorithm = algorithm_selection.get()
    
    if algorithm == "RSA":
        decrypted_text = rsa_decrypt(cipher_text, key_text)
    elif algorithm == "DES":
        decrypted_text = des_decrypt(cipher_text, key_text)
    elif algorithm == "Vigenère":
        decrypted_text = vigenere_decrypt(cipher_text, key_text)
    
    plain_text_box.delete("1.0", tk.END)
    plain_text_box.insert(tk.END, decrypted_text)

root = tk.Tk()
root.title("Decryption App")

cipher_label = tk.Label(root, text="Cipher:")
cipher_label.pack(padx=10, pady=10, anchor=tk.W)
cipher_text_box = tk.Text(root, wrap=tk.WORD, height=10, width=50)
cipher_text_box.pack(padx=10, pady=10)

key_label = tk.Label(root, text="Key:")
key_label.pack(padx=10, pady=10, anchor=tk.W)
key_text_box = tk.Text(root, wrap=tk.WORD, height=2, width=50)
key_text_box.pack(padx=10, pady=10)

algorithm_selection = tk.StringVar()
algorithm_selection.set("Select Algorithm")
algorithm_dropdown = ttk.Combobox(root, textvariable=algorithm_selection, values=("RSA", "DES", "Vigenère"))
algorithm_dropdown.pack(padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack(padx=10, pady=10)

plain_text_label = tk.Label(root, text="Plain Text:")
plain_text_label.pack(padx=10, pady=10, anchor=tk.W)
plain_text_box = tk.Text(root, wrap=tk.WORD, height=10, width=50)
plain_text_box.pack(padx=10, pady=10)

root.mainloop()
