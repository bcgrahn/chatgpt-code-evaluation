import os

class PythonFile:
    def create(responses, type):

        folder_path = "./public/ResponseFiles"

        i = 1
        for response in responses:
            # Define the file name and the code to be written to the file
            fileName = f"response{i}({type}).py"
            file_path = os.path.join(folder_path, fileName)
            i = i + 1
            
            #remove old file if it exists
            if os.path.exists(file_path):
                os.remove(file_path)
                print("[Delete old file] " + fileName)

            # Create a new file and write the dummy code to it
            with open(file_path, "w") as f:
                print("[create python file] " + fileName)
                f.write(response)

            

                    