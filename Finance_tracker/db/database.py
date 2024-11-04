# database.py

import sqlite3

class Database:
    def __init__(self, db_file):
        """Inizializza la connessione al database."""
        self.connection = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        """Crea le tabelle necessarie nel database."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    status TEXT,
                    balance REAL NOT NULL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    amount REAL NOT NULL,
                    transaction_type TEXT NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS investments (
                    id INTEGER PRIMARY KEY,
                    principal REAL NOT NULL,
                    interest_rate REAL NOT NULL,
                    duration_years INTEGER NOT NULL,
                    investment_type TEXT
                )
            ''')

    def insert_account(self, account):
        with self.connection:
            self.connection.execute('''
                INSERT INTO accounts (name, status, balance) VALUES (?, ?, ?)
            ''', (account.name, account.status, account.balance))

    def get_accounts(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM accounts')
        return cursor.fetchall()

    def delete_account(self, account_id):
        with self.connection:
            self.connection.execute('DELETE FROM accounts WHERE id = ?', (account_id,))

    def insert_transaction(self, transaction):
        with self.connection:
            self.connection.execute('''
                INSERT INTO transactions (amount, transaction_type, description, date) VALUES (?, ?, ?, ?)
            ''', (transaction.amount, transaction.transaction_type, transaction.description, transaction.date.isoformat()))

    def get_transactions(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM transactions')
        return cursor.fetchall()

    def delete_transaction(self, transaction_id):
        with self.connection:
            self.connection.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))

    def insert_investment(self, investment):
        with self.connection:
            self.connection.execute('''
                INSERT INTO investments (principal, interest_rate, duration_years, investment_type) VALUES (?, ?, ?, ?)
            ''', (investment.principal, investment.interest_rate, investment.duration_years, investment.investment_type))

    def get_investments(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM investments')
        return cursor.fetchall()

    def delete_investment(self, investment_id):
        with self.connection:
            self.connection.execute('DELETE FROM investments WHERE id = ?', (investment_id,))

    def close(self):
        """Chiude la connessione al database."""
        self.connection.close()
