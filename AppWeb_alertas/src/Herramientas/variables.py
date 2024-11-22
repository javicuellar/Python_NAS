import os
from dotenv import load_dotenv



class Variables():
    def __init__(self) -> None:
        if os.name == 'nt':
            load_dotenv('\\Python\\config.env')
        else:
            load_dotenv('./config.env')

        self.usuario = os.getenv("USER_MAIL")
        self.password = os.getenv("PASSWORD_MAIL")
        self.destinatario = os.getenv("DESTINATARIO_MAIL")