import clipboard
import tkinter as tk
from tkinter import ttk, Text
import frequencyCharGraph
import RSAattack
import vigenereHacker
import subprocess
import pyperclip
#import DESMIM2
def open_text_files():
    with open('plaintext.txt', 'r') as file1, open('ciphertext.txt', 'r') as file2:
        lines1 = file1.readlines()[:10]
        lines2 = file2.readlines()[:10]

        plaintext.delete(1.0, tk.END)
        for line1, line2 in zip(lines1, lines2):
            plaintext.insert(tk.END, f"{line1.strip()} - {line2.strip()}\n")

def rsa_decrypt(plain, cipher):
    return RSAattack.assignValues(1024,plain)

def vigenere_decrypt(plaintext, ciphertext):
    key = ''
    plaintext=plaintext.upper().replace(' ', '')
    ciphertext=ciphertext.upper().replace(' ', '')
    for p, c in zip(plaintext, ciphertext):
        key_char = (ord(c) - ord(p)) % 26
        key += chr(key_char + 65)
        decrypted_output.delete('1.0', tk.END)
        decrypted_output.insert(tk.END, key)
    return key
def playfair(str1,str2):
    return  str1+str2
def des_decrypt(str1,str2):
    
    return str1+str2
def process_and_show_decrypted():
    algorithm = algorithm_var.get()
    lines = plaintext.get(1.0, tk.END).strip().split('\n')
    decrypted_output.delete(1.0, tk.END)

    for line in lines:
        str1, str2 = line.split(' - ')
        if algorithm == "RSA":
            # RSAattack.assignValues(64,str1.strip())
            # process = subprocess.Popen(['python', 'RSAattack.py',str1.strip()])
            # process.wait()
            RSAattack.assignValues(64,str1.strip())
            decrypted_output.insert(tk.END, str(clipboard.paste()))
        elif algorithm == "Vigenere":
            decrypted_text = vigenere_decrypt(str1, str2)
        elif algorithm=="Playfair":
            #decrypted_text=playfair(str1,str2)
            process = subprocess.Popen(['python', 'temp2.py',str2])
            process.wait()
            decrypted_output.insert(tk.END, str(clipboard.paste()))
        elif algorithm=="DES":
            decrypted_text=des_decrypt(str1,str2)             
            # process = subprocess.Popen(['python', 'DESMIM2.py']) #passing cipher only as arguments
            # process.wait()
            # decrypted_output.insert(tk.END, str(clipboard.paste()))
        elif algorithm=="Vigenere COA":
            decrypted_output.insert(tk.END, "please wait...\n")
            clipboard.copy('')
            process = subprocess.Popen(['python', 'vigenereHacker.py',str2.strip()]) #passing cipher only as arguments
            process.wait()
            decrypted_output.insert(tk.END, str(clipboard.paste()))
        else:
            decrypted_text = "Invalid algorithm"
        if algorithm!="Vigenere COA" and algorithm!="RSA":
            decrypted_output.insert(tk.END, decrypted_text + "\n")
        frequencyCharGraph.plot_char_frequencies(str1,str2)
def save_decrypted_output():
    decrypted_text = decrypted_output.get(1.0, tk.END).strip()
    with open("keys.txt", "a") as file:
        file.write(decrypted_text + "\n")

root = tk.Tk()
root.title("Cryptanalysis Tool")
root.geometry("600x400")

open_text_button = tk.Button(root, text="Open plain text and cipher text from txt files", command=open_text_files)
open_text_button.pack(pady=5)

plaintext = Text(root, height=10)
plaintext.pack(pady=5)

# Dropdown menu to choose between RSA, Playfair, DES, and Vigenere
algorithm_var = tk.StringVar()
algorithm_var.set("Choose algorithm")
algorithm_menu = ttk.Combobox(root, textvariable=algorithm_var, values=["RSA", "Playfair", "DES", "Vigenere","Vigenere COA"])
algorithm_menu.pack(pady=10)

process_button = tk.Button(root, text="Decrypt and Show", command=process_and_show_decrypted)
process_button.pack(pady=10)

decrypted_output = Text(root, height=10)
decrypted_output.pack(pady=5)

# Save button
save_button = tk.Button(root, text="Save to keys.txt", command=save_decrypted_output)
save_button.pack(pady=5)

root.mainloop()
