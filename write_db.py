import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# cursor.execute('''
#     insert into estudantes(nome, idade) \
#     values(?, ?)
# ''',
#                ("Joana", 16)
# )

cursor.execute(
    '''
    insert into disciplinas(
        estudante_id, nome_disciplina
    ) values(?, ?)
    ''',
    (1, "Matemática")
               )

conn.commit()
conn.close()