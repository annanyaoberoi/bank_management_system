
import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  
        database="bank_sys"
    )

def create_account(acc_no, name, dob, address, mob_no, initial_balance=0):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO accounts (acc_no, name, dob, address, mob_no, balance) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (acc_no, name, dob, address, mob_no, initial_balance)
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()

def record_transaction(acc_no, tx_type, amount):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        delta = amount if tx_type == 'deposit' else -amount
        cur.execute("UPDATE accounts SET balance = balance + %s WHERE acc_no = %s",
                    (delta, acc_no))
        cur.execute("INSERT INTO transactions (acc_no, type, amount) VALUES (%s, %s, %s)",
                    (acc_no, tx_type, amount))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def get_balance(acc_no):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row[0] if row else None

def get_statement(acc_no):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT tx_id, type, amount, ts FROM transactions "
        "WHERE acc_no = %s ORDER BY ts DESC",
        (acc_no,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
