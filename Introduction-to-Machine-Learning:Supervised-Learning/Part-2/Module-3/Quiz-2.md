1.
Question 1
When analyzing cluster profiles, which of the following steps can help derive more meaningful insights? Select all that apply.

Assuming clusters have equal variance by default.

Visualizing clusters using dimensionality reduction techniques.

Nice work
Correct! Visualization can provide an intuitive understanding of the cluster distribution.

Evaluating the silhouette score of the clusters.

Nice work
Good choice! The silhouette score helps in understanding the separation between clusters.

Ignoring outliers as they do not affect analysis.

1 / 1 point


2.
Question 2
What is the primary advantage of using Gaussian Mixture Models (GMMs) over K-means clustering?

GMMs guarantee convergence to the global optimum.

GMMs require less computational power than K-means.

GMMs can model complex data distributions with overlapping clusters.

GMMs are easier to implement than K-means.

Nice work
Correct! Gaussian Mixture Models can capture more complex cluster shapes due to their probabilistic approach, unlike K-means which assumes spherical clusters.

1 / 1 point


3.
Question 3
What is the primary objective of the k-means clustering algorithm?

Enhance data visualization.

Maximize the number of clusters.

Minimize the within-cluster sum of squares.

Maximize the distance between clusters.

Nice work
Great! The goal of k-means is to minimize the within-cluster sum of squares (WCSS) to ensure tight clusters.

1 / 1 point


4.
Question 4
Which aspects should you consider when assigning labels to clusters to ensure they are appropriate and ethical? Select all that apply.

Clarity and interpretability of the labels.

Nice work
Correct. Clear and interpretable labels facilitate understanding and communication of insights.

Cultural sensitivity of the labels.

Nice work
Correct. Considering cultural sensitivity ensures the labels are respectful and appropriate for diverse groups.

Personal biases and preferences.

Relevance to current market trends.

Statistical significance of cluster differences

Nice work
Correct. Understanding statistical significance aids in providing meaningful labels based on data insights.

1 / 1 point


5.
Question 5
Which of the following statements are true about the update step in the k-means algorithm? Select all that apply.

The update step runs before the initial assignment of data points.

It recalculates the centroids based on current cluster assignments.

Nice work
Exactly! Recalculating centroids is a key part of the update step in k-means.

It minimizes the mean square error within clusters.

Nice work
Correct! The update step minimizes the mean square error, ensuring better cluster cohesion.

It always increases the within-cluster sum of squares.

It involves assigning data points to the nearest centroid.

1 / 1 point


6.
Question 6
Which of the following are common methods used in clustering? Select all that apply.

K-Means

Nice work
Right! K-Means is a popular clustering method.

Principal Component Analysis

Hierarchical Clustering

Nice work
Yes, hierarchical clustering is a widely used technique in unsupervised learning.

Support Vector Machines

1 / 1 point


7.
Question 7
What does the assignment step in the k-means algorithm ensure?

It decreases the number of data points.

It does not increase the objective function 
J
JJ.

It optimizes the centroid positions.

It increases the number of clusters.

Nice work
Well done! The assignment step aims to ensure that the objective function 
J
JJ, representing total variance, does not increase.

1 / 1 point


8.
Question 8
What is the purpose of the Silhouette method in the context of clustering?

To determine the maximum number of clusters possible.

To calculate the variance of data points within a cluster.

To visualize the clustering process in real-time.

To assess how similar an object is to its own cluster compared to other clusters.

Nice work
Correct! The Silhouette method evaluates cluster cohesion and separation.

1 / 1 point


9.
Question 9
Which method is used to determine the optimal number of clusters in k-means clustering?

Silhouette method

Hierarchical clustering

Elbow method

Principal Component Analysis

Nice work
Great job! The Elbow method is commonly used to find the optimal number of clusters by plotting the within-cluster sum of squares against the number of clusters.

1 / 1 point


10.
Question 10
When analyzing cluster profiles, which elements are essential to consider for deriving meaningful insights? Select all that apply.

Cluster size variability within the dataset.

Nice work
Correct! Variability in cluster sizes can indicate different levels of diversity or homogeneity in the dataset.

The distribution of data points within each cluster.

Nice work
Correct! Understanding how data points are distributed helps in assessing the cluster's representation.

The initial centroids chosen for clustering.

The average distance between clusters.

This should not be selected
Incorrect. While distances can be insightful, the average distance alone provides limited insights without considering other factors.

The color coding used in cluster visualization.









1.
Question 1
In hierarchical clustering, what does a dendrogram represent?

A tree-like diagram illustrating data point merges.

A chart of feature importances.

A graph showing correlation coefficients.

A tree-like diagram showing data point distances.

Nice work
Correct! A dendrogram shows how data points are grouped together.

1 / 1 point


2.
Question 2
What is a limitation of K-means clustering that Gaussian Mixture Models can overcome?

K-means can model overlapping clusters effectively.

K-means always converges to the global optimum.

K-means is highly efficient with very large datasets.

K-means assumes all clusters are spherical and equally sized.

Nice work
Correct! K-means assumes clusters are spherical and of equal size, which GMMs can model more flexibly with varying shapes and sizes.

1 / 1 point


3.
Question 3
Which of the following best describes the concept of probabilistic membership in Gaussian Mixture Models?

Data points are randomly assigned to clusters without probabilities.

Probabilistic membership is irrelevant in GMMs.

Each data point belongs to all clusters with certain probabilities.

Each data point belongs to only one cluster with absolute certainty.

Nice work
Correct! In GMMs, each data point is assigned a probability of belonging to each cluster, allowing for overlapping memberships.

1 / 1 point


4.
Question 4
Which of the following statements accurately describe the Expectation-Maximization (EM) algorithm when applied to Gaussian Mixture Models (GMMs)? Select all that apply.

The EM algorithm guarantees finding the global maximum of the likelihood function.

The convergence of the EM algorithm is determined by the improvement in log-likelihood between iterations.

Nice work
Correct! The algorithm typically checks for convergence by monitoring changes in log-likelihood.

The E-step involves estimating the probability that each data point belongs to each cluster.

Nice work
Correct! The E-step estimates the membership probabilities for each data point in each cluster.

The EM algorithm requires prior knowledge of the exact number of clusters.

The M-step updates the model parameters to maximize the expected log-likelihood.

Nice work
Correct! The M-step focuses on refining the model parameters to increase the fit.

1 / 1 point


5.
Question 5
How can the performance of a clustering algorithm be evaluated without true labels?

Using the silhouette score.

Measuring ROC-AUC.

Using confusion matrices.

Calculating accuracy.

Nice work
Correct! The silhouette score helps evaluate the quality of clusters without labels.

1 / 1 point


6.
Question 6
Which of the following steps are part of the k-means clustering algorithm? Select all that apply.

Use decision trees to split data.

Merge clusters based on distance.

Assign each data point to the nearest centroid.

Nice work
Good job! Data points are assigned based on their proximity to centroids.

Initialize centroids randomly.

Nice work
Correct! Initializing centroids randomly is a crucial first step in the k-means algorithm.

Calculate new centroids by averaging data points in each cluster.

Nice work
Well done! New centroids are computed by averaging the data points assigned to each cluster.

1 / 1 point


7.
Question 7
Which mathematical approach is used to find the optimal centroid for a cluster in k-means clustering?

Applying the mean of all data points.

Maximizing the variance within the cluster.

Using derivatives to minimize the distance.

Calculating the median point of the cluster.

Nice work
Correct! Derivatives are used to calculate the optimal centroid by minimizing the distance.

1 / 1 point


8.
Question 8
Which of the following methods can be used to assess the quality of clusters in a dataset? Select all that apply.

Elbow method

Nice work
Right! The Elbow method helps in determining the quality of clusters by plotting within-cluster sums of squares.

Confusion matrix

Within-cluster sum of squares

Nice work
Good choice! WCSS indicates the compactness of clusters, reflecting quality.

Silhouette method

Nice work
Correct! The Silhouette method evaluates how well-separated a cluster is from others.

Cross-validation

1 / 1 point


9.
Question 9
What are potential pitfalls of the K-Means clustering algorithm? Select all that apply.

Sensitivity to outliers.

Nice work
Correct. Outliers can significantly affect K-Means clustering outcomes.

Inability to handle large datasets.

Sensitivity to initial centroid placement.

Nice work
Correct, K-Means can yield different results based on initial centroids.

Difficulty in clustering non-spherical data.

Nice work
Yes, K-Means struggles with non-spherical clusters.

Guaranteed global optimum solution.

1 / 1 point


10.
Question 10
What is the primary goal of clustering in unsupervised learning?

To find patterns and structures in data without pre-labeled outcomes.

To label data for classification tasks.

To increase the accuracy of supervised models.

To minimize the number of features in a dataset.

Nice work
Correct! Clustering aims to discover hidden patterns without using pre-labeled data.

1 / 1 point
