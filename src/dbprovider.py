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
            print("[Table not deleted]")

        #create new table
        cursor.execute("CREATE TABLE Data (ID INTEGER PRIMARY KEY, Prompt TEXT, Response TEXT, Evaluation TEXT)")
        i = 1
        
        for prompt, response, evaluation, in zip(prompts, responses, evaluations):
            # Insert data into the table
            query = f"INSERT INTO Data (ID, Prompt, Response, Evaluation) VALUES ('{i}', '{prompt}', '{response}', '{evaluation}')"
            
            try:
                cursor.execute(query)
                print("[Write to db] " + str(i))
            except pyodbc.ProgrammingError:
                print("[Unable to write] " + str(i))

            i = i + 1
                
            conn.commit()

        # Close the connection
        conn.close()
