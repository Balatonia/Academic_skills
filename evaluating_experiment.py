import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

def add_mean_value_to_df(dataframe):
    dataframe= dataframe.assign(average = dataframe.mean(axis=1))
    return dataframe



df = pd.read_csv("/Users/ferry/Desktop/Coding/ergebnisse_modifiziert.csv")

#select the relevant two questions for each condition by filtering the columns using regex
df_dat_test = df.filter(regex=("test_dat_*"))
df_acc_test= df.filter(regex=("test_acc_*"))
df_nom_test= df.filter(regex=("test_nom_*"))
df_prep_test= df.filter(regex=("test_prep_*"))
df_dat_control = df.filter(regex=("control_dat_*"))
df_acc_control = df.filter(regex=("control_acc_*"))
df_nom_control = df.filter(regex=("control_nom_*"))
df_prep_control = df.filter(regex=("control_prep_*"))
df_filler_gr = df.filter(regex=("filler_gr_*"))
df_filler_marked = df.filter(regex=("filler_marked_*"))
df_filler_ungr = df.filter(regex=("filler_ungr_*"))

#list of all subframes
all_frames= [df_dat_test, df_acc_test, df_nom_test, df_prep_test, df_dat_control, df_acc_control, df_nom_control, df_prep_control, df_filler_gr, df_filler_marked, df_filler_ungr]
all_frames_with_means = [add_mean_value_to_df(frame) for frame in all_frames]

#this frame now contains the average of test datives and control datives
compare_two_dative_conditions = pd.concat([all_frames_with_means[0]["average"], all_frames_with_means[4]["average"]], axis=1, keys=["Test", "Control"])
#check out the basic stats using .describe
print(compare_two_dative_conditions.describe())

#compare both conditions visually
plt.hist(compare_two_dative_conditions)
plt.title("Test condition vs control condition")
plt.show()

