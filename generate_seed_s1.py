"""
Question generation and validation script for University of Mumbai T.E. AI&DS (Sem V).
Generates high quality MCQs module by module with:
- id, subject, subject_code, module, module_number, topic
- question, option_a, option_b, option_c, option_d, answer, explanation
- difficulty (easy 25%, medium 50%, hard 25%)
- question_type (conceptual, application, scenario, numerical, algorithm_tracing, comparison, output_based, code_debugging, architecture, case_study, core, self_learning)
"""

import json
import random
from syllabus_data import SYLLABUS_STRUCTURE

def generate_all_questions():
    questions = []
    q_id = 1

    # Subject 1: Statistics for Machine Learning and Data Science (2015111)
    s1_code = "2015111"
    s1_name = "Statistics for Machine Learning and Data Science"
    
    # S1 M1: Statistical Foundations, Covariance, and Sampling
    m1_name = "Module I - Statistical Foundations, Covariance, and Sampling"
    s1_m1_q = [
        {
            "topic": "Types of data",
            "question": "A dataset contains features: 'Customer ID', 'Credit Rating (AAA, AA, A)', 'Temperature in Celsius', and 'Transaction Amount ($)'. What is the correct classification for 'Credit Rating' and 'Temperature in Celsius' respectively?",
            "option_a": "Ordinal data and Interval data",
            "option_b": "Nominal data and Ratio data",
            "option_c": "Ordinal data and Ratio data",
            "option_d": "Nominal data and Interval data",
            "answer": "A",
            "explanation": "Credit rating has a clear ranking order without fixed numeric differences (Ordinal), while Celsius temperature has meaningful differences but an arbitrary zero point (Interval).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Skewness",
            "question": "For a unimodal salary distribution where Mean = $85,000, Median = $62,000, and Mode = $48,000, what is the nature of the skewness and what does it imply about the tail?",
            "option_a": "Positively skewed (right-tailed) with extreme high salaries pulling the mean upward",
            "option_b": "Negatively skewed (left-tailed) with extreme low salaries pulling the mean downward",
            "option_c": "Symmetric with zero skewness",
            "option_d": "Mesokurtic with balanced tails",
            "answer": "A",
            "explanation": "When Mean > Median > Mode, the distribution has positive skewness with a long right tail caused by high outlier values.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Kurtosis",
            "question": "In financial risk modeling, an asset return distribution exhibits heavy tails with excess kurtosis > 0. Which distribution type best describes this behavior compared to a normal distribution?",
            "option_a": "Leptokurtic",
            "option_b": "Platykurtic",
            "option_c": "Mesokurtic",
            "option_d": "Uniform",
            "answer": "A",
            "explanation": "Leptokurtic distributions have positive excess kurtosis (> 0), characterized by heavy tails and a higher probability of extreme events (fat tails).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Covariance",
            "question": "Given two random variables X and Y where Var(X) = 16, Var(Y) = 25, and Cov(X, Y) = -10. What is Pearson's correlation coefficient r(X, Y)?",
            "option_a": "-0.50",
            "option_b": "-0.25",
            "option_c": "0.50",
            "option_d": "-0.40",
            "answer": "A",
            "explanation": "r = Cov(X,Y) / (Std(X) * Std(Y)) = -10 / (sqrt(16) * sqrt(25)) = -10 / (4 * 5) = -10 / 20 = -0.50.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Cosine distance",
            "question": "Vector u = [1, 1, 0] and vector v = [0, 1, 1]. What is the Cosine Similarity and Cosine Distance between vectors u and v?",
            "option_a": "Cosine Similarity = 0.50, Cosine Distance = 0.50",
            "option_b": "Cosine Similarity = 0.707, Cosine Distance = 0.293",
            "option_c": "Cosine Similarity = 0.25, Cosine Distance = 0.75",
            "option_d": "Cosine Similarity = 0.866, Cosine Distance = 0.134",
            "answer": "A",
            "explanation": "Dot product = (1*0 + 1*1 + 0*1) = 1. ||u|| = sqrt(2), ||v|| = sqrt(2). Cosine similarity = 1 / (sqrt(2)*sqrt(2)) = 1/2 = 0.50. Cosine distance = 1 - 0.50 = 0.50.",
            "difficulty": "hard",
            "question_type": "numerical"
        },
        {
            "topic": "Stratified sampling",
            "question": "A fraud detection dataset has 99,000 legitimate transactions and 1,000 fraudulent transactions. To ensure representative validation splits across both classes, which sampling technique must be employed?",
            "option_a": "Stratified random sampling based on the class label",
            "option_b": "Cluster sampling using transaction timestamps",
            "option_c": "Simple random sampling without replacement",
            "option_d": "Systematic sampling taking every 100th record",
            "answer": "A",
            "explanation": "Stratified sampling divides the population into strata (classes) and samples proportionally from each, preserving the critical minority class proportion.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Central Limit Theorem",
            "question": "According to the Central Limit Theorem (CLT), regardless of the underlying population distribution (provided it has finite mean μ and variance σ²), what happens to the sampling distribution of the sample mean as sample size n increases?",
            "option_a": "It approaches a normal distribution with mean μ and variance σ²/n",
            "option_b": "It approaches a uniform distribution between 0 and 1",
            "option_c": "It converges to the exact shape of the original non-normal population",
            "option_d": "Its variance increases proportionally to n * σ²",
            "answer": "A",
            "explanation": "CLT states that the sampling distribution of the mean approaches N(μ, σ²/n) as n becomes sufficiently large (typically n >= 30).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Outlier treatment",
            "question": "A feature has Q1 = 30 and Q3 = 70. Under Tukey's standard Interquartile Range (IQR) rule, what is the boundary threshold for identifying outlier values?",
            "option_a": "Values < -30 or Values > 130",
            "option_b": "Values < 10 or Values > 90",
            "option_c": "Values < 0 or Values > 140",
            "option_d": "Values < -10 or Values > 110",
            "answer": "A",
            "explanation": "IQR = Q3 - Q1 = 70 - 30 = 40. Lower bound = Q1 - 1.5*IQR = 30 - 1.5*(40) = 30 - 60 = -30. Upper bound = Q3 + 1.5*IQR = 70 + 60 = 130.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Normalization",
            "question": "When comparing Min-Max Scaling and Z-score Standardization on a feature with extreme positive outliers, how do the methods behave?",
            "option_a": "Min-Max scaling squashes non-outlier data into a very narrow interval, whereas Z-score retains relative variance but has no bounded range",
            "option_b": "Min-Max scaling eliminates all outlier influence completely",
            "option_c": "Z-score forces all values strictly into the interval [0, 1]",
            "option_d": "Both methods are completely invariant to extreme outliers",
            "answer": "A",
            "explanation": "Min-Max scales data to [0,1] using min and max, so an extreme outlier causes inliers to compress into a tiny band. Z-score standardizes to mean=0, std=1 without bounded clipping.",
            "difficulty": "hard",
            "question_type": "comparison"
        },
        {
            "topic": "Boxplots",
            "question": "In an exploratory data analysis workflow, an engineer observes that the median line inside the boxplot is positioned near the bottom edge of the box and the upper whisker is twice as long as the lower whisker. What does this reveal?",
            "option_a": "The feature distribution is right-skewed (positively skewed)",
            "option_b": "The feature distribution is perfectly symmetrical",
            "option_c": "The feature distribution is left-skewed (negatively skewed)",
            "option_d": "The feature has uniform density throughout the range",
            "answer": "A",
            "explanation": "A median closer to Q1 (bottom of the box) with an extended upper whisker indicates a concentration of data at lower values and a stretched right tail (positive skew).",
            "difficulty": "medium",
            "question_type": "application"
        }
    ]
    for q in s1_m1_q:
        q.update({"id": q_id, "subject": s1_name, "subject_code": s1_code, "module": m1_name, "module_number": 1})
        questions.append(q)
        q_id += 1

    # S1 M2: Statistical Inference, Estimation & Resampling
    m2_name = "Module II - Statistical Inference, Estimation & Resampling"
    s1_m2_q = [
        {
            "topic": "Maximum Likelihood Estimation",
            "question": "In Maximum Likelihood Estimation (MLE) for n independent and identically distributed Bernoulli trials with parameter p, what is the analytical estimator hat(p)?",
            "option_a": "hat(p) = (1/n) * sum(x_i), which is the sample mean",
            "option_b": "hat(p) = sum(x_i) / (n - 1)",
            "option_c": "hat(p) = max(x_i) - min(x_i)",
            "option_d": "hat(p) = sqrt((1/n) * sum(x_i^2))",
            "answer": "A",
            "explanation": "Maximizing the log-likelihood L(p) = sum(x_i)ln(p) + (n - sum(x_i))ln(1-p) yields dL/dp = 0 => hat(p) = sum(x_i)/n, the sample proportion.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "t-test",
            "question": "A data science team evaluates whether a new caching algorithm reduces server response time. The sample size is n = 18, the population variance is unknown, and the response times are normally distributed. Which hypothesis testing procedure is appropriate?",
            "option_a": "One-sample Student's t-test with 17 degrees of freedom",
            "option_b": "Standard two-tailed z-test using known variance",
            "option_c": "Chi-Square goodness of fit test",
            "option_d": "One-way ANOVA with 18 groups",
            "answer": "A",
            "explanation": "When the sample size is small (n < 30) and the population standard deviation σ is unknown, Student's t-test with (n - 1) = 17 degrees of freedom is required.",
            "difficulty": "easy",
            "question_type": "scenario"
        },
        {
            "topic": "ANOVA",
            "question": "An AI researcher is comparing the classification accuracy across 4 distinct deep learning architectures on the same benchmark. To determine if at least one architecture has a statistically significant different mean without inflating Type I error, which test should be conducted first?",
            "option_a": "One-way Analysis of Variance (ANOVA) followed by Tukey's HSD post-hoc test",
            "option_b": "Six independent pairwise two-sample t-tests at alpha = 0.05",
            "option_c": "Mann-Whitney U test between the best and worst model",
            "option_d": "Chi-Square test of independence",
            "answer": "A",
            "explanation": "Running multiple pairwise t-tests causes family-wise error rate inflation (1 - (1-alpha)^k). One-way ANOVA tests the global omnibus hypothesis H0: mu1 = mu2 = mu3 = mu4 simultaneously.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Bootstrap confidence intervals",
            "question": "How does non-parametric Bootstrap estimation compute the 95% confidence interval for a non-standard metric like the median or F1-score?",
            "option_a": "By resampling the original dataset B times with replacement, computing the metric on each bootstrap sample, and taking the 2.5th and 97.5th percentiles",
            "option_b": "By fitting a Gaussian distribution to the sample and using +/- 1.96 * (s / sqrt(n))",
            "option_c": "By sampling without replacement repeatedly until half the dataset is exhausted",
            "option_d": "By generating synthetic observations from a uniform prior distribution",
            "answer": "A",
            "explanation": "Bootstrap resampling draws n samples with replacement B times from the empirical data, generating an empirical distribution of the estimator to find percentile confidence bounds.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Bonferroni correction",
            "question": "A bio-informatician conducts 100 simultaneous hypothesis tests at a global significance level of alpha = 0.05. Applying the standard Bonferroni correction, what adjusted p-value threshold must an individual test meet to reject its null hypothesis?",
            "option_a": "alpha_adj = 0.0005",
            "option_b": "alpha_adj = 0.005",
            "option_c": "alpha_adj = 0.05",
            "option_d": "alpha_adj = 0.00005",
            "answer": "A",
            "explanation": "Bonferroni correction sets the per-hypothesis significance threshold to alpha / m = 0.05 / 100 = 0.0005 to control the Family-Wise Error Rate (FWER).",
            "difficulty": "easy",
            "question_type": "numerical"
        },
        {
            "topic": "Mann-Whitney U",
            "question": "When testing for difference in central tendency between two independent groups where the data is severely skewed and fails the normality assumption of a two-sample t-test, which non-parametric test is the robust choice?",
            "option_a": "Mann-Whitney U test (Wilcoxon Rank-Sum test)",
            "option_b": "Kruskal-Wallis test for 3 or more groups",
            "option_c": "Paired Student's t-test",
            "option_d": "Pearson's Chi-square test",
            "answer": "A",
            "explanation": "The Mann-Whitney U test evaluates differences between two independent groups by comparing ranks of observations rather than parametric means.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Confidence intervals",
            "question": "A sample of size n = 100 drawn from a population with known standard deviation sigma = 20 gives a sample mean of 150. What is the 95% confidence interval for the population mean (using z_0.025 = 1.96)?",
            "option_a": "[146.08, 153.92]",
            "option_b": "[140.00, 160.00]",
            "option_c": "[148.04, 151.96]",
            "option_d": "[144.12, 155.88]",
            "answer": "A",
            "explanation": "Margin of error = z * (sigma / sqrt(n)) = 1.96 * (20 / sqrt(100)) = 1.96 * 2 = 3.92. CI = [150 - 3.92, 150 + 3.92] = [146.08, 153.92].",
            "difficulty": "easy",
            "question_type": "numerical"
        },
        {
            "topic": "Monte Carlo simulation",
            "question": "In high-dimensional quantitative risk analysis where analytical integration of posterior probabilities is intractable, why is Monte Carlo simulation preferred?",
            "option_a": "Because its convergence rate O(1/sqrt(N)) is independent of the dimensionality of the state space",
            "option_b": "Because it guarantees exact closed-form algebraic solutions in O(1) time",
            "option_c": "Because it converts non-convex loss surfaces into convex quadratic forms",
            "option_d": "Because it removes the requirement of random number pseudo-generators",
            "answer": "A",
            "explanation": "Monte Carlo integration converges at rate 1/sqrt(N) regardless of dimension d, avoiding the exponential 'curse of dimensionality' of grid-based numerical quadrature.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Permutation tests",
            "question": "What is the key mechanistic assumption under the null hypothesis when executing a two-sample permutation test?",
            "option_a": "The group labels are exchangeable under the null hypothesis that both samples originate from the same distribution",
            "option_b": "The population follows a standard normal Gaussian distribution with zero kurtosis",
            "option_c": "Observations in group 1 are linearly correlated with observations in group 2",
            "option_d": "The variances of the two groups must be known constants",
            "answer": "A",
            "explanation": "Under H0 (no treatment effect), any observation was equally likely to belong to either treatment group, so permuting group labels creates the exact null distribution.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "FDR",
            "question": "How does Benjamini-Hochberg False Discovery Rate (FDR) control differ fundamentally from the Family-Wise Error Rate (FWER) controlled by Bonferroni?",
            "option_a": "FDR controls the expected proportion of false positives among rejected nulls, offering greater statistical power than FWER in large-scale testing",
            "option_b": "FDR guarantees zero false positive discoveries under all conditions",
            "option_c": "FDR is strictly more conservative than Bonferroni correction",
            "option_d": "FDR can only be used when testing fewer than 5 hypotheses",
            "answer": "A",
            "explanation": "FDR = E[V / R] controls the false discovery proportion among discoveries, providing higher sensitivity than FWER which limits the probability of making even a single false positive.",
            "difficulty": "hard",
            "question_type": "comparison"
        }
    ]
    for q in s1_m2_q:
        q.update({"id": q_id, "subject": s1_name, "subject_code": s1_code, "module": m2_name, "module_number": 2})
        questions.append(q)
        q_id += 1

    # S1 M3: Regression Models, Regularization & Nonlinear Models
    m3_name = "Module III - Regression Models, Regularization & Nonlinear Models"
    s1_m3_q = [
        {
            "topic": "VIF",
            "question": "In a multiple linear regression model, a feature x_j has a coefficient of determination R_j^2 = 0.90 when regressed on all other predictors. What is its Variance Inflation Factor (VIF), and what does it indicate?",
            "option_a": "VIF = 10, indicating severe multicollinearity",
            "option_b": "VIF = 1.11, indicating negligible multicollinearity",
            "option_c": "VIF = 0.10, indicating perfect orthogonality",
            "option_d": "VIF = 5.0, indicating moderate multicollinearity",
            "answer": "A",
            "explanation": "VIF = 1 / (1 - R_j^2) = 1 / (1 - 0.90) = 1 / 0.10 = 10. A VIF >= 5-10 indicates high multicollinearity that inflates standard errors of regression coefficients.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Cook's distance",
            "question": "What is the primary purpose of computing Cook's Distance D_i for the i-th observation in ordinary least squares regression?",
            "option_a": "To measure the aggregate influence of observation i on all fitted values when it is omitted from the model",
            "option_b": "To test the homoscedasticity assumption across residual quantiles",
            "option_c": "To calculate the L1 penalty coefficient in Lasso regression",
            "option_d": "To determine the optimal polynomial degree for nonlinear curve fitting",
            "answer": "A",
            "explanation": "Cook's distance measures how much all fitted values y_hat change when the i-th data point is removed, combining both leverage and residual magnitude.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Lasso regression",
            "question": "Why does Lasso regression (L1 regularization) perform automatic feature selection by setting some coefficients strictly to zero, whereas Ridge regression (L2 regularization) only shrinks them towards zero?",
            "option_a": "The L1 diamond-shaped constraint region has sharp corners on coordinate axes where elliptical OLS loss contours are likely to hit first",
            "option_b": "Ridge regression uses an absolute value penalty that has non-differentiable gradients",
            "option_c": "Lasso regression minimizes the determinant of the covariance matrix directly",
            "option_d": "Ridge regression forces coefficients to be strictly positive numbers",
            "answer": "A",
            "explanation": "The geometric geometry of the L1 ball ||beta||_1 <= t has sharp vertices on the coordinate axes. The quadratic contour level sets of the sum of squared errors frequently intersect at these axes, forcing coefficients to exactly 0.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Elastic Net",
            "question": "In a genomics dataset where n = 200 samples and p = 10,000 features with groups of highly correlated genes, why is Elastic Net preferred over standard Lasso regression?",
            "option_a": "Elastic Net combines L1 and L2 penalties, selecting groups of correlated features together and overcoming Lasso's limitation of selecting at most n features",
            "option_b": "Elastic Net converts non-linear relationships into linear ones without hyperparameters",
            "option_c": "Elastic Net does not require any cross-validation for tuning lambda",
            "option_d": "Elastic Net eliminates the residual sum of squares component from the loss function",
            "answer": "A",
            "explanation": "Lasso can select at most n variables when p > n and tends to arbitrarily pick one from a group of correlated predictors. Elastic Net's L1+L2 hybrid penalty groups correlated predictors and handles p >> n effectively.",
            "difficulty": "hard",
            "question_type": "application"
        },
        {
            "topic": "Residual analysis",
            "question": "A plot of residuals versus fitted values for a linear regression model displays a distinct funnel or cone shape (increasing spread as fitted values grow). Which Gauss-Markov assumption is violated?",
            "option_a": "Homoscedasticity (constant error variance)",
            "option_b": "No multicollinearity among features",
            "option_c": "Linear independence of observation rows",
            "option_d": "Zero mean of error distribution",
            "answer": "A",
            "explanation": "A funnel-shaped residual plot indicates heteroscedasticity (non-constant variance of residuals across the range of fitted values), violating the homoscedasticity assumption.",
            "difficulty": "easy",
            "question_type": "scenario"
        },
        {
            "topic": "Simple linear regression",
            "question": "Given sample statistics: Var(x) = 4, Cov(x, y) = 6, bar(x) = 10, bar(y) = 25. What is the estimated slope beta_1 and intercept beta_0 for the simple linear regression line y = beta_0 + beta_1 * x?",
            "option_a": "beta_1 = 1.5, beta_0 = 10.0",
            "option_b": "beta_1 = 0.67, beta_0 = 18.3",
            "option_c": "beta_1 = 2.0, beta_0 = 5.0",
            "option_d": "beta_1 = 1.2, beta_0 = 13.0",
            "answer": "A",
            "explanation": "beta_1 = Cov(x,y) / Var(x) = 6 / 4 = 1.5. beta_0 = bar(y) - beta_1 * bar(x) = 25 - (1.5 * 10) = 25 - 15 = 10.0.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Polynomial regression",
            "question": "When fitting a high-degree polynomial regression model (e.g., degree 15) to a small dataset with noise, what typical behavior occurs regarding training error and test generalization error?",
            "option_a": "Training error approaches near zero while test generalization error explodes due to high variance (overfitting)",
            "option_b": "Both training and test error increase simultaneously due to high bias",
            "option_c": "The model becomes invariant to changes in input features",
            "option_d": "The model automatically prunes irrelevant high-order terms without regularization",
            "answer": "A",
            "explanation": "High-degree polynomials have high model capacity, fitting noise in the training set (near zero training error) but failing dramatically on unseen test data (high test error due to variance).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Interaction effects",
            "question": "In the regression model y = beta_0 + beta_1*x_1 + beta_2*x_2 + beta_3*(x_1*x_2) + epsilon, what is the partial derivative dy/dx_1 (marginal effect of x_1 on y)?",
            "option_a": "dy/dx_1 = beta_1 + beta_3 * x_2",
            "option_b": "dy/dx_1 = beta_1",
            "option_c": "dy/dx_1 = beta_1 + beta_2",
            "option_d": "dy/dx_1 = beta_3 * (x_1 + x_2)",
            "answer": "A",
            "explanation": "With an interaction term, the effect of x_1 on y is conditional on the level of x_2: dy/dx_1 = beta_1 + beta_3 * x_2.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Ridge regression",
            "question": "In Ridge regression, what is the effect of increasing the regularization hyperparameter lambda towards infinity?",
            "option_a": "The regression coefficients beta_j approach zero, reducing variance at the expense of higher bias",
            "option_b": "The regression coefficients beta_j diverge to infinity, increasing variance",
            "option_c": "The model fits every individual training point perfectly",
            "option_d": "The model transforms into an unconstrained ordinary least squares regression",
            "answer": "A",
            "explanation": "As lambda -> infinity, the penalty on coefficient magnitude ||beta||_2^2 dominates, shrinking all coefficients towards 0, resulting in a constant model with low variance but high bias.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Leverage",
            "question": "In linear regression diagnostics, high leverage points are identified using the diagonal elements h_ii of the hat matrix H = X(X^T X)^(-1) X^T. A data point has high leverage if:",
            "option_a": "Its predictor values x_i are extreme or far from the centroid of predictor space, regardless of its response value y_i",
            "option_b": "Its residual (y_i - y_hat_i) is negative",
            "option_c": "Its target value y_i is exactly equal to the sample mean bar(y)",
            "option_d": "Its Cook's distance is exactly zero",
            "answer": "A",
            "explanation": "Leverage h_ii measures the distance of the i-th observation's predictor values from the mean of predictors. It depends strictly on feature space X, not on target value y.",
            "difficulty": "hard",
            "question_type": "conceptual"
        }
    ]
    for q in s1_m3_q:
        q.update({"id": q_id, "subject": s1_name, "subject_code": s1_code, "module": m3_name, "module_number": 3})
        questions.append(q)
        q_id += 1

    # S1 M4: Classification & Supervised Learning
    m4_name = "Module IV - Classification & Supervised Learning"
    s1_m4_q = [
        {
            "topic": "Odds ratio",
            "question": "In a logistic regression model for disease diagnosis, the estimated coefficient for smoking status (binary predictor) is beta_1 = 0.693. What is the odds ratio associated with smoking, given e^(0.693) approx 2.0?",
            "option_a": "The odds of having the disease are 2.0 times higher for smokers compared to non-smokers",
            "option_b": "The probability of having the disease is exactly 69.3% higher",
            "option_c": "The odds of having the disease decrease by 50%",
            "option_d": "The odds ratio is 0.693, meaning smokers have lower risk",
            "answer": "A",
            "explanation": "In logistic regression, the odds ratio associated with a unit increase in predictor x is exp(beta). Here exp(0.693) = 2.0, meaning the odds of disease double for smokers.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Precision-Recall curves",
            "question": "For an extreme imbalanced classification problem (e.g., credit card fraud where positive fraud cases represent 0.05% of all transactions), why is the Precision-Recall AUC (PR-AUC) preferred over the ROC-AUC?",
            "option_a": "ROC-AUC uses False Positive Rate = FP / (FP + TN), which is dominated by the huge number of True Negatives, creating an overly optimistic performance metric",
            "option_b": "Precision-Recall curves cannot be computed when True Negatives are present",
            "option_c": "ROC-AUC requires all classes to be completely balanced at training time",
            "option_d": "Precision-Recall curves are invariant to changes in classification threshold",
            "answer": "A",
            "explanation": "In extreme class imbalance, TN is huge so FPR = FP / (FP + TN) remains tiny even for high FP counts, making ROC-AUC artificially inflated. PR curves focus directly on positive class performance.",
            "difficulty": "hard",
            "question_type": "comparison"
        },
        {
            "topic": "SMOTE",
            "question": "How does Synthetic Minority Over-sampling Technique (SMOTE) generate new synthetic samples for an imbalanced training dataset?",
            "option_a": "By taking linear combinations between minority class instances and their k-nearest minority class neighbors in feature space",
            "option_b": "By duplicating existing minority class records with exact copy replacement",
            "option_c": "By randomly removing majority class instances until class counts match",
            "option_d": "By flipping class labels of majority class boundary points",
            "answer": "A",
            "explanation": "SMOTE selects a minority sample x, identifies its k nearest minority neighbors, and generates synthetic points along the line segment connecting x and a chosen neighbor.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "SVM",
            "question": "In Soft-Margin Support Vector Machines (SVM), what is the role of the regularization hyperparameter C in the objective function min (1/2)||w||^2 + C * sum(xi_i)?",
            "option_a": "C controls the trade-off between maximizing the margin width and penalizing margin slack violations (slack variables xi_i)",
            "option_b": "C sets the degree of the polynomial kernel function directly",
            "option_c": "C determines the number of support vectors to discard during training",
            "option_d": "C forces all training data to lie strictly outside the margin boundaries",
            "answer": "A",
            "explanation": "Large C penalizes slack violations heavily (narrower margin, low bias, higher variance), while small C allows more violations (wider margin, higher bias, lower variance).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Random Forest",
            "question": "What are the two key randomization mechanisms that enable Random Forest ensembles to reduce variance compared to individual decision trees?",
            "option_a": "Bootstrap aggregating (bagging) of training instances and random feature subset selection at each node split",
            "option_b": "Random weight initialization and stochastic gradient descent updates",
            "option_c": "Random pruning of tree depth and random output thresholding",
            "option_d": "Random shuffling of class labels and random kernel transformations",
            "answer": "A",
            "explanation": "Random Forest de-correlates trees by training each tree on a bootstrap sample (bagging) and evaluating only a random subset of m features (typically sqrt(p)) at each split.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Confusion matrix",
            "question": "A model evaluated on 1,000 samples produces: TP = 80, FP = 20, FN = 40, TN = 860. What are the Precision, Recall, and F1-score for the positive class?",
            "option_a": "Precision = 0.80, Recall = 0.667, F1-score = 0.727",
            "option_b": "Precision = 0.667, Recall = 0.80, F1-score = 0.727",
            "option_c": "Precision = 0.80, Recall = 0.80, F1-score = 0.80",
            "option_d": "Precision = 0.88, Recall = 0.60, F1-score = 0.713",
            "answer": "A",
            "explanation": "Precision = TP / (TP + FP) = 80 / (80 + 20) = 80/100 = 0.80. Recall = TP / (TP + FN) = 80 / (80 + 40) = 80/120 = 2/3 approx 0.667. F1 = 2 * (0.80 * 0.667) / (0.80 + 0.667) approx 0.727.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Naive Bayes",
            "question": "What is the fundamental 'naive' conditional independence assumption made by the Naive Bayes classifier given class label C?",
            "option_a": "All feature predictors x_1, x_2, ..., x_d are mutually conditionally independent given the class label C: P(x_1, ..., x_d | C) = product(P(x_i | C))",
            "option_b": "The prior probabilities of all classes must be equal to 1/K",
            "option_c": "The features follow a uniform distribution across all domains",
            "option_d": "The covariance matrix between features is a dense non-diagonal matrix",
            "answer": "A",
            "explanation": "Naive Bayes assumes that features are conditionally independent given the target class, simplifying the joint probability P(X|C) into the product of individual conditional probabilities.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Gradient Boosting",
            "question": "How does Gradient Boosting sequentially construct an ensemble of weak base learners?",
            "option_a": "Each new weak learner is trained to predict the negative gradient (pseudo-residuals) of the loss function with respect to the current ensemble's predictions",
            "option_b": "Each learner is trained on an independently bootstrapped sample in parallel",
            "option_c": "Each learner adjusts instance weights by multiplying by exp(alpha) for misclassified points",
            "option_d": "Each learner replaces the previous learner whenever accuracy improves",
            "answer": "A",
            "explanation": "Gradient Boosting fits each sequential base estimator to the pseudo-residuals (gradient of the loss function L(y, f(x)) with respect to f(x)), performing gradient descent in function space.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Platt scaling",
            "question": "What is the function of Platt Scaling when applied to the output of a Support Vector Machine or uncalibrated classifier?",
            "option_a": "It fits a logistic regression model to the classifier's raw margin scores to output calibrated posterior probability estimates P(y=1|x)",
            "option_b": "It expands the kernel feature matrix into infinite dimensions",
            "option_c": "It converts continuous features into discrete quantile bins",
            "option_d": "It scales gradient updates during backpropagation",
            "answer": "A",
            "explanation": "Platt scaling transforms raw decision function outputs f(x) into calibrated class probabilities via a sigmoid function P(y=1|x) = 1 / (1 + exp(A*f(x) + B)), trained via MLE.",
            "difficulty": "hard",
            "question_type": "application"
        },
        {
            "topic": "Decision Trees",
            "question": "When building a classification decision tree with two classes (p_1, p_2), what is the Gini Impurity for a pure node (p_1 = 1, p_2 = 0) and a maximally impure node (p_1 = 0.5, p_2 = 0.5)?",
            "option_a": "Pure node = 0.0, Maximally impure node = 0.50",
            "option_b": "Pure node = 1.0, Maximally impure node = 0.0",
            "option_c": "Pure node = 0.50, Maximally impure node = 1.0",
            "option_d": "Pure node = 0.0, Maximally impure node = 1.0",
            "answer": "A",
            "explanation": "Gini = 1 - sum(p_i^2). For pure node: 1 - (1^2 + 0^2) = 0. For 50/50 split: 1 - (0.5^2 + 0.5^2) = 1 - 0.50 = 0.50.",
            "difficulty": "medium",
            "question_type": "numerical"
        }
    ]
    for q in s1_m4_q:
        q.update({"id": q_id, "subject": s1_name, "subject_code": s1_code, "module": m4_name, "module_number": 4})
        questions.append(q)
        q_id += 1

    # S1 M5: Unsupervised Learning & Dimensionality Reduction
    m5_name = "Module V - Unsupervised Learning & Dimensionality Reduction"
    s1_m5_q = [
        {
            "topic": "PCA",
            "question": "In Principal Component Analysis (PCA) applied to a standardized dataset X (mean 0, variance 1), what do the eigenvectors and eigenvalues of the sample covariance matrix X^T X / (n-1) represent?",
            "option_a": "Eigenvectors define the orthogonal directions of maximum variance; eigenvalues quantify the amount of variance explained along each principal axis",
            "option_b": "Eigenvectors represent cluster centroids; eigenvalues represent within-cluster sum of squares",
            "option_c": "Eigenvectors define class decision boundaries; eigenvalues represent misclassification error",
            "option_d": "Eigenvectors contain kernel weights; eigenvalues represent polynomial degrees",
            "answer": "A",
            "explanation": "PCA projects data onto the eigenvectors of the covariance matrix, ordered by descending eigenvalues lambda_i which equal the variance captured along each principal component.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "LDA",
            "question": "How does Linear Discriminant Analysis (LDA) differ fundamentally from Principal Component Analysis (PCA) in its mathematical objective?",
            "option_a": "PCA is unsupervised and maximizes total variance, whereas LDA is supervised and maximizes between-class variance relative to within-class variance",
            "option_b": "LDA is completely unsupervised while PCA requires class labels",
            "option_c": "PCA can only project to 1 dimension whereas LDA projects to infinite dimensions",
            "option_d": "LDA minimizes total dataset variance while PCA maximizes classification error",
            "answer": "A",
            "explanation": "PCA finds directions of maximum overall variance without labels (unsupervised). LDA maximizes Fisher's criterion S_B / S_W (between-class scatter vs within-class scatter) using class labels.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "K-means",
            "question": "What objective function does the standard Lloyd's K-Means clustering algorithm iteratively minimize?",
            "option_a": "The Within-Cluster Sum of Squares (WCSS) / Inertia across all k clusters",
            "option_b": "The Between-Cluster variance divided by total variance",
            "option_c": "The maximum Chebyshev distance between cluster centroids",
            "option_d": "The Silhouette coefficient across border instances",
            "answer": "A",
            "explanation": "K-means minimizes WCSS = sum_{k=1}^K sum_{x in S_k} ||x - mu_k||^2, assigning points to nearest centroids and recalculating centroids until convergence.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "DBSCAN",
            "question": "In Density-Based Spatial Clustering of Applications with Noise (DBSCAN), what distinguishes a 'Core Point' from a 'Border Point' given parameters eps and MinPts?",
            "option_a": "A Core Point contains at least MinPts within its eps-neighborhood; a Border Point has fewer than MinPts within eps but falls inside the eps-neighborhood of a Core Point",
            "option_b": "A Core Point is located on the boundary of a convex hull",
            "option_c": "A Border Point is always classified as noise (-1)",
            "option_d": "A Core Point must have zero distance to its nearest cluster neighbor",
            "answer": "A",
            "explanation": "Core points satisfy |N_eps(p)| >= MinPts. Border points have |N_eps(p)| < MinPts but are density-reachable from a core point. Noise points are neither.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Silhouette score",
            "question": "For a data point i, let a(i) be the mean distance to all other points in its own cluster, and b(i) be the mean distance to points in the nearest neighbor cluster. What is the formula for the Silhouette score s(i), and what does s(i) = 0.85 indicate?",
            "option_a": "s(i) = (b(i) - a(i)) / max(a(i), b(i)); indicating the point is well-clustered and far from neighboring clusters",
            "option_b": "s(i) = (a(i) - b(i)) / (a(i) + b(i)); indicating the point belongs to a noise cluster",
            "option_c": "s(i) = a(i) / b(i); indicating high cluster overlap",
            "option_d": "s(i) = b(i) - a(i); indicating the cluster has 85 points",
            "answer": "A",
            "explanation": "Silhouette score s(i) = (b(i) - a(i)) / max(a(i), b(i)), ranging from -1 to +1. A value close to +1 (0.85) indicates tight intra-cluster cohesion and good inter-cluster separation.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "t-SNE",
            "question": "Why does t-SNE (t-Distributed Stochastic Neighbor Embedding) employ a Student's t-distribution (with 1 degree of freedom) in the low-dimensional embedding space rather than a Gaussian distribution?",
            "option_a": "The heavy tails of the Cauchy/t-distribution alleviate the 'crowding problem', preventing moderately distant points in high dimensions from collapsing into a dense cluster in 2D",
            "option_b": "The t-distribution computes faster than exponential Gaussian calculations",
            "option_c": "Gaussian distributions cannot model non-negative probability densities",
            "option_d": "The t-distribution guarantees global convexity of the KL-divergence loss function",
            "answer": "A",
            "explanation": "The 'crowding problem' arises because the volume of sphere in 2D is much smaller than in high dimensions. The heavy tail of the t-distribution allows moderate distances in high-D to map to larger distances in low-D.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Isolation Forest",
            "question": "What is the foundational principle underlying the Isolation Forest algorithm for anomaly/outlier detection?",
            "option_a": "Anomalies are few and structurally different, requiring fewer random partition splits to be isolated in terminal leaf nodes (shorter average path lengths in iTrees)",
            "option_b": "Anomalies always have the highest density of nearest neighbors in high-dimensional space",
            "option_c": "Anomalies follow a Gaussian distribution with zero mean and unit variance",
            "option_d": "Anomalies require constructing convex hulls around cluster centroids",
            "answer": "A",
            "explanation": "Isolation Forest randomly selects a feature and split value. Because anomalies are sparse and distinct, they are isolated close to the root with noticeably shorter path lengths h(x).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "LOF",
            "question": "How does Local Outlier Factor (LOF) identify anomalous data points in comparison to global density methods?",
            "option_a": "It compares the local density of an object to the local densities of its k-nearest neighbors, allowing detection of anomalies in datasets with varying density clusters",
            "option_b": "It computes a single global distance threshold for the entire dataset",
            "option_c": "It fits a single multivariate normal ellipsoid over all observations",
            "option_d": "It requires all clusters to have identical variance and sample counts",
            "answer": "A",
            "explanation": "LOF is a local anomaly detection algorithm: an object with substantially lower local reachability density than its neighbors receives a LOF score > 1, detecting local outliers even across differing density clusters.",
            "difficulty": "hard",
            "question_type": "application"
        },
        {
            "topic": "Hierarchical clustering",
            "question": "In agglomerative hierarchical clustering, which linkage criterion computes the distance between two clusters as the maximum distance between any single pair of points across the clusters?",
            "option_a": "Complete linkage (Maximum linkage)",
            "option_b": "Single linkage (Minimum linkage)",
            "option_c": "Average linkage (UPGMA)",
            "option_d": "Ward's minimum variance linkage",
            "answer": "A",
            "explanation": "Complete linkage uses max {d(u, v) : u in A, v in B}, producing compact, spherical clusters and avoiding the 'chaining effect' seen in single linkage.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "UMAP",
            "question": "Compared to t-SNE, what major practical and theoretical advantage does UMAP (Uniform Manifold Approximation and Projection) provide for high-dimensional visualization and preprocessing?",
            "option_a": "UMAP better preserves both local and global topological structure while offering significantly faster computational scaling and supporting transformation of new unseen data",
            "option_b": "UMAP is strictly limited to 2-dimensional embeddings only",
            "option_c": "UMAP does not require any distance metric specification",
            "option_d": "UMAP eliminates the need for any hyperparameter tuning",
            "answer": "A",
            "explanation": "UMAP is grounded in Riemannian geometry and algebraic topology. It captures global structure better than t-SNE, scales faster O(N) to large datasets, and can transform new data points into the learned manifold.",
            "difficulty": "hard",
            "question_type": "comparison"
        }
    ]
    for q in s1_m5_q:
        q.update({"id": q_id, "subject": s1_name, "subject_code": s1_code, "module": m5_name, "module_number": 5})
        questions.append(q)
        q_id += 1

    # S1 M6: Model Evaluation, Bayesian Inference & Ethics
    m6_name = "Module VI - Model Evaluation, Bayesian Inference & Ethics"
    s1_m6_q = [
        {
            "topic": "AIC",
            "question": "For a statistical model with k estimated parameters and maximum log-likelihood ln(hat(L)), what is Akaike's Information Criterion (AIC), and what does a lower AIC value indicate?",
            "option_a": "AIC = 2k - 2*ln(hat(L)); a lower value indicates a better trade-off between goodness-of-fit and model complexity",
            "option_b": "AIC = k*ln(n) - 2*ln(hat(L)); a lower value indicates high underfitting",
            "option_c": "AIC = 2*ln(hat(L)) - k; a lower value indicates high variance",
            "option_d": "AIC = hat(L) / (2*k); a lower value indicates maximum parameter count",
            "answer": "A",
            "explanation": "AIC = 2k - 2ln(L). The 2k penalty discourages overfitting by penalizing additional parameters; lower AIC denotes superior relative model quality.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Posterior",
            "question": "According to Bayes' Theorem, how is the posterior distribution P(theta | D) expressed in terms of prior P(theta), likelihood P(D | theta), and marginal evidence P(D)?",
            "option_a": "P(theta | D) = (P(D | theta) * P(theta)) / P(D)",
            "option_b": "P(theta | D) = P(D | theta) / (P(theta) * P(D))",
            "option_c": "P(theta | D) = P(D) * P(theta) / P(D | theta)",
            "option_d": "P(theta | D) = P(D | theta) + P(theta) - P(D)",
            "answer": "A",
            "explanation": "Bayes' formula states Posterior = (Likelihood * Prior) / Evidence: P(theta|D) = [P(D|theta) * P(theta)] / int P(D|theta)P(theta)d theta.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Beta-Bernoulli",
            "question": "In Bayesian inference, if the prior distribution on parameter p is Beta(alpha, beta) and we observe k successes and (n - k) failures in n independent Bernoulli trials, what is the exact analytical posterior distribution?",
            "option_a": "Beta(alpha + k, beta + n - k)",
            "option_b": "Normal(alpha + k, beta + n - k)",
            "option_c": "Beta(alpha * k, beta * (n - k))",
            "option_d": "Gamma(alpha + k, beta + n)",
            "answer": "A",
            "explanation": "The Beta distribution is the conjugate prior for the Bernoulli/Binomial likelihood. The posterior updates algebraically by adding observed successes and failures: Beta(alpha + k, beta + n - k).",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "SHAP",
            "question": "What mathematical property from cooperative game theory guarantees that SHAP (SHapley Additive exPlanations) values distribute feature contributions fairly and uniquely?",
            "option_a": "Efficiency, Symmetry, Dummy (Null player), and Additivity axioms of Shapley values",
            "option_b": "Maximum Entropy principle and Nash Equilibrium",
            "option_c": "Gauss-Markov theorem of minimum variance",
            "option_d": "Pareto optimality and Karush-Kuhn-Tucker conditions",
            "answer": "A",
            "explanation": "SHAP values are the unique additive feature attribution method satisfying all 4 fundamental Shapley axioms: Efficiency (sum equals difference from base value), Symmetry, Dummy, and Additivity.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "LIME",
            "question": "How does LIME (Local Interpretable Model-agnostic Explanations) explain an individual prediction made by a complex black-box machine learning model?",
            "option_a": "It perturbs the input instance, collects model predictions on the perturbed samples, weights them by proximity to the instance, and fits an interpretable linear model locally",
            "option_b": "It computes exact analytical gradients through all hidden layers globally",
            "option_c": "It retrains the entire black-box model using only single decision tree rules",
            "option_d": "It inverts the final softmax layer using pseudo-inverse matrix decomposition",
            "answer": "A",
            "explanation": "LIME constructs a local surrogate model: it samples perturbations around instance x, weights them by similarity kernel pi_x(z), and trains a simple interpretable model (e.g. Ridge or sparse linear regression) locally.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Demographic parity",
            "question": "In AI ethics and algorithmic fairness, a binary classification decision rule hat(Y) in {0, 1} satisfies Demographic Parity (Statistical Parity) with respect to a protected demographic attribute A in {0, 1} if:",
            "option_a": "P(hat(Y) = 1 | A = 0) = P(hat(Y) = 1 | A = 1)",
            "option_b": "P(hat(Y) = 1 | Y = 1, A = 0) = P(hat(Y) = 1 | Y = 1, A = 1)",
            "option_c": "P(Y = 1 | hat(Y) = 1, A = 0) = P(Y = 1 | hat(Y) = 1, A = 1)",
            "option_d": "P(hat(Y) = Y | A = 0) = 1.0",
            "answer": "A",
            "explanation": "Demographic Parity requires that the likelihood of receiving a positive outcome (e.g., loan approval) is identical across all protected demographic groups, regardless of true label Y.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Equalized odds",
            "question": "How does the fairness metric Equalized Odds refine Demographic Parity to account for true underlying qualifications or target labels Y?",
            "option_a": "It requires both True Positive Rate and False Positive Rate to be equal across all protected groups: P(hat(Y)=1 | Y=y, A=0) = P(hat(Y)=1 | Y=y, A=1) for y in {0, 1}",
            "option_b": "It forces equal error rates only when the model accuracy is 100%",
            "option_c": "It prohibits using any numerical features in the training pipeline",
            "option_d": "It requires the base rates P(Y=1 | A=0) and P(Y=1 | A=1) to be artificially altered",
            "answer": "A",
            "explanation": "Equalized odds requires that predictor hat(Y) and protected attribute A are conditionally independent given true outcome Y, equating both TPR and FPR across groups.",
            "difficulty": "hard",
            "question_type": "comparison"
        },
        {
            "topic": "Brier score",
            "question": "A probabilistic weather prediction model outputs predicted rain probabilities p_i. The Brier score is computed across N days with binary rain outcomes y_i in {0, 1}. What is the formula and optimal value?",
            "option_a": "Brier Score = (1/N) * sum((p_i - y_i)^2); optimal value is 0 (perfect calibration and accuracy)",
            "option_b": "Brier Score = sum(y_i * ln(p_i)); optimal value is +infinity",
            "option_c": "Brier Score = (1/N) * sum(|p_i - y_i|); optimal value is 1.0",
            "option_d": "Brier Score = 1 - (TP / (TP + FP)); optimal value is 0.50",
            "answer": "A",
            "explanation": "The Brier score is the mean squared error of probability forecasts: (1/N) * sum((p_i - y_i)^2). It is a strictly proper scoring rule where 0 indicates perfect probability calibration.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "LOOCV",
            "question": "When comparing Leave-One-Out Cross-Validation (LOOCV) with 10-fold cross-validation on a dataset of size n = 500, what is the primary computational and statistical trade-off?",
            "option_a": "LOOCV requires fitting the model 500 times with low bias but potentially high variance due to correlated training sets, whereas 10-fold CV requires only 10 fits and is computationally much faster",
            "option_b": "LOOCV trains only 1 model whereas 10-fold CV trains 500 models",
            "option_c": "LOOCV has higher estimation bias than 10-fold CV",
            "option_d": "10-fold CV is strictly non-deterministic while LOOCV cannot evaluate regression models",
            "answer": "A",
            "explanation": "LOOCV sets k = n, training n models on n-1 points. It has virtually no bias relative to the full dataset, but is computationally expensive for large n and has higher variance because the n training sets are 99.8% identical.",
            "difficulty": "hard",
            "question_type": "comparison"
        },
        {
            "topic": "PDP",
            "question": "What is the primary difference in interpretation between a Partial Dependence Plot (PDP) and Individual Conditional Expectation (ICE) plots for a feature x_s?",
            "option_a": "A PDP shows the average marginal effect of feature x_s across the entire population, while ICE plots show individual functional curves for every single instance, revealing heterogeneous interactions",
            "option_b": "PDP is strictly for classification while ICE is strictly for unsupervised clustering",
            "option_c": "ICE plots average all features simultaneously while PDP focuses on one sample",
            "option_d": "PDP requires model retraining while ICE plots do not use model predictions",
            "answer": "A",
            "explanation": "PDP displays the global average marginal effect E_{x_c}[f(x_s, x_c)]. ICE plots un-aggregate this by plotting one curve per instance, making subgroup differences and interaction effects visible.",
            "difficulty": "medium",
            "question_type": "comparison"
        }
    ]
    for q in s1_m6_q:
        q.update({"id": q_id, "subject": s1_name, "subject_code": s1_code, "module": m6_name, "module_number": 6})
        questions.append(q)
        q_id += 1

    return questions, q_id

if __name__ == "__main__":
    qs, last_id = generate_all_questions()
    print(f"Generated {len(qs)} questions for Subject 1. Last ID: {last_id}")
