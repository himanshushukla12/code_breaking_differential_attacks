import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
import rsa as rsa
from Crypto.Cipher import DES
import RSAattack
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import itertools
import string
import itertools

os.chdir(os.getcwd())

#vigenere working fine
def vigenere_encrypt(plaintext, key):
    def char_shift(c, k, encrypt=True):
        if encrypt:
            return chr(((ord(c) - ord('A')) + (ord(k) - ord('A'))) % 26 + ord('A'))
        else:
            return chr(((ord(c) - ord('A')) - (ord(k) - ord('A'))) % 26 + ord('A'))

    ciphertext = []
    key = itertools.cycle(key.upper())

    for c in plaintext.upper():
        if c.isalpha():
            k = next(key)
            ciphertext.append(char_shift(c, k))
        else:
            ciphertext.append(c)

    return "".join(ciphertext)
def generate_playfair_key(keyword):
    keyword = keyword.upper().replace("J", "I")
    key = "".join(sorted(set(keyword), key=keyword.index))
    key += "".join(c for c in string.ascii_uppercase if c not in key and c != "J")
    return [key[i:i + 5] for i in range(0, 25, 5)]

def generate_key_table(keyword):
    keyword = keyword.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_table = ""

    for char in keyword:
        if char not in key_table and char in alphabet:
            key_table += char

    for char in alphabet:
        if char not in key_table:
            key_table += char

    return [key_table[i:i+5] for i in range(0, 25, 5)]

def prepare_text(text):
    text = text.upper().replace("J", "I")
    prepared_text = ""
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i+1]:
            prepared_text += text[i] + "X"
            i += 1
        else:
            prepared_text += text[i:i+2]
            i += 2
    if len(prepared_text) % 2 == 1:
        prepared_text += "X"
    return prepared_text

def find_position(key_table, char):
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == char:
                return row, col
    return None
import re
def playfair_encrypt(plain_text, keyword):
    plain_text= re.sub(r'[^a-zA-Z]', '', plain_text)
    plain_text = plain_text.replace(" ", "")
    key_table = generate_key_table(keyword)
    prepared_text = prepare_text(plain_text)
    print(key_table)
    print("plaintext",plain_text)
    print("preparedtext",prepared_text)
    encrypted_text = ""

    for i in range(0, len(prepared_text), 2):
        row1, col1 = find_position(key_table, prepared_text[i])
        row2, col2 = find_position(key_table, prepared_text[i+1])

        if row1 == row2:
            encrypted_text += key_table[row1][(col1+1)%5] + key_table[row2][(col2+1)%5]
        elif col1 == col2:
            encrypted_text += key_table[(row1+1)%5][col1] + key_table[(row2+1)%5][col2]
        else:
            encrypted_text += key_table[row1][col2] + key_table[row2][col1]

    return encrypted_text
def playfair_encrypt2(plaintext, key_matrix):
    def find_char_position(c):
        for i, row in enumerate(key_matrix):
            if c in row:
                return i, row.index(c)
        return None

    plaintext = plaintext.upper().replace("J", "I")
    plaintext = "".join(c for c in plaintext if c.isalpha())
    pairs = list(itertools.zip_longest(*[iter(plaintext)] * 2, fillvalue="X"))
    ciphertext = []

    for p1, p2 in pairs:
        r1, c1 = find_char_position(p1)
        r2, c2 = find_char_position(p2)

        if r1 == r2:
            ciphertext.extend([key_matrix[r1][(c1 + 1) % 5], key_matrix[r2][(c2 + 1) % 5]])
        elif c1 == c2:
            ciphertext.extend([key_matrix[(r1 + 1) % 5][c1], key_matrix[(r2 + 1) % 5][c2]])
        else:
            ciphertext.extend([key_matrix[r1][c2], key_matrix[r2][c1]])

    return "".join(ciphertext)
def generate_rsa_key_pair(bits=1024):
    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key.decode(), public_key.decode()

def rsa_encrypt(plaintext, public_key):
    public_key_obj = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key_obj)
    return cipher.encrypt(plaintext.encode())

def rsa_decrypt(ciphertext, private_key):
    private_key_obj = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key_obj)
    return cipher.decrypt(ciphertext).decode()


#double DES used for 64 bit keys
def des_encrypt(plaintext, key):
    # Pad the plaintext to a multiple of 8 bytes
    padding_length = 8 - (len(plaintext) % 8)
    plaintext = plaintext.encode()
    plaintext += bytes([padding_length] * padding_length)

    # Initialize the DES cipher with the key
    cipher = DES.new(key, DES.MODE_ECB)

    # Encrypt the plaintext using DES
    ciphertext = cipher.encrypt(plaintext)

    # Return the ciphertext
    return ciphertext


# from Crypto.Cipher import DES3

# def des_encrypt(plaintext, key):
#     # Pad the plaintext to a multiple of 8 bytes
#     padding_length = 8 - (len(plaintext) % 8)
#     plaintext = plaintext.encode()
#     plaintext += bytes([padding_length] * padding_length)

#     # Generate 3 keys from the provided key
#     key1 = key[:8]
#     key2 = key[8:16]
#     key3 = key[16:]

#     # Initialize the Triple DES cipher with the 3 keys
#     cipher = DES3.new(key1 + key2 + key3, DES3.MODE_ECB)

#     # Encrypt the plaintext using Triple DES
#     ciphertext = cipher.encrypt(plaintext)

#     # Return the ciphertext
#     return ciphertext





def encrypt_and_save():
    plaintext = plaintext_entry.get()
    algorithm = algorithm_combobox.get()
    secret_key = key_entry.get()
    global attack_type
    attack_type=None
    if algorithm == "Playfair Cipher":
        attack_type="Playfair Cipher"
        ciphertext= playfair_encrypt(plaintext,secret_key)
            
    elif algorithm == "Vigenere Cipher":
        attack_type='Vigenere_Cipher'
        ciphertext = vigenere_encrypt(plaintext, secret_key)
  
    elif algorithm == "DES":
        ciphertext = des_encrypt(plaintext, bytes.fromhex(secret_key))
            
  
    elif algorithm == "RSA":
        private_key, public_key = generate_rsa_key_pair()
        ciphertext = rsa_encrypt(plaintext, public_key)
        
    if attack_type == 'Vigenere_Cipher'or attack_type=="Playfair Cipher":
        with open("ciphertext.txt", "a") as cipher_file:
            cipher_file.write(ciphertext + "\n")
            ciphertext_entry.delete(0, tk.END)
            ciphertext_entry.insert(10, str(ciphertext))
        with open("plaintext.txt", "a") as plaintext_file:
            plaintext_file.write(plaintext + "\n")
            
    else:
        with open("ciphertext.txt", "a") as cipher_file:
            cipher_file.write(ciphertext.hex() + "\n")
        with open("plaintext.txt", "a") as plaintext_file:
            plaintext_file.write(plaintext + "\n")
        ciphertext_entry.delete(0, tk.END)
        ciphertext_entry.insert(0, str(ciphertext.hex()))
    
        
    

    
    showinfo("Success", "Plaintext and ciphertext have been saved.")

app = tk.Tk()
app.title("Encryption Tool")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

plaintext_label = ttk.Label(frame, text="Plaintext:")
plaintext_label.grid(row=0, column=0, sticky=tk.W)
plaintext_entry = ttk.Entry(frame, width=40)
plaintext_entry.grid(row=0, column=1)

algorithm_label = ttk.Label(frame, text="Algorithm:")
algorithm_label.grid(row=1, column=0, sticky=tk.W)
algorithm_combobox = ttk.Combobox(
    frame, values=["Playfair Cipher", "Vigenere Cipher", "DES", "RSA"], state="readonly"
)
algorithm_combobox.grid(row=1, column=1)
algorithm_combobox.current(0)

key_label = ttk.Label(frame, text="Secret Key:")
key_label.grid(row=2, column=0, sticky=tk.W)
key_entry = ttk.Entry(frame, width=40)
key_entry.grid(row=2, column=1)

encrypt_button = ttk.Button(frame, text="Encrypt and Save", command=encrypt_and_save)
encrypt_button.grid(row=3, column=0, columnspan=2)

ciphertext_label = ttk.Label(frame, text="Ciphertext: ")
ciphertext_label.grid(row=4, column=0, sticky=tk.W)
ciphertext_entry = ttk.Entry(frame, width=40)
ciphertext_entry.grid(row=4, column=1)
app.mainloop()

