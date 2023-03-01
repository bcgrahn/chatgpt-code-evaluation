import pyodbc

class dbprovider:

    def start(prompts, responses, evaluations):
        # Connect to the Microsoft Access database
        conn_str = (
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=./database/database.accdb;"
        )
        conn = pyodbc.connect(conn_str)

        tableName = "Data"

        # Create a table
        cursor = conn.cursor()

        try:
            cursor.execute(f"DROP TABLE {tableName}")
            conn.commit()
        except:
            print("not deleted")

        # cursor.execute(f"SELECT COUNT(*) FROM MSysObjects WHERE Name='{tableName}' AND Type=1")
        # result = cursor.fetchone()
        
        cursor.execute("CREATE TABLE Data (ID INTEGER PRIMARY KEY, Prompt TEXT, Response TEXT, Evaluation TEXT)")
       
        i = 1
        
        for prompt, response, evaluation, in zip(prompts, responses, evaluations):
            # Insert data into the table
            print("[Write to db] " + str(i))
            query = f"INSERT INTO Data (ID, Prompt, Response, Evaluation) VALUES ('{i}', '{prompt}', '{response}', '{evaluation}')"
            i = i + 1
            cursor.execute(query)
        conn.commit()

        # Fetch data from the table
        # cursor.execute("SELECT * FROM Users")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)

        # Close the connection
        conn.close()
