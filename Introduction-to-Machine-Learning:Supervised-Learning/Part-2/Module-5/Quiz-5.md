1.
Question 1
Which statement best describes a generative model?

A model that reduces the dimensionality of the data for visualization.

A model that predicts future events based on historical data.

A model that generates new samples from an existing dataset.

A model that optimizes decision-making processes.

Nice work
Correct! Generative models are designed to create new instances that resemble the data they were trained on.

1 / 1 point


2.
Question 2
In the SVD-based alternating imputation algorithm, how should the rank M be chosen in practice?

M should be set to 1 for all datasets.

M should equal the number of missing entries.

By using cross-validation on held-out observed entries.

M should always equal the number of variables in the dataset.

Nice work
Correct! Cross-validation on observed entries — trying different values of M and selecting the one with the lowest reconstruction error on validation data, allows you to find the rank that best balances approximation quality and overfitting

1 / 1 point


3.
Question 3
What is the main goal of unsupervised learning in machine learning?

To find hidden patterns or intrinsic structures in unlabeled data.

To train a model to predict outcomes from labeled data.

To enhance the accuracy of supervised learning models.

To optimize the parameters of a pre-trained model.

Nice work
Correct! Unsupervised learning aims to discover patterns without predefined labels.

1 / 1 point


4.
Question 4
A data scientist has a large dataset of customer purchase histories with no labels or predefined categories. She wants to group customers so that customers within each group have similar purchasing behavior. Which unsupervised learning approach is most appropriate?

Regression

Anomaly detection

Classification

Clustering

Nice work
Correct! Clustering groups data points based on similarity, making it ideal for finding natural customer segments in unlabeled data.

1 / 1 point


5.
Question 5
An Isolation Forest is trained on a dataset and flags a small number of observations as anomalies. If the contamination parameter is set to 5%, but only a much smaller fraction of points are truly anomalous, what is the most likely outcome?

The model will only detect anomalies that are at least 5% different from the mean.

The model will fail to converge.

The model will flag some normal points as anomalies (false positives).

The model will automatically adjust its contamination rate to match the true rate.

Nice work
Correct! Setting contamination higher than the true anomaly rate causes the model to over-flag normal observations.

1 / 1 point


6.
Question 6
Which of the following are important steps in the text preprocessing phase for Latent Dirichlet Allocation (LDA)? Select all that apply.

Applying Gaussian filters to text data.

Converting text to uppercase for uniformity.

Stemming or lemmatization of words.

Nice work
Correct. Stemming or lemmatization helps in reducing words to their base or root form.

Tokenization of text data.

Nice work
Correct. Tokenization is a crucial step in preparing text data for analysis.

Removing stop words from the text.

Nice work
Correct. Stop words are often removed to focus on more meaningful words.

1 / 1 point


7.
Question 7
A dataset has Feature X with observed values: 40, 55, 45, 60, and one missing entry. A data scientist applies mean imputation. Which of the following statements is true about the imputed value? 

The missing entry is replaced with the mean of all features across the entire row.

The missing entry is replaced with the mean of the observed values of Feature X (50 in this case).

The missing entry is replaced with the median of Feature X.

The missing entry is replaced with the most frequent value in Feature X.

Nice work
Correct! Mean imputation replaces each missing value with the column mean computed from the non-missing observations.

1 / 1 point


8.
Question 8
What is the purpose of "validation by masking" when evaluating imputation quality?

To mask the identities of individuals in the dataset for privacy.

To artificially hide a subset of known observed values, run imputation, and then compare the imputed values to the true held-out values.

To prevent the imputation algorithm from using certain features.

To remove all missing values from the dataset before imputation.

Nice work
Correct! Since we don't know the true missing values, masking observed entries creates a ground truth for evaluating imputation accuracy.

1 / 1 point


9.
Question 9
What is the first step in text preprocessing for Latent Dirichlet Allocation (LDA)?

Part-of-speech tagging

Tokenization

Removing stop words

Stemming

Nice work
Correct! Tokenization is usually the first step in preparing text for LDA.

1 / 1 point



10.
Question 10
Why is it important to understand the impact of missing values in a dataset?

Because missing values need to be converted to zeros to maintain consistency.

Because missing values can bias the results of data analysis if not handled properly.

Because missing values are useful for increasing the dataset size.

Because they always indicate a data collection error.

Nice work
Correct! Missing values may lead to biased or incorrect conclusions if they are not properly addressed.
