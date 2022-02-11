import csv
import pandas as pd
import re

pathFramaData = "../frameDataScraper/frameData.csv"


#due to uneven column sizes pd.read_csv has issues loading in the data
# frameData = pd.read_csv(pathFramaData,header=None)

#so instead I will read each row in to a pandas series then concatenate the series into a dataframe where NaNs will be autoinserted into the uneven columns
series_list = []
with open(pathFramaData, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
       series_list.append(pd.Series(row))

df = pd.DataFrame(series_list)
df.rename({0:"Character"},axis=1,inplace=True)
df.set_index("Character",inplace=True)
print(df.head(1))


# Now that the dataframe is created moves can be read in and formatted/ feature engineered to be more usable for a machine learning applications.
# I am planning to use a recommendation/ranking system based on a persons preferences
# will do a simple content based filtering system 
# each character will be treated as a user and the features that are engineered for each character will be the items


#user inputs will be survivability {low,medium,high}, difficulty{0,1,2,3}, speed{0,1,2},do_you want to learn combos{0,1,2},floaty{0,1},combo_food{0,1},fast moves{0,1,2,3},recovery{0,1,2,3},high_damage {0,1,2,3}
#features that will be engineered for the smash ultimate characters will be weight_class {0,1,2,3} ,average_frame_data_grounded, average_frame_data_aerial, average_frame_data_smashes,average_damage,move_laggyness,speed, fast_faller {0,1,2},combo_based{0,1},combo_food{0,1}


names = []
move_frame_data = []

for index, row in df.iterrows():
    names.append(index)
    for move in row:
        if type(move) != float:
            moveDict = eval(move)
            # print(moveDict)
            frameData = re.split('- |, |/',moveDict['startup'].replace(".",""))
            print(frameData)


