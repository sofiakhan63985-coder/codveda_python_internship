from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key


def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return None

    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)
    encrypted_path = file_path + ".enc"
    with open(encrypted_path, "wb") as file:
        file.write(encrypted)

    print(f"Encrypted file saved as {encrypted_path}")
    return encrypted_path


def decrypt_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return None

    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted = fernet.decrypt(encrypted_data)
    out_path = file_path.replace(".enc", "_decrypted.txt")
    with open(out_path, "wb") as file:
        file.write(decrypted)

    print(f"Decrypted file saved as {out_path}")
    return out_path


if __name__ == "__main__":
    if not os.path.exists(KEY_FILE):
        generate_key()

    action = input("Choose action (encrypt/decrypt): ").strip().lower()
    path = input("Enter file path: ").strip()

    if action == "encrypt":
        encrypt_file(path)
    elif action == "decrypt":
        decrypt_file(path)
    else:
        print("Invalid option selected.")