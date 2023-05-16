import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t, chi2
matplotlib.use('TkAgg')
def analyze_data_with_CI(data: list, confidence_level: float, nr_of_bins: int):
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
    plt.show()