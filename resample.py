import pandas as pd

def Resample_File(name):
    fileName = "raw_data\\"+name+".csv"
    og_df = pd.read_csv(fileName)
    ratio_list = [2,4,8,10,20]
    original_frequency = 2000
    for ratio in ratio_list:
        Downsample_DF(og_df, ratio, name, original_frequency)
        
def Conv_StringTime_Seconds(string_time):
    h, m, s = map(int, string_time.split(':'))
    return h * 3600 + m * 60 + s

def Conv_Seconds_StringTime(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02}:{m:02}:{s:02}"

def Simple_Downsample_DF(og_df, ratio):
    return og_df.iloc[::ratio]

def Average_Downsample_DF(og_df, ratio):
    avg_df = og_df.copy(deep=True)
    avg_df['Time [HH:mm:ss]'] = avg_df['Time [HH:mm:ss]'].apply(Conv_StringTime_Seconds)
    #avg_df = og_df.apply(pd.to_numeric, errors='coerce')
    avg_df = avg_df.groupby(avg_df.index // ratio).mean()
    avg_df['Time [HH:mm:ss]'] = avg_df['Time [HH:mm:ss]'].apply(Conv_Seconds_StringTime)
    
    return avg_df
    
def Downsample_DF(og_df, ratio, name, original_frequency):
    new_frequency = original_frequency/ratio
    
    simple_downsample_df = Simple_Downsample_DF(og_df, ratio)
    avg_downsample_df = Average_Downsample_DF(og_df, ratio)
    
    Save_DF(simple_downsample_df, name, "simple", new_frequency)
    Save_DF(avg_downsample_df, name, "average", new_frequency)
    
def Save_DF(df, name, ds_method, freq):
    file_name = "resampled\\" + name + "-" + ds_method + "_downsample-" + str(int(freq)) + "Hz.csv"
    print("Saving: "+file_name)
    df.to_csv(file_name, encoding='utf-8', index=False)
    
def Main():
    print("starting resampling")
    Resample_File("day_1_data")
    Resample_File("day_2_group-1-4_data")
    Resample_File("day_2_group-5-8_data")
    print("complete")
    
Main()