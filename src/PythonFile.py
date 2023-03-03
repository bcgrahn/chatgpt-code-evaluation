import os

class PythonFile:
    def create(responses, fileNames):

        folder_path = "./public/ResponseFiles"
        
        for response, fileName in zip(responses, fileNames):
            # Define the file name and the code to be written to the file

            file_path = os.path.join(folder_path, fileName)

            if os.path.exists(file_path):
                os.remove(file_path)
                print("[Delete old file] " + fileName)

            # Create a new file and write the dummy code to it
            with open(file_path, "w") as f:
                print("[create python file] " + fileName)
                f.write(response)

            # if os.path.isfile(file_name):
            #     print(f"File {file_name} created successfully.")
            # else:
            #     print(f"Error: could not create {file_name}.")
                    