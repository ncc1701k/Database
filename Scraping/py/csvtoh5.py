
import pandas as pd


# Open the csv file as pandas data frame
playerxefg = pd.read_csv('xefg_by_player.csv', sep=',', low_memory=False)

# Write the resulting data frame to the hdf5 file
playerxefg.to_hdf('/media/sf_GitHub/Database/Scraping/py/playerxefg.h5', 'playerxefg', format='table', complevel=9,
            complib='lzo')

teamxefg = pd.read_csv('xefg_by_team.csv', sep=',', low_memory=False)

# Write the resulting data frame to the hdf5 file
playerxefg.to_hdf('/media/sf_GitHub/Database/Scraping/py/teamxefg.h5', 'teamxefg', format='table', complevel=9,
            complib='lzo')