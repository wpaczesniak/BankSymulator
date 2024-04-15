from clase_iban import IBAN
from clase_operacion import OperacionBancaria
from clase_pila import Pila


class CuentaBancaria:
    def __init__(self, iban, titular, balance):
        self.iban = IBAN(iban)  # Użycie klasy IBAN
        self.titular = titular
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = balance
        self.operaciones = Pila()  # Pila do przechowywania operacji

    def GetIBAN(self):
        return self.iban

    def GetTitular(self):
        return self.titular

    def GetBalance(self):
        return self.balance

    def Ingresar(self, amount, concepto):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.operaciones.Apilar(OperacionBancaria(amount, concepto))  # Zapis operacji

    def Retirar(self, amount, concepto):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds in the account")
        self.balance -= amount
        self.operaciones.Apilar(OperacionBancaria(-amount, concepto))  # Zapis operacji jako kwota negatywna

    def MostrarOperaciones(self):
        if self.operaciones.EsVacia():
            print("No hay operaciones registradas.")
        else:
            print(self.operaciones)  # Wypisanie historii operacji od najnowszej do najstarszej

    def __str__(self):
        formatted_iban = str(self.iban)  # Wywołanie __str__ klasy IBAN
        return f"IBAN: {formatted_iban}, Account Holder: {self.titular}, Balance: {self.balance} EUR"

# exercise 1

# class CuentaBancaria:
#     def __init__(self, iban, titular, balance):
#         self.iban = IBAN(iban)  # Using the IBAN class
#         self.titular = titular
#         if balance < 0:
#             raise ValueError("Initial balance cannot be negative")
#         self.balance = balance

#     def GetIBAN(self):
#         return self.iban

#     def GetTitular(self):
#         return self.titular

#     def GetBalance(self):
#         return self.balance

#     def Deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self.balance += amount

#     def Withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive")
#         if self.balance < amount:
#             raise ValueError("Insufficient funds in the account")
#         self.balance -= amount

#     def __str__(self):
#         formatted_iban = str(self.iban)  # Calling __str__ of the IBAN class
#         return f"IBAN: {formatted_iban}, Account Holder: {self.titular}, Balance: {self.balance} EUR"

# # Example of use:
# c = CuentaBancaria("ES9820385778983000760236", "P. Perez", 1000)
# print(c)  # Displays initial account information

# c.Deposit(500)
# print(c.GetBalance())  # Should display 1500

# c.Withdraw(300)
# print(c.GetBalance())  # Should display 1200


#  test - exercise 1

# Example of use:
# c = CuentaBancaria("ES9820385778983000760236", "P. Perez", 1000)
# print(c)  # Displays initial account information

# c.Deposit(500)
# print(c.GetBalance())  # Should display 1500

# c.Withdraw(300)
# print(c.GetBalance())  # Should display 1200