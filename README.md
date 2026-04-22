# Caesar Crypto

A simple Caesar cipher cryptography application with a graphical user interface.

## What is Caesar Cipher?

Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

## Project Structure

- `crypto.py` - Encryption application (encrypts text using a Caesar cipher)
- `decrypto.py` - Decryption application (decrypts Caesar cipher text)
- `Makefile` - Build automation file

## Requirements

- Python 3.x
- tkinter (included with Python)
- PyInstaller (for building executables)

## How to Execute

### Running Directly

To run the encryption program:
```bash
python3 crypto.py
```

To run the decryption program:
```bash
python3 decrypto.py
```

### Building Executables

To build both the encryption and decryption executables:
```bash
make all
```

Or build them individually:
```bash
make crypto    # Builds the encryptor
make decrypto  # Builds the decryptor
```

The built executables will be located in the `dist/` directory.

## How to Use

1. **Run the application** (`python3 crypto.py` for encryption)
2. **Enter the text** you want to encrypt in the text field
3. **Enter the shift key** (an integer that determines how many positions each letter is shifted)
4. **Click "Crypter"** to encrypt the text
5. **Copy the encrypted result** from the output field

To decrypt, use `decrypto.py` with the same shift key that was used for encryption.