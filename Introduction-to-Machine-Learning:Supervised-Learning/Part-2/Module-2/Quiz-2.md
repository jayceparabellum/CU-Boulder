
Question 1
What is the primary goal of clustering in unsupervised learning?

To classify data into predefined categories.

To reduce the dimensionality of the dataset.

To group similar data points together based on certain features.

To predict future data trends.

Nice work
Correct! Clustering aims to group similar data points together based on the data's features.

1 / 1 point


2.
Question 2
What distinguishes unsupervised learning from supervised learning?

Unsupervised learning requires large training datasets with labels.

Unsupervised learning focuses on finding hidden patterns without guidance.

Unsupervised learning always provides a clear output.

Unsupervised learning uses labeled data while supervised learning does not.

Nice work
Correct! Unsupervised learning finds hidden patterns in data without any provided guidance.

1 / 1 point


3.
Question 3
Which of the following interpretations can be made from PCA results on a wine dataset? Select all that apply.

Visualizing the overall taste profile of wines.

Nice work
Great! PCA can facilitate the visualization of complex data like taste profiles.

Clustering wines based on similar characteristics without predefined categories.

Nice work
Yes, PCA can assist in grouping wines based on similarities, enhancing understanding of wine profiles.

Determining the exact age of each wine sample.

Identifying which chemical compounds contribute most to the variation among wines.

Nice work
Correct! PCA helps identify key compounds driving differences in wine characteristics.

Predicting future wine production quantities.

1 / 1 point


4.
Question 4
How can loadings derived from PCA help in understanding the data structure?

They indicate the correlation of each variable with the principal components.

They represent the variance of each variable in the dataset.

They measure the accuracy of the PCA model.

They provide the mean values of each variable in the dataset.

Nice work
Well done! Loadings show how strongly each variable influences the principal components.

1 / 1 point


5.
Question 5
Which mathematical technique is applied first in the PCA process to reduce dimensionality?

Rotation of components.

Calculating the covariance matrix.

Computing eigenvectors.

Standardization of data.

Nice work
Correct! Standardizing data is often the initial step before applying PCA.

1 / 1 point


6.
Question 6
What is the role of matrix multiplication in PCA?

It multiplies data points by their means to achieve centering.

It reduces the dimensionality of data by eliminating zero eigenvalues.

It is used in the computation of the covariance matrix, which is central to PCA.

It directly aligns data points to the origin of the new coordinate system.

Nice work
That's correct! Matrix multiplication is key in calculating the covariance matrix for PCA.

1 / 1 point


7.
Question 7
Which of the following are common algorithms used for clustering in unsupervised learning? Select all that apply.

Principal Component Analysis (PCA)

Hierarchical Clustering

Nice work
Correct! Hierarchical Clustering is a method used for clustering data.

K-Means

Nice work
Correct! K-Means is a widely used clustering algorithm.

Linear Regression

1 / 1 point


8.
Question 8
In the context of unsupervised learning, what does the term 'centroid' refer to?

The mean position of all the points in a cluster.

The initial data point chosen for clustering.

The point with the highest density in a cluster.

The boundary line separating two clusters.

Nice work
Correct! The centroid is the mean position of all the points within a cluster.

1 / 1 point


9.
Question 9
Select the steps involved in projecting data points onto principal components in PCA. Select all that apply.

Multiply data by the highest eigenvalue.

Center the data by subtracting the mean.

Nice work
Correct! Centering the data is a crucial initial step in PCA.

Sort eigenvectors by eigenvalues in descending order.

Determine the eigenvectors of the covariance matrix.

Nice work
Correct! Eigenvectors of the covariance matrix are used to determine the principal components.

Divide the data by the standard deviation.

This should not be selected
Incorrect. Dividing by the standard deviation is not typically a part of the PCA projection process.

0.6 / 1 point


10.
Question 10
Which of the following steps are involved in computing Principal Component Analysis (PCA)? Select all that apply.


Calculating the covariance matrix.

Nice work
Correct, calculating the covariance matrix helps in understanding the relationships between features.

Standardizing the data.

Nice work
Yes, standardizing the data is an important step to ensure each feature contributes equally to the analysis.

Applying logistic regression.

Executing the k-means clustering algorithm.

Finding eigenvalues and eigenvectors.

Nice work
That's right! Eigenvalues and eigenvectors are essential to determine the principal components.

1 / 1 point










1.
Question 1
What is the mathematical foundation of Principal Component Analysis (PCA)?

It applies random forest algorithms to determine feature importance.

It utilizes linear regression to model relationships between variables.

It is based on the eigen decomposition of the covariance matrix.

It uses decision trees to classify data points into clusters.

Nice work
Correct! PCA relies on eigen decomposition to identify principal components from the covariance matrix.

1 / 1 point


2.
Question 2
In hierarchical clustering, what is the primary purpose of a dendrogram?

To evaluate the accuracy of the clustering model.

To visually represent the arrangement of the clustered data points over various scales.

To improve the speed of convergence in clustering algorithms.

To predict the class labels of new data points.

Nice work
Excellent! A dendrogram is a tree-like diagram that shows the arrangement and relationships among different clusters.

1 / 1 point


3.
Question 3
Identify the correct statements about PCA and variance relationship. Select all that apply.

PCA uses variance to determine the significance of each principal component.

Nice work
Great job! Variance helps PCA decide which components carry the most information.

PCA aligns data along directions of maximum variance.

Nice work
Correct! PCA's goal is to maximize variance in the projection directions.

PCA seeks to minimize variance in the data.

PCA assigns zero variance to irrelevant data points.

1 / 1 point


4.
Question 4
How does Multidimensional Scaling (MDS) represent data?

By maximizing the separation between different classes of data.

By preserving the original distances between points as closely as possible.

By transforming data into a set of orthogonal vectors.

By clustering similar data points together.

Nice work
Correct! MDS aims to preserve the distances between points when representing data in lower dimensions.

1 / 1 point


5.
Question 5
Which of the following statements are true about the application of T-SNE and UMAP for dimensionality reduction? Select all that apply.

T-SNE is faster than PCA in processing large datasets.

T-SNE is particularly effective for embedding high-dimensional data into two or three dimensions.

Nice work
Correct! T-SNE is widely used for this purpose due to its efficiency in capturing local structures.

Both T-SNE and UMAP use linear transformations for dimensionality reduction.

UMAP preserves more of the global structure of data compared to T-SNE.

Nice work
Well done! UMAP is known for preserving more global data structures than T-SNE.

1 / 1 point


6.
Question 6
Which of the following techniques are considered dimensionality reduction methods? Select all that apply.

Principal Component Analysis (PCA)

Nice work
Correct! PCA is a widely-used technique for reducing the dimensionality of data.

Linear Regression

K-Means Clustering

Uniform Manifold Approximation and Projection (UMAP)

Nice work
Correct! UMAP is used for dimensionality reduction, particularly in visualization.

t-Distributed Stochastic Neighbor Embedding (t-SNE)

Nice work
Correct! t-SNE is commonly used for visualizing high-dimensional data.

1 / 1 point



7.
Question 7
Identify the key outcomes of performing PCA on a dataset of wine characteristics. Select all that apply.

Improvement of model prediction accuracy by including all components.

Reduction of dimensionality while retaining essential information.

Nice work
Yes! PCA aims to simplify the data with minimal loss of important details.

Automatic detection of anomalies in the dataset.

Reconstruction of the original dataset with minor errors using principal components.

Nice work
Great! PCA allows for dataset reconstruction with some loss of detail.

1 / 1 point
8.
Question 8
What is the primary purpose of using Singular Value Decomposition (SVD) in Principal Component Analysis (PCA)?

To reduce the dimensionality of the dataset while preserving its variance.

To increase the number of dimensions for detailed analysis.

To compute the inverse of a data matrix for analysis purposes.

To eliminate the need for data normalization in PCA.

Nice work
Correct! SVD helps in dimensionality reduction by finding the directions (principal components) that maximize variance.

1 / 1 point


9.
Question 9
Select the statements that accurately describe the process of Singular Value Decomposition (SVD) in the context of PCA. Select all that apply.

SVD is used to normalize the data before PCA.

SVD can aid in compressing data without significant loss of information.

Nice work
Good choice! Data compression is one of the applications of SVD.

SVD is exclusively used to determine the number of principal components.

SVD directly provides the final PCA result without further computation.

SVD decomposes the original data matrix into singular vectors and singular values.

Nice work
Nicely done! SVD is essential for identifying the structure of the data matrix.

1 / 1 point


10.
Question 10
What is a primary limitation of Principal Component Analysis (PCA) in dimensionality reduction?

PCA requires labeled data for training.

PCA is unable to handle large datasets.

PCA increases the dimensionality of data.

PCA assumes linear relationships among variables.

Nice work
Correct! PCA assumes linear relationships which can limit its effectiveness in capturing complex patterns.

1 / 1 point
