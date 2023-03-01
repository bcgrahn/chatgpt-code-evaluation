import os

class PythonFile:
    def create(responses):

        i = 1
        for response in responses:
            # Define the file name and the code to be written to the file

            filename = f"response{i}.py"
            i = i + 1

            if os.path.exists(filename):
                os.remove(filename)
                print("[Delete old file] " + filename)

            # Create a new file and write the dummy code to it
            with open(filename, "w") as f:
                print("[create python file] " + filename)
                f.write(response)

            # if os.path.isfile(file_name):
            #     print(f"File {file_name} created successfully.")
            # else:
            #     print(f"Error: could not create {file_name}.")
                    