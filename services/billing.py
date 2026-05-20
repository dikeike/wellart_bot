import sqlite3
from config import DB_PATH

# -----------------------------------------------------
# Инициализация БД
# -----------------------------------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            credits INTEGER DEFAULT 5
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------------------------------
# Получить баланс пользователя
# -----------------------------------------------------
def get_balance(user_id: int) -> int:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT credits FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()

    if row:
        balance = row[0]
    else:
        cursor.execute("INSERT INTO users (user_id, credits) VALUES (?, ?)", (user_id, 5))
        conn.commit()
        balance = 5

    conn.close()
    return balance


# -----------------------------------------------------
# Списать кредиты
# -----------------------------------------------------
def charge_user(user_id: int, amount: int) -> bool:
    balance = get_balance(user_id)

    if balance < amount:
        return False

    new_balance = balance - amount

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET credits = ? WHERE user_id = ?", (new_balance, user_id))
    conn.commit()
    conn.close()
    return True


# -----------------------------------------------------
# Начислить кредиты
# -----------------------------------------------------
def add_credits(user_id: int, amount: int):
    balance = get_balance(user_id)
    new_balance = balance + amount

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET credits = ? WHERE user_id = ?", (new_balance, user_id))
    conn.commit()
    conn.close()