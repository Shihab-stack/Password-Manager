import os
from dotenv import load_dotenv  # 1. Import the loader
from encryption_decryption import generate_password_key, encrypt_data, decrypt_data

# 2. Load the variables from your .env file into the environment
load_dotenv()

# 3. Pull the password securely
key_pass = os.getenv("MASTER_PASSWORD")

while True:
    # 1. Log In Screen (Only happens once per app launch!)
    input_pass = input(
        "\nEnter password for your password manager (or 'q' to quit): ")

    if input_pass.lower() == 'q':
        break

    if key_pass == input_pass:
        key = generate_password_key(key_pass)
        print("🔓 Access Granted!  ")
        while True:
            prmpt = input(
                "What do you want? add|view  q for quit        ").lower()
            if prmpt == 'q':
                break
            if prmpt == 'add':
                idd = input("Write the id:  ")
                passs = input("Enter to save the password:  ")
                with open("src.txt", "a") as f:
                    enc_pass = passs.encode()
                    encry_pass = encrypt_data(enc_pass, key)
                    f.write(f"{idd}"+"\n"+f"{encry_pass.decode()}"+"\n")
                    print("Succcessfully Saved  ")
            elif prmpt == 'view':
                if not os.path.exists("src.txt"):
                    print("No passwords saved yet. ")
                    continue
                with open("src.txt", "r") as f:
                    words = f.read().strip().split("\n")
                if words == [""]:
                    print("No passwords saved yet. ")
                    continue
                i = 1
                for word in words:
                    if i % 2 != 0:
                        print(f"ID    : {word}")

                    else:
                        byte_word = word.encode()
                        drcypted = decrypt_data(byte_word, key)
                        decoded = drcypted.decode()
                        print(f"PASS    :{decoded}")
                    i = i+1

    else:
        print("Wrong password(master)! try again!")
