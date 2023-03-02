import os

class PythonFile:
    def create(responses, fileNames):

        
        for response, fileName in zip(responses, fileNames):
            # Define the file name and the code to be written to the file

            if os.path.exists(fileName):
                os.remove(fileName)
                print("[Delete old file] " + fileName)

            # Create a new file and write the dummy code to it
            with open(fileName, "w") as f:
                print("[create python file] " + fileName)
                f.write(response)

            # if os.path.isfile(file_name):
            #     print(f"File {file_name} created successfully.")
            # else:
            #     print(f"Error: could not create {file_name}.")
                    