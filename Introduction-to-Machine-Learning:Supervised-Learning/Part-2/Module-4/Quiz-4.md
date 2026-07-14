1.
Question 1
In clustering analysis, what is the primary goal?

To partition a dataset into groups where members of a group are more similar to each other than to those in other groups.

To reduce the dimensionality of data to make it more manageable.

To determine the causal relationship between variables.

To predict a dependent variable based on independent variables.

Nice work
Well done! The primary goal of clustering is to group similar data points together.

1 / 1 point


2.
Question 2
Which methods can be used to determine the number of clusters in a dataset? Select all that apply.

Principal Component Analysis

Silhouette analysis

Nice work
Correct! Silhouette analysis measures how similar an object is to its own cluster compared to other clusters.

Elbow method

Nice work
Correct! The elbow method helps visualize the variance explained as a function of the number of clusters.

Kurtosis test

1 / 1 point


3.
Question 3
What is a key challenge when using hierarchical clustering for large datasets?
Computational complexity increases with dataset size.

Hierarchical clustering does not require distance metrics.

Clusters are always determined by the initial conditions.

It only works with categorical data, not numerical data.

Nice work
That's right! Hierarchical clustering's time complexity can become a bottleneck with large datasets due to the calculations involved.

1 / 1 point


4.
Question 4
What characteristics can be used to profile clusters after assigning data points? Select all that apply.

Mean values of attributes within the cluster.

Nice work
Correct! Mean values provide a central tendency measure for the attributes in a cluster.

The sequence in which data points were added to the cluster.

Standard deviation of attributes within the cluster.

Nice work
Correct! Standard deviation helps understand the variability of attributes within the cluster.

Unique color assigned to each cluster.

1 / 1 point


5.
Question 5
Identify the factors to consider when choosing a linkage method for hierarchical clustering. Select all that apply.

Number of clusters desired.

This should not be selected
Incorrect. Hierarchical clustering doesn't require a pre-specified number of clusters. Reflect on its exploratory nature.

Shape of the data.

Nice work
Correct! The shape of the data can significantly influence the choice of linkage method.

Computational efficiency.

Nice work
Great! Computational efficiency is crucial, especially with large datasets.

Presence of outliers.

Nice work
Yes, outliers can impact the effectiveness of different linkage methods.

The color of the data points.

0.8 / 1 point


6.
Question 6
When analyzing a dendrogram, what indicates an optimal cutting point to extract clusters?

The longest vertical distance between horizontal cuts.

The shortest vertical distance between horizontal cuts.

The point where the branches intersect the x-axis.

The point closest to the top of the dendrogram.

Nice work
Well done! The longest vertical distance between horizontal cuts in a dendrogram typically indicates the optimal points for cutting to form clusters.

1 / 1 point


7.
Question 7
Identify the techniques commonly used to evaluate the quality of clustering results. Select all that apply.

Elbow Method

Nice work
Right! The Elbow Method helps in determining the optimal number of clusters.

Silhouette Score

Nice work
Correct! Silhouette Score is widely used to assess how well data points have been clustered.

Dunn Index

Nice work
Good job! Dunn Index measures the compactness and separation of the clusters.

Gini Impurity

Gradient Descent

1 / 1 point


8.
Question 8
What are some key characteristics that differentiate hierarchical clustering methods from other clustering methods? Select all that apply. 

They can only be used with continuous data.

They do not require the number of clusters to be specified beforehand.

Nice work
Correct! Hierarchical clustering builds a hierarchy of clusters without the need for pre-specifying the number of clusters.

They always produce non-overlapping clusters.

Nice work
Correct! Hierarchical clustering cannot produce overlapping clusters depending on the linkage criteria used. 

They are always more computationally efficient than other methods.

1 / 1 point


9.
Question 9
Which of the following are true about the Expectation-Maximization (EM) algorithm? Select all that apply.

EM can be used for clustering applications.

Nice work
Good job! EM is often employed for clustering, especially in Gaussian mixture models.

EM is used to find maximum likelihood estimates.

Nice work
Correct! The EM algorithm helps in estimating the parameters in statistical models.

EM requires labeled data to work.

EM directly solves the optimization problem in closed form.

1 / 1 point


10.
Question 10
Which linkage method in hierarchical clustering tends to create elongated clusters by prioritizing the shortest distance between points in different clusters?

Single linkage

Centroid linkage

Complete linkage

Average linkage

Nice work
Correct! Single linkage, also known as the nearest neighbor method, uses the shortest distance between points to form clusters.










1.
Question 1
What is an important step to consider when assigning data points to clusters?

Assigning data points based on their labels.

Maximizing the number of clusters to ensure precise grouping.

Calculating the Euclidean distance between data points.

Ensuring each cluster has a unique identifier.

Nice work
Great job! Calculating the Euclidean distance helps measure the similarity between data points, which is crucial for assigning them to clusters.

1 / 1 point


2.
Question 2
Select the properties that define a good clustering algorithm. Select all that apply.

Ability to identify non-linear structures

Nice work
Good choice! Identifying non-linear structures allows clustering algorithms to better capture the shapes of data.

Dependence on data labels

Scalability to large datasets

Nice work
Well done! Scalability is essential for clustering algorithms to handle large datasets efficiently.

High intra-cluster similarity

Nice work
Correct! A good clustering algorithm ensures that items within the same cluster are very similar.

High inter-cluster similarity

1 / 1 point


3.
Question 3
In unsupervised learning, which technique is used to reduce the dimensionality of data while preserving variance?

Principal Component Analysis (PCA)

Logistic Regression

Hierarchical Clustering

Decision Trees

Nice work
Excellent! PCA is used to reduce dimensionality while preserving as much variance as possible.

1 / 1 point


4.
Question 4
Which algorithm is most commonly used for clustering in unsupervised learning?

Linear Regression

K-Means Clustering

Principal Component Analysis

Support Vector Machines

Nice work
Great job! K-Means Clustering is widely used for its simplicity and efficiency in unsupervised learning tasks.

1 / 1 point


5.
Question 5
What is the primary purpose of Principal Component Analysis (PCA) in unsupervised learning?

Dimensionality reduction

Enhancing model accuracy

Data clustering

Predicting outcomes

Nice work
Well done! PCA is mainly used to reduce the number of variables in the data while preserving as much information as possible.

1 / 1 point


6.
Question 6
In which scenario is hierarchical clustering most appropriate to use?

When a fixed number of clusters is known beforehand.

When real-time clustering is required.

When the dataset contains non-spherical clusters.

When clustering a very large dataset quickly.

Nice work
Correct! Hierarchical clustering is versatile and can handle non-spherical clusters.

1 / 1 point


7.
Question 7
Which of the following are characteristics of complete linkage in hierarchical clustering? Select all that apply.

Considers the maximum distance between clusters.

Nice work
Yes, complete linkage uses the furthest distance between points when merging clusters.

Primarily used for clustering non-numeric data.

Uses the shortest distance between points.

Sensitive to outliers.

Nice work
Great! Complete linkage can be sensitive to outliers, affecting the clustering outcome.

May produce compact clusters.

Nice work
Correct! The method tends to create more compact clusters.

1 / 1 point


8.
Question 8
Which of the following best describes the process of agglomerative hierarchical clustering?

Random assignment of clusters.

Top-down approach splitting clusters.

Clusters formed based on data density.

Bottom-up approach merging clusters.

Nice work
Great job! Agglomerative hierarchical clustering starts with individual points and merges them into clusters.

1 / 1 point


9.
Question 9
Which of the following are true about the Expectation-Maximization (EM) algorithm? Select all that apply.

EM is used to find maximum likelihood estimates.

Nice work
Correct! The EM algorithm helps in estimating the parameters in statistical models.

EM can be used for clustering applications.

Nice work
Good job! EM is often employed for clustering, especially in Gaussian mixture models.

EM directly solves the optimization problem in closed form.

EM requires labeled data to work.

1 / 1 point


10.
Question 10
Identify the techniques commonly used to evaluate the quality of clustering results. Select all that apply.

Gradient Descent

Dunn Index

Nice work
Good job! Dunn Index measures the compactness and separation of the clusters.

Elbow Method

Nice work
Right! The Elbow Method helps in determining the optimal number of clusters.

Gini Impurity

Silhouette Score

Nice work
Correct! Silhouette Score is widely used to assess how well data points have been clustered.
