import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm, t, chi2
matplotlib.use('TkAgg')
def analyze_data_with_CI(data: list, confidence_level: float, nr_of_bins: int, show_plot: bool):
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    sample_variance = np.var(data, ddof=1)
    sample_size = len(data)
    standard_error = sample_std / np.sqrt(sample_size)

    # Calculate the t-value for the given confidence level and degrees of freedom
    degrees_of_freedom = sample_size - 1
    t_value = t.ppf((1 + confidence_level) / 2, degrees_of_freedom)
    margin_of_error = t_value * standard_error

    # Calculate the lower and upper bounds of the confidence interval for the mean
    lower_bound_mean = sample_mean - margin_of_error
    upper_bound_mean = sample_mean + margin_of_error

    # Calculate the chi-squared values for the confidence interval
    chi2_lower = chi2.ppf((1 - confidence_level) / 2, degrees_of_freedom)
    chi2_upper = chi2.ppf((1 + confidence_level) / 2, degrees_of_freedom)

    # Calculate the confidence interval for the variance
    lower_bound_variance = (degrees_of_freedom * sample_variance) / chi2_upper
    upper_bound_variance = (degrees_of_freedom * sample_variance) / chi2_lower

    # Define the x-axis range
    x_min = sample_mean - 4 * sample_std
    x_max = sample_mean + 4 * sample_std
    x_step = 0.1
    x = np.arange(x_min, x_max, x_step)

    # Calculate the normal distribution using the sample mean and standard deviation
    pdf = norm.pdf(x, loc=sample_mean, scale=sample_std)

    plt.hist(data, bins=nr_of_bins, density=True)
    plt.plot(x, pdf, color='red', label='Normal Distribution')
    plt.legend()

    # Set the axis labels
    plt.xlabel('Amount')
    plt.ylabel('Density')

    # Print the confidence interval
    print(f"Confidence Interval for the Mean ({confidence_level * 100:}%): [{lower_bound_mean:.2f},"
          f" {upper_bound_mean:.2f}]")
    # Print the confidence interval
    print( f"Confidence Interval for Variance ({confidence_level * 100:}%): [{lower_bound_variance:.2f},"
           f" {upper_bound_variance:.2f}]")

    print(f"Sample Mean: {sample_mean:.2f}")

    print(f"Sample Standard Deviation: {sample_std:.2f}")

    print(f"Sample Variance: {sample_variance:.2f}")
    # Show the plot
    if show_plot:
        plt.show()
def t_test(data: list, null_hypothesis_mean: float, alternative: str, significance_level: float) -> float:
    """
    Perform a t-test to evaluate the null hypothesis regarding the mean of a sample.

    Args:
        data (list): List of numeric values representing the sample data.
        null_hypothesis_mean (float): Expected mean value under the null hypothesis.
        alternative (str): Type of alternative hypothesis ('two-sided', 'less', or 'greater').
        significance_level (float): Significance level for the test.

    Returns:
        float: Calculated p-value for the test.

    Raises:
        ValueError: If the alternative is not one of 'two-sided', 'less', or 'greater'.
    """
    if len(data) < 2:
        raise ValueError("Insufficient data for t-test. The sample size should be at least 2.")
    if alternative not in ['two-sided', 'less', 'greater']:
        raise ValueError("Invalid alternative hypothesis. Should be 'two-sided', 'less', or 'greater'.")
    if not 0 < significance_level < 1:
        raise ValueError("Invalid significance level. Should be between 0 and 1 (exclusive).")

    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    sample_size = len(data)
    standard_error = sample_std / np.sqrt(sample_size)
    degrees_of_freedom = sample_size - 1
    t_statistic = (sample_mean - null_hypothesis_mean) / standard_error
    p_val:int
    if alternative == 'two-sided':
        p_val = 2 * t.cdf(-np.abs(t_statistic), df=degrees_of_freedom)
    elif alternative == 'less':
        p_val = t.cdf(t_statistic, df=degrees_of_freedom)
    else:  # alternative == 'greater'
        p_val = 1 - t.cdf(t_statistic, df=degrees_of_freedom)

    return p_val

def p_value(data: list, test_statistic: float, alternative: str, distribution: str) -> float:
    p = 0
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    sample_size = len(data)
    standard_error = sample_std / np.sqrt(sample_size)
    if distribution == 'normal':
        z = (test_statistic - sample_mean) / standard_error

        if alternative == 'two-sided':
            p = 2 * stats.norm.cdf(-np.abs(z))
        elif alternative == 'less':
            p = stats.norm.cdf(z)
        elif alternative == 'greater':
            p = 1 - stats.norm.cdf(z)
        else:
            raise ValueError("alternative not recognized\n"
                             "should be 'two-sided', 'less' or 'greater'")
    elif distribution == 't':
        t = (test_statistic - sample_mean) / standard_error

        if alternative == 'two-sided':
            p = 2 * stats.t.cdf(-np.abs(t), df=sample_size - 1)
        elif alternative == 'less':
            p = stats.t.cdf(t, df=sample_size - 1)
        elif alternative == 'greater':
            p = 1 - stats.t.cdf(t, df=sample_size - 1)
        else:
            raise ValueError("alternative not recognized\n"
                             "should be 'two-sided', 'less' or 'greater'")
    else:
        raise ValueError("distribution not recognized")

    return p
def sum_of_x_squared(data: list) -> float:
    return sum([x ** 2 for x in data])

def n_choose_k_combinations(n: int, k: int) -> int:
    return int(np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k)))

def n_choose_k_permutations(n: int, k: int) -> int:
    return int(np.math.factorial(n) / np.math.factorial(n - k))