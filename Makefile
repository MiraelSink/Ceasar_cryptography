NAME_CRP = crypto
NAME_DCRP = decrypto

all: init $(NAME_CRP) $(NAME_DCRP)

init:
	pip install pyinstaller

$(NAME_CRP):
	pyinstaller --onefile --name $(NAME_CRP) crypto.py

$(NAME_DCRP):
	pyinstaller --onefile --name $(NAME_DCRP) decrypto.py