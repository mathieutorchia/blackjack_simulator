import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path_combined_1 = "/Applications/Everything/Personal Projects/GIT/FirstRepo/combined_data.csv"
file_path_simplified_1 = "/Applications/Everything/Personal Projects/GIT/FirstRepo/simplified_data.csv"
file_path_combined_2 = "/Applications/Everything/Personal Projects/GIT/FirstRepo/combined_data_2.csv"
file_path_simplified_2 = "/Applications/Everything/Personal Projects/GIT/FirstRepo/simplified_data_2.csv"


df_total_1 = pd.read_csv(file_path_combined_1)
df_simplified_1 = pd.read_csv(file_path_simplified_1)
df_total_2 = pd.read_csv(file_path_combined_2)
df_simplified_2 = pd.read_csv(file_path_simplified_2)

line_chart = True
histogram_chart = True
smooth_chart = True

num_simulations_1 = df_total_1['simulation_number'].max()
num_meta_simulations_1 = df_total_1['meta_simulation_number'].max()

# Line Graph Chart
if line_chart:
    session_data = [group[1][['simulation_number', 'cumulative_money']] for group in
                    df_total_2.groupby('meta_simulation_number')]
    for session_data in session_data:
        plt.plot(session_data['simulation_number'], session_data['cumulative_money'])
    plt.style.use('ggplot')
    plt.xlabel('Number of Hands')
    plt.ylabel('Total Profit ($)')
    plt.title(f'Total Profit After {num_meta_simulations_1} Simulations')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Histogram Chart
if histogram_chart:
    plt.hist(df_simplified_2['money'], edgecolor="skyblue", cumulative=False, alpha=0.7)
    plt.style.use('ggplot')
    plt.xlabel("Average Profit per $10 Hand")
    plt.ylabel("Frequency")
    plt.title(
        f"Distribution of Profit per Hand After {num_meta_simulations_1} Simulations")
    plt.axvline(df_simplified_2['money'].mean(), color="red", linestyle="--", linewidth=2, label="Mean Profit per Hand")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(-4, 4)
    plt.show()

# Smooth Histogram Chart
if smooth_chart:
    sns.kdeplot(df_simplified_2['money'], fill=True, color="skyblue")
    plt.style.use('ggplot')
    plt.xlabel("Average Profit per $10 Hand")
    plt.ylabel("Density")
    plt.title(
        f"Distribution of Profit per Hand After {num_meta_simulations_1} Simulations")
    plt.axvline(df_simplified_2['money'].mean(), color="red", linestyle="--", linewidth=2, label="Mean Profit per Hand")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(-4, 4)
    plt.show()


# print(df_total_1.describe())
# print(df_total_1['result'].value_counts())
#
# print((df_simplified_1['money'] > 0).sum())
# print((df_simplified_1['money'] < 0).sum())
# print((df_simplified_1['money'] == 0).sum())
#
# count_profitable = (df_simplified_1['money'] > 0).sum()
# count_loss = (df_simplified_1['money'] < 0).sum()
#
# average_profit = df_simplified_1.loc[df_simplified_1['money'] > 0, 'money'].mean()
# average_loss = df_simplified_1.loc[df_simplified_1['money'] < 0, 'money'].mean()
#
# print(f'There are {count_profitable} people who made a profit, with an average profit of {average_profit}.')
# print(f'There are {count_loss} people who booked a loss, with an average loss of {average_loss}.')
#
# print(df_simplified_1['money'].mean())
#
#
# average_win =  df_total_1.loc[df_total_1['result'] == "W", 'money'].mean()
# average_loss = df_total_1.loc[df_total_1['result'] == "L", 'money'].mean()
# print(average_win)
# print(average_loss)

print(df_total_2.describe())
print(df_total_2['result'].value_counts())

print((df_simplified_2['money'] > 0).sum())
print((df_simplified_2['money'] < 0).sum())
print((df_simplified_2['money'] == 0).sum())

count_profitable = (df_simplified_2['money'] > 0).sum()
count_loss = (df_simplified_2['money'] < 0).sum()

average_profit = df_simplified_2.loc[df_simplified_2['money'] > 0, 'money'].mean()
average_loss = df_simplified_2.loc[df_simplified_2['money'] < 0, 'money'].mean()

print(f'There are {count_profitable} people who made a profit, with an average profit of {average_profit}.')
print(f'There are {count_loss} people who booked a loss, with an average loss of {average_loss}.')

print(df_simplified_2['money'].mean())


average_win =  df_total_2.loc[df_total_2['result'] == "W", 'money'].mean()
average_loss = df_total_2.loc[df_total_2['result'] == "L", 'money'].mean()
print(average_win)
print(average_loss)