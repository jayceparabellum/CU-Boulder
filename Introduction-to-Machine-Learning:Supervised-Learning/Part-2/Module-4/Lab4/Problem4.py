4. Visualize Dendrogram (10 points)
A dendrogram is a tree diagram that visualizes the hierarchical clustering process. The y-axis shows the distance (dissimilarity) at which clusters merge. Observations are shown at the bottom, and merges are shown as horizontal lines connecting branches.

Create a dendrogram using scipy's dendrogram() function.

Store the results as:

q4_dendrogram: The dictionary returned by scipy's dendrogram() function
q4_n_leaves: The number of leaves in the dendrogram (should equal n_samples)
q4_plot_created: Set to True after creating the dendrogram plot
# Grade Cell: Question 4
#
# Task: Create and visualize a dendrogram
#
# Instructions:
# 1. Create a figure with appropriate size
# 2. Use scipy.cluster.hierarchy.dendrogram() with the linkage matrix
# 3. Add labels and title
# 4. The dendrogram() function returns a dictionary with information about the tree
​
plt.figure(figsize=(14, 7))
​
q4_dendrogram = dendrogram(
    q3_linkage_matrix,
    leaf_rotation=90,
    leaf_font_size=6,
)
​
plt.title("Hierarchical Clustering Dendrogram (Complete Linkage)")
plt.xlabel("Sample index")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()
​
q4_n_leaves: int = len(q4_dendrogram["ivl"])
​
q4_plot_created: bool = True
​
print(f"Number of leaves in dendrogram: {q4_n_leaves}")
print(f"Dendrogram keys: {list(q4_dendrogram.keys())}"):
