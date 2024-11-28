import pandas as pd
import matplotlib.pyplot as plt
import os

def Plot_Figure(file_path, n):
    fig = plt.figure(n)
    raw_df = pd.read_csv(file_path)
    
    # correct for gravity in z axis
    raw_df[" zAccel [m/s/s]"] = raw_df[" zAccel [m/s/s]"].apply(lambda x: x+9.81)

    plt.plot(raw_df[" inc time [s]"], raw_df[" xAccel [m/s/s]"], label="X Axis")
    plt.plot(raw_df[" inc time [s]"], raw_df[" yAccel [m/s/s]"], label="Y Axis")
    plt.plot(raw_df[" inc time [s]"], raw_df[" zAccel [m/s/s]"], label="Z Axis")

    plt.xlabel("Inc Time (s)")
    plt.ylabel("Acceleration (m/s/s)")
    plt.title(os.path.basename(file_path))
    plt.legend()
    fig.show()

def Plot_Raw_Data():
    raw_data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"raw_data")        
    raw_file_list = [os.path.join(raw_data_dir, f) for f in os.listdir(raw_data_dir) if os.path.isfile(os.path.join(raw_data_dir, f))]  
    
    for i in range(len(raw_file_list)):
        file_path = raw_file_list[i]
        Plot_Figure(file_path, i+1)
    
Plot_Raw_Data()

input()