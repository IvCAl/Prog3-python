import getpass

class Email():
    def __init__(self,id: str, domain: str):
        self.id = id
        self.domain = domain
        self.password = self.create_password()

    def show_account(self) -> str:
        return f"Correo Electronico: {self.id}@{self.domain}"

    def create_password(self) -> str:
        while True:
            password = getpass.getpass('Ingrese una contraseña: ',)
            confirm_password = getpass.getpass('Vuelva a ingresar la contraseña: ')
            if password != confirm_password:
                print('Las contraseñas no coinciden')
            else:
                print('Guardado con exito') 
                return password

    def get_pass(self):
        return f'Contraseña: {self.password}'

test = Email('correo','hotmail.com')

print(test.show_account())
print(test.get_pass())