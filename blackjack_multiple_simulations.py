# blackjack_multiple_simulations.py
import pandas as pd
from blackjack_simulation import run_blackjack_simulation
import matplotlib.pyplot as plt
import seaborn as sns

line_chart = True
histogram_chart = True
smooth_chart = True

def run_simulations(num_simulations, num_meta_simulations):
    all_data = []

    for meta_sim in range(num_meta_simulations):
        for sim in range(num_simulations):
            df = run_blackjack_simulation()
            df['simulation_number'] = sim + 1  # Add a column for the simulation number
            df['meta_simulation_number'] = meta_sim + 1  # Add a column for the meta-simulation number

            # Reorder columns to make 'meta_simulation_number' and 'simulation_number' the first columns
            cols = df.columns.tolist()
            cols = ['meta_simulation_number', 'simulation_number'] + [col for col in cols if
                                                                      col not in ['meta_simulation_number',
                                                                                  'simulation_number']]
            df = df[cols]

            all_data.append(df)

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


if __name__ == "__main__":
    num_simulations = 10
    num_meta_simulations = 10
    combined_df = run_simulations(num_simulations, num_meta_simulations)
    combined_df['cumulative_money'] = combined_df.groupby('meta_simulation_number')['money'].cumsum()

    df_simplified = combined_df.groupby('meta_simulation_number')['money'].mean().reset_index()

    # # Specify the file names
    # combined_csv_file = 'combined_data_2.csv'
    # simplified_csv_file = 'simplified_data_2.csv'
    #
    # # Save the DataFrames to CSV files
    # combined_df.to_csv(combined_csv_file, index=False)
    # df_simplified.to_csv(simplified_csv_file, index=False)

    # Line Graph Chart
    if line_chart:
        session_data = [group[1][['simulation_number', 'cumulative_money']] for group in combined_df.groupby('meta_simulation_number')]
        for session_data in session_data:
            plt.plot(session_data['simulation_number'], session_data['cumulative_money'])
        plt.style.use('ggplot')
        plt.xlabel('Number of Hands')
        plt.ylabel('Total Profit ($)')
        plt.title(f'Total Profit After {num_simulations} Hand, for {num_meta_simulations} Simulations.')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()

    # Histogram Chart
    if histogram_chart:
        plt.hist(df_simplified['money'], edgecolor="skyblue", cumulative=False, alpha=0.7)
        plt.style.use('ggplot')
        plt.xlabel("Average Profit per $10 Hand")
        plt.ylabel("Frequency")
        plt.title(f"Distribution of Profit per Hand Over {num_simulations} Hands, Across {num_meta_simulations} Simulations")
        plt.axvline(df_simplified['money'].mean(), color="red", linestyle="--", linewidth=2, label="Mean Profit per Hand")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.xlim(-4, 4)
        plt.show()

    # Smooth Histogram Chart
    if smooth_chart:
        sns.kdeplot(df_simplified['money'], fill=True, color="skyblue")
        plt.style.use('ggplot')
        plt.xlabel("Average Profit per $10 Hand")
        plt.ylabel("Density")
        plt.title(f"Distribution of Profit per Hand Over {num_simulations} Hands, Across {num_meta_simulations} Simulations")
        plt.axvline(df_simplified['money'].mean(), color="red", linestyle="--", linewidth=2, label="Mean Profit per Hand")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.xlim(-4, 4)
        plt.show()


