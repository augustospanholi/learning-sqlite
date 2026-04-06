import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("""
    update estudantes SET nome = ? where \
        id = ? 
""",
               ( "Leandro", 2)
               )
conn.commit()
conn.close()

