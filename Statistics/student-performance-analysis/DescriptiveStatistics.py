import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

# Display basic info and statistics
def explore_data(df):
    print("\n--- Dataset Info ---")
    print(df.info())
    print("\n--- Summary Statistics ---")
    print(df.describe())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

# Descriptive statistics
def descriptive_stats(df):
    print("\n--- Descriptive Statistics ---")
    print("Math Mean:", df['math score'].mean())
    print("Reading Median:", df['reading score'].median())
    print("Writing Mode:", df['writing score'].mode()[0])

# Plot distributions
def plot_distributions(df):
    sns.histplot(df['math score'], kde=True)
    plt.title('Math Score Distribution')
    plt.xlabel('Math Score')
    plt.ylabel('Frequency')
    plt.show()

    sns.boxplot(x='gender', y='reading score', data=df)
    plt.title('Reading Score by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Reading Score')
    plt.show()

# Probability of high scores
def calculate_probability(df):
    high_scores = df[
        (df['math score'] > 80) &
        (df['reading score'] > 80) &
        (df['writing score'] > 80)
    ]
    prob = len(high_scores) / len(df)
    print("\nP(score > 80 in all subjects):", round(prob, 4))

# Correlation matrix heatmap
def plot_correlation_matrix(df):
    corr = df[['math score', 'reading score', 'writing score']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

# Main execution
def main():
    df = load_data('StudentsPerformance.csv')
    explore_data(df)
    descriptive_stats(df)
    plot_distributions(df)
    calculate_probability(df)
    plot_correlation_matrix(df)

if __name__ == "__main__":
    main()
0