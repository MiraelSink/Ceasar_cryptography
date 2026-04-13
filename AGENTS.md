# Repository Guidelines

## Project Structure & Module Organization
This repository contains two small GUI entry points built with `tkinter`:

- `crypto.py`: Caesar-style text encryption window.
- `decrypto.py`: Caesar-style text decryption window.
- `Makefile`: build and cleanup targets for PyInstaller packaging.
- `Crypter.png`, `Decrypter.png`, `cesar.ico`: UI assets used by the desktop windows.

Build artifacts are generated into `build/`, `dist/`, and `*.spec` files. Keep source files at the repository root unless the project is intentionally reorganized.

## Build, Test, and Development Commands
- `python3 crypto.py`: run the encryption GUI locally.
- `python3 decrypto.py`: run the decryption GUI locally.
- `make`: install `pyinstaller` and build both executables.
- `make crypto`: package only the encryptor.
- `make decrypto`: package only the decryptor.
- `make fclean`: remove `build/`, `dist/`, `__pycache__/`, and generated `.spec` files.

Run commands from the repository root so image paths such as `Crypter.png` resolve correctly.

## Coding Style & Naming Conventions
Use Python with 4-space indentation and `snake_case` for functions and variables. Prefer explicit imports over expanding the current wildcard `tkinter` import in new code. Keep UI labels, colors, and asset names consistent between `crypto.py` and `decrypto.py`.

When adding logic, separate UI setup from transformation code where possible. Example: keep Caesar-shift logic in a small helper such as `encrypt_text(text, key)`.

## Testing Guidelines
There is no automated test suite yet. For now, verify changes manually by running both GUIs and checking:

- normal text encrypt/decrypt flow
- empty input behavior
- invalid key input handling
- asset loading from the repo root

If tests are added, prefer `unittest` with files named `test_*.py`, and focus first on the text transformation logic rather than the GUI.

## Commit & Pull Request Guidelines
Recent history uses short Conventional Commit prefixes such as `feat:` and `fix:`. Follow that pattern, for example: `fix: validate empty key input`.

Pull requests should include a brief summary, the user-visible behavior change, manual test steps, and screenshots for UI changes. Keep PRs small and focused on one script or one behavior at a time.
