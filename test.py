import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    if table_name == "sqlite_sequence":
        continue
    else:
        print(f"\n📋 Table: {table_name}")
        print("-" * 40)

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Get column names
        column_names = [description[0] for description in cursor.description]
        print(" | ".join(column_names))
        print("-" * 40)

        if rows:
            for row in rows:
                print(" | ".join(str(value) for value in row))
        else:
            print("None")

conn.close()



