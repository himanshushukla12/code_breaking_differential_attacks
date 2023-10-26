# README

## Project Workflow

This project consists of two main modules, designed for generating encryption keys, encrypting plaintext, and performing cryptanalysis on the ciphertext. Here is the step-by-step workflow of the project:

### Module 1: Key Generation and Encryption

1. **Install Dependencies:**
    - Ensure you have the required dependencies installed:
        - `pycryptodome`
        - `libnum`
        - `matplotlib`
        - `seaborn`
        - `pyperclip`
        - `tkinter`

2. **Key Generation:**
    - Run `keyGenUI.py` to open the Key Generator UI window.
    - In the Key Generator window, choose the encryption algorithm (DES, RSA, or Vigenere) from the drop-down menu.
    - Click on the "Generate Key" button to create the encryption key for the selected algorithm.
    - Use the "Copy Key" button to copy the generated key to the clipboard, or click on "Save Key to the File" to save the key in a text file.

3. **Encryption:**
    - Run `CipherGenerationUI.py` to open the Encryption Tool UI window.
    - Input the plaintext you want to encrypt.
    - Select the same encryption algorithm from the drop-down menu as chosen in the Key Generator window.
    - Paste the copied key into the "Secret Key" text box.
    - Click on the "Encrypt and Save" button to encrypt the plaintext and save the ciphertext. The plaintext, keys, and ciphertexts are saved in separate text files and displayed in the result box within the window.

### Module 2: Cryptanalysis

4. **Cryptanalysis:**
    - Run `SecondModule.py` to open the Cryptanalysis UI window.
    - Click on the "Open Cipher Texts and Plain Texts from Files" button to load the ciphertexts and plaintexts from their respective text files.
    - Choose the encryption algorithm from the drop-down menu, the same one used in the first module.
    - Click on the "Decrypt and Show" button to perform cryptanalysis on the loaded ciphertexts. The decrypted plaintext will be displayed in the result box.

5. **Frequency Analysis:**
    - Frequency analysis graphs for the plaintext and ciphertext are generated and displayed in the Cryptanalysis UI window.

This concludes the second module of the project, showcasing the complete workflow of the encryption and cryptanalysis processes.
