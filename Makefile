NAME_CRP = crypto
NAME_DCRP = decrypto

all: init $(NAME_CRP) $(NAME_DCRP)

init:
	pip install pyinstaller

$(NAME_CRP):
	python3 -m PyInstaller --onefile --name $(NAME_CRP) crypto.py

$(NAME_DCRP):
	python3 -m PyInstaller --onefile --name $(NAME_DCRP) decrypto.py