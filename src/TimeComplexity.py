import time
import matplotlib.pyplot as plt
import os

def plot_time_complexity(data, name):
    x = list(range(len(data)))
    y = data

    plt.plot(x, y, label = name)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    return

def measure_time_complexity(fileNames):

    input_sizes = list(range(1, 101))

    timeEvaluations = []
    folder_path = "./public/ResponseFiles/"
    
    for filename in fileNames:
        file_path = os.path.join(folder_path, filename)
        # your algorithm here
        command = f"python {file_path}"

        times =[]

        for size in input_sizes:

            start_time = time.time()
            os.system(command)
            end_time = time.time()
            time_taken = end_time - start_time
            
            times.append(time_taken)

        plot_time_complexity(times, filename)
        print("[Evaluate time complexity] " + filename)

    plt.legend()
    plt.show()

    
