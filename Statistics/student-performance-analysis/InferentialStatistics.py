from scipy import stats

# Hypothesis Testing: Female vs Male Reading Scores
def test_gender_reading_scores(df):
    # H₀: There is no significant difference in average reading scores between female and male students.
    # H₁: There is a significant difference in average reading scores between female and male students.

    female_scores = df[df['gender'] == 'female']['reading score']
    male_scores = df[df['gender'] == 'male']['reading score']

    t_stat, p_val = stats.ttest_ind(female_scores, male_scores)

    print("\n--- Hypothesis Testing: Female vs Male Reading Scores ---")
    print("H₀: μ_female = μ_male")
    print("H₁: μ_female ≠ μ_male")
    print("T-statistic:", round(t_stat, 4))
    print("P-value:", round(p_val, 4))

    if p_val < 0.05:
        print("✅ Reject the null hypothesis: Significant difference in reading scores.")
    else:
        print("❌ Fail to reject the null hypothesis: No significant difference.")

# Call this function after loading your DataFrame
# test_gender_reading_scores(df)