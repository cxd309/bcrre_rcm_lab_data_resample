import pandas as pd
import matplotlib.pyplot as plt
import os

def Plot_Figure(file_path):
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
    plt.show()
    
def Get_Raw_Data_Contents():
    raw_data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"raw_data")        
    return [os.path.join(raw_data_dir, f) for f in os.listdir(raw_data_dir) if os.path.isfile(os.path.join(raw_data_dir, f)) and os.path.splitext(f)[1]== ".csv"]

def File_Selector():
    file_list = Get_Raw_Data_Contents()
    
    if len(file_list)<1:
        print("No valid files in directory")
        input()
        return
    
    valid_option_list = []
    print("Select file to plot:")
    for i in range(len(file_list)):
        file_path = file_list[i]
        print(str(i)+". "+os.path.basename(file_path))
        valid_option_list.append(str(i))
    file_no = input()
    if file_no in valid_option_list:
        Plot_Figure(file_list[int(file_no)])
    else:
        print("Invalid option selection")
        input()
    
while(1):
    File_Selector()