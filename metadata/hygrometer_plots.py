#%%
# Hygrometer_plots

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob as glob
import datetime

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# import data
file_names = glob.glob('*.csv')


df = pd.read_csv(file_names[1], skiprows=7, sep='\s*,', skipinitialspace=True, skipfooter=1, names=['rh1','temp1','rh2','temp2','time','date'])
#leading spaces after first row of data cause import issues. Skipping header + initial row of data appears to have fixed this issue. 
# final row is just four spaces/ indent --> deleted with skipfooter=1

#df.info()
# First RH imported with '+' - need to remove
df=df.replace({'\x00':'','\+':''},regex=True) # delete leading null and +
df.rh1 = pd.to_numeric(df.rh1) # convert to float

# Create new dataframe column with datetime format
df.loc[:,'datetime']= np.transpose([df.date + ' '+ df.time]) # combine date and time
df.datetime = pd.to_datetime(df.datetime) # convert to datetime format (NOTE: seems slow)

# delete 2012 data 
# hygrometer defaults to year 2012 before date is set, removing this data since it is not useful
datecut = datetime.datetime.strptime('01-01-2013 00:00:00','%m-%d-%Y %H:%M:%S')
k = df.datetime > datecut
df = df[k]

#%% Plotting

# plot hygrometer data 
def plot_hygrom(df):
    cmap = plt.cm.get_cmap('tab10') # get colormap
    # Internal channel
    fig, ax1 = plt.subplots()
    ax1.plot(df.datetime, df.temp1, color=cmap(0), linewidth=0.7)
    ax1.set_xlabel('Date')
    plt.xticks(rotation=45, ha='right')
    ax1.set_ylabel('Int Temperature (C)', color=cmap(0))
    ax2=ax1.twinx()
    ax2.plot(df.datetime, df.rh1, color=cmap(1), linewidth=0.7)
    ax2.set_ylabel('Int Relative Humidity (%)', color=cmap(1))
    plt.xticks(rotation=45, ha='right')
    #plt.show()

    # External channel
    fig, ax3 = plt.subplots()
    #ax = plt.gca()
    ax3.plot(df.datetime, df.temp2, color=cmap(2), linewidth=0.7)
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Ext Temperature (C)', color=cmap(2))
    ax4=ax3.twinx()
    ax4.plot(df.datetime, df.rh2, color=cmap(4), linewidth=0.7)
    ax4.set_ylabel('Ext Relative Humidity (%)', color=cmap(4))
    plt.xticks(rotation=45, ha='right') # NOT WORKING ?

    plt.show()

plot_hygrom(df)


#%%
# visualize in Jupyter notebook
# Slider widgets to change x and y axis



# save data to json (?)
    #check if json file exists
        # check for new data
        # add new data and save
    #else
        # create json file and save

# Plot for each lab



# %%

# %%
