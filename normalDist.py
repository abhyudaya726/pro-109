import statistics as st
import pandas as pd

file = pd.read_csv("data.csv")

scoreList = file["math_score"].tolist()
scoreMean = st.mean(scoreList)
scoreStdev = st.stdev(scoreList)

stdev_1_start,stdev_1_end = scoreMean+scoreStdev,scoreMean-scoreStdev
stdev_1_list = [result for result in scoreList if result<stdev_1_start and result>stdev_1_end]
stdev_1_precentage = len(stdev_1_list)/len(scoreList)*100
print(stdev_1_precentage)

stdev_2_start,stdev_2_end = scoreMean+scoreStdev*2,scoreMean-scoreStdev*2
stdev_2_list = [result for result in scoreList if result<stdev_2_start and result>stdev_2_end]
stdev_2_precentage = len(stdev_2_list)/len(scoreList)*100
print(stdev_2_precentage)

stdev_3_start,stdev_3_end = scoreMean+scoreStdev*3,scoreMean-scoreStdev*3
stdev_3_list = [result for result in scoreList if result<stdev_3_start and result>stdev_3_end]
stdev_3_precentage = len(stdev_3_list)/len(scoreList)*100
print(stdev_3_precentage)