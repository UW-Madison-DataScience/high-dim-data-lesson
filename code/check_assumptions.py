# statsmodels
import statsmodels.api as sm
import statsmodels.stats.api as sms
# normal errors
import statsmodels.graphics.gofplots as smg # qqplot
# independent errors
from statsmodels.stats.stattools import durbin_watson
# VIF score / multicollinearity
from statsmodels.stats.outliers_influence import variance_inflation_factor

# essentials
import numpy as np
import pandas as pd
from pandas import Series
from scipy import stats
# plotting
import seaborn as sns
import matplotlib.pyplot as plt



def normal_resid_test(resids: Series, threshold_p_value: float = 0.05) -> plt.Figure:
    """
    Perform tests and visualizations to assess the normality of residuals.
    
    Args:
        resids (Series): Series of residuals.

    Returns:
        plt.Figure: A figure containing histograms, QQ-plots, and test results.
    """
    print('\n==========================')
    print('VERIFYING NORMAL ERRORS...')
    
    # Extract the residuals and calculate median — should lie close to 0 if it is a normal distribution
    print('Median of residuals:', np.median(resids))
    
    # Set up square figure with 1x2 subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    # plot histogram
    ax1.hist(resids)
    ax1.set_title('Histogram of Residuals')
    
    # measure skew
    skewness = resids.skew() 
    print('Skewness of resids (+/- 0.5 is bad):', skewness)

    # Plot the QQ-plot of residuals
    smg.qqplot(resids, line='s', ax=ax2)
    ax2.set_xlabel('Theoretical Quantiles')
    ax2.set_ylabel('Sample Quantiles')
    ax2.set_title('QQ-Plot of Residuals')

    # Hypothesis tests
    shapiro_stat, shapiro_p = stats.shapiro(resids)
    print(f"Shapiro-Wilk test: statistic={shapiro_stat:.4f}, p-value={shapiro_p:.10f}")
    shapiro_pass = shapiro_p > threshold_p_value
    print("Shapiro-Wilk test passes:", shapiro_pass)
    
    ks_stat, ks_p = stats.kstest(resids, 'norm')
    print(f"Kolmogorov-Smirnov test: statistic={ks_stat:.4f}, p-value={ks_p:.10f}")
    ks_pass = ks_p > threshold_p_value
    print("Kolmogorov-Smirnov test passes:", ks_pass)
    
    # Adjust layout to make figures square
    plt.tight_layout()
    
    plt.show()
    
    return fig


def plot_corr_matrix(corr_matrix: pd.DataFrame) -> plt.figure:
    # Create a heatmap with variable labels
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
                square=True, cbar=True, linewidths=0.5)

    # Set plot labels
    plt.title("Correlation Matrix")
    plt.xlabel("Predictor Variables")
    plt.ylabel("Predictor Variables")

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha="right")

    # Show the plot
    # plt.tight_layout()
    return fig


def calc_print_VIF(X):
    # Calculate VIF for each predictor in X
    vif = pd.DataFrame()
    vif["Variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    # Display the VIF values
    print(vif)
    
def multicollinearity_test(X: pd.DataFrame):
    print('\n==========================')
    print('VERIFYING MULTICOLLINEARITY...')
    
    # remove y-intercept column, if present
    X = X[X.columns.difference(['const'])]
    
    # caculate VIF
    calc_print_VIF(X)
    corr_matrix = X.corr()
    
    # plot results
    fig = plot_corr_matrix(corr_matrix)
    # fig.suptitle('Multicollinearity', y=1.05)

    # plt.savefig('..//fig//regression//assumptions//corrMat_multicollinearity2.png', bbox_inches='tight', dpi=300, facecolor='white');
    plt.show()
    return fig
    
    
def plot_pred_v_resid(y_pred, resids, ax):
    
    sns.regplot(x=y_pred, y=resids, lowess=True, ax=ax, line_kws={'color': 'red'})
    ax.axhline(0, color='blue', linestyle='dashed')  # Add a horizontal line at y=0

    # ax2.set_title('Residuals vs Fitted', fontsize=16)
    ax.set(xlabel='Predicted', ylabel='Residuals')
    ax.set_aspect('equal')
    return ax


import statsmodels.api as sm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from regression_predict_sklearn import plot_predictions

def homoscedasticity_linearity_test(trained_model: sm.regression.linear_model.RegressionResultsWrapper, 
                                    y: pd.Series, y_pred: pd.Series, y_log_scaled: bool, plot_raw: bool,
                                    threshold_p_value: float = 0.05):
    '''
    Function for testing the homoscedasticity of residuals in a linear regression model.
    It plots residuals and standardized residuals vs. fitted values and runs Breusch-Pagan and Goldfeld-Quandt tests.
    
    Args:
    * model - fitted OLS model from statsmodels
    * threshold_p_value - Threshold p-value for determining homoscedasticity (default: 0.05)
    '''
    print('\n=======================================')
    print('VERIFYING LINEARITY & HOMOSCEDASTICITY...')

    sns.set_style('darkgrid')
    sns.mpl.rcParams['figure.figsize'] = (15.0, 9.0)
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,10))#, sharex=True, sharey=True)
    # fig.suptitle('Linearity & Homoscedasticiy')

    # Predictions vs actual
    ax1 = plot_predictions(ax1, y, y_pred, y_log_scaled=y_log_scaled, plot_raw=plot_raw, keep_tick_labels=True)
    
    # Predictions vs residuals
    resids = y_pred - y
        
    ax2 = plot_pred_v_resid(y_pred, resids, ax2)
    
    # GQ test
    gq_test = pd.DataFrame(sms.het_goldfeldquandt(resids, trained_model.model.exog)[:-1],
                           columns=['value'],
                           index=['F statistic', 'p-value'])

    print('\n Goldfeld-Quandt test (homoscedasticity) ----')
    print(gq_test)
    
    # Check if p-value is below the threshold
    if gq_test.loc['p-value', 'value'] < threshold_p_value:
        print("Homoscedasticity test: Does not pass (heteroscedasticity is present)")
    else:
        print("Homoscedasticity test: Passes (homoscedasticity is assumed)")
    
    print('\n Residuals plots ----')
    plt.show()
    return fig


import matplotlib.pyplot as plt
import statsmodels.stats.stattools as smt
from pandas import Series

def independent_resid_test(y_pred: Series, resids: Series, include_plot: bool = True) -> plt.Figure:
    """
    Perform tests and visualizations to assess the independence of residuals.
    
    Args:
        y_pred (Series): Series of predicted values.
        resids (Series): Series of residuals.
        include_plot (bool, optional): Whether to include the plot or not. Defaults to True.

    Returns:
        plt.Figure: A figure containing the plot and test results.
    """
    print('\n==========================')
    print('VERIFYING INDEPENDENT ERRORS...')

    durbin_watson_statistic = smt.durbin_watson(resids)
    print(f"Durbin-Watson test statistic: {durbin_watson_statistic}")
    
    if durbin_watson_statistic > 1.5 and durbin_watson_statistic < 2.5:
        print("Durbin-Watson test statistic is within the expected range (1.5 to 2.5) for no significant autocorrelation.")
    else:
        print("Durbin-Watson test statistic suggests potential autocorrelation.")
    
    if include_plot:
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))
        ax = plot_pred_v_resid(y_pred, resids, ax)
        # Adjust layout to make figure square
        plt.tight_layout()
        plt.show()
    else:
        fig = None
        

    return fig


def eval_regression_assumptions(trained_model, X, y, y_pred, y_log_scaled, plot_raw, threshold_p_value):
    multicollinearity_test(X)
    
    homoscedasticity_linearity_test(trained_model=trained_model, y=y, y_pred=y_pred, 
                                    y_log_scaled=y_log_scaled, plot_raw=plot_raw, 
                                    threshold_p_value=threshold_p_value) 
    resids = y - y_pred
    normal_resid_test(resids, threshold_p_value) 
    independent_resid_test(y_pred, resids, include_plot=False)
    
    return None

