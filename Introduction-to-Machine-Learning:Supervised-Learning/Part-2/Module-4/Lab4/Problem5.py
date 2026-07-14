5. Compare Linkage Criteria (10 points)
Different linkage criteria produce different dendrograms. The three main linkage methods are:

Single linkage: Distance = minimum distance between any pair of members
Complete linkage: Distance = maximum distance between any pair of members
Average linkage: Distance = average of all pairwise distances
Compute linkage matrices for all three methods and compare the maximum merge distances.

Store the results as:

q5_linkage_single: Linkage matrix using single linkage
q5_linkage_complete: Linkage matrix using complete linkage
q5_linkage_average: Linkage matrix using average linkage
q5_max_distances: A dictionary mapping linkage name to max merge distance
# Grade Cell: Question 5
#
# Task: Compute and compare linkage matrices for different methods
#
# Instructions:
# 1. Compute linkage with method='single', 'complete', and 'average'
# 2. Extract the maximum merge distance from each (last row, column index 2)
# 3. Store in a dictionary for comparison
​
q5_linkage_single = linkage(q2_scaled_data, method="single")
q5_linkage_complete = linkage(q2_scaled_data, method="complete")
q5_linkage_average = linkage(q2_scaled_data, method="average")
​
q5_max_distances: Dict[str, float] = {
    "single": round(float(q5_linkage_single[-1, 2]), 2),
    "complete": round(float(q5_linkage_complete[-1, 2]), 2),
    "average": round(float(q5_linkage_average[-1, 2]), 2),
}
​
print("Maximum merge distances by linkage:")
for name, dist in q5_max_distances.items():
    print(f"  {name}: {dist}")
