# main.py

from models.account import Account
from models.transaction import Transaction
from models.investment import Investment
from db.database import Database
from datetime import datetime

# Inizializza il database
db = Database('finances.db')

def display_accounts():
    accounts = db.get_accounts()
    if accounts:
        for account in accounts:
            print(account)
    else:
        print("Nessun account disponibile.")

def add_account():
    name = input("Nome dell'account: ")
    status = input("Stato dell'account (es. active): ")
    balance = float(input("Saldo iniziale: "))
    account = Account(name, status, balance)
    db.insert_account(account)
    print("Account aggiunto con successo.")

def delete_account():
    display_accounts()
    idx = int(input("Inserisci l'ID dell'account da eliminare: "))
    db.delete_account(idx)
    print("Account eliminato.")

def display_transactions():
    transactions = db.get_transactions()
    if transactions:
        for transaction in transactions:
            print(transaction)
    else:
        print("Nessuna transazione disponibile.")

def add_transaction():
    amount = float(input("Importo: "))
    transaction_type = input("Tipo (income o expense): ")
    description = input("Descrizione: ")
    date = datetime.now()
    transaction = Transaction(amount, transaction_type, description, date)
    db.insert_transaction(transaction)
    print("Transazione aggiunta con successo.")

def delete_transaction():
    display_transactions()
    idx = int(input("Inserisci l'ID della transazione da eliminare: "))
    db.delete_transaction(idx)
    print("Transazione eliminata.")

def display_investments():
    investments = db.get_investments()
    if investments:
        for investment in investments:
            print(investment)
    else:
        print("Nessun investimento disponibile.")

def add_investment():
    principal = float(input("Importo iniziale: "))
    interest_rate = float(input("Tasso di interesse (decimale, es. 0.05 per 5%): "))
    duration_years = int(input("Durata in anni: "))
    investment_type = input("Tipo di investimento (es. stock): ")
    investment = Investment(principal, interest_rate, duration_years, investment_type)
    db.insert_investment(investment)
    print("Investimento aggiunto con successo.")

def delete_investment():
    display_investments()
    idx = int(input("Inserisci l'ID dell'investimento da eliminare: "))
    db.delete_investment(idx)
    print("Investimento eliminato.")

def manage_accounts():
    while True:
        print("\nGestione Account:")
        print("1. Visualizza Account")
        print("2. Aggiungi Account")
        print("3. Elimina Account")
        print("4. Torna al menu principale")
        choice = input("Scegli un'opzione: ")

        if choice == "1":
            display_accounts()
        elif choice == "2":
            add_account()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            break
        else:
            print("Scelta non valida. Riprova.")

def manage_transactions():
    while True:
        print("\nGestione Transazioni:")
        print("1. Visualizza Transazioni")
        print("2. Aggiungi Transazione")
        print("3. Elimina Transazione")
        print("4. Torna al menu principale")
        choice = input("Scegli un'opzione: ")

        if choice == "1":
            display_transactions()
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            break
        else:
            print("Scelta non valida. Riprova.")

def manage_investments():
    while True:
        print("\nGestione Investimenti:")
        print("1. Visualizza Investimenti")
        print("2. Aggiungi Investimento")
        print("3. Elimina Investimento")
        print("4. Torna al menu principale")
        choice = input("Scegli un'opzione: ")

        if choice == "1":
            display_investments()
        elif choice == "2":
            add_investment()
        elif choice == "3":
            delete_investment()
        elif choice == "4":
            break
        else:
            print("Scelta non valida. Riprova.")

def main_menu():
    while True:
        print("\nMenu principale:")
        print("1. Gestisci Account")
        print("2. Gestisci Transazioni")
        print("3. Gestisci Investimenti")
        print("4. Esci")
        choice = input("Scegli un'opzione: ")

        if choice == "1":
            manage_accounts()
        elif choice == "2":
            manage_transactions()
        elif choice == "3":
            manage_investments()
        elif choice == "4":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    try:
        main_menu()
    finally:
        db.close()  # Assicurati di chiudere la connessione al database
