
import os
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import folium

# --------------------------------------------------
# 1) LOAD DATA
# --------------------------------------------------

# Path to coordinates file
coordinates_file_path = '../Data/Haikou/Haikou.co'

# Load the coordinates (Lat, Lon)
coordinates = pd.read_csv(coordinates_file_path, header=None, names=['Latitude', 'Longitude'], sep='\s+')
# Filter out invalid rows
coordinates = coordinates[coordinates['Latitude'] != 45948]
coordinates = coordinates.dropna()

# Number of rows to read
n = 40000

# Path to requests file
requests_file_path = '../Data/Haikou/Haikou_Order_Clustering.txt'
# Load only first n rows
requests = pd.read_csv(
    requests_file_path, 
    delim_whitespace=True, 
    header=None, 
    names=['Time', 'StartNode', 'EndNode', 'Capacity','tdsp'], 
    nrows=n
)

starting_nodes = requests['EndNode']
starting_coords = coordinates.iloc[starting_nodes].reset_index(drop=True)


# --------------------------------------------------
# 2) APPLY K-MEANS ON THE `tdsp` COLUMN
# --------------------------------------------------

k = 8  # Number of clusters (adjust as needed)
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)

# Fit KMeans to the raw `tdsp` values
requests['Cluster'] = kmeans.fit_predict(requests[['tdsp']])
#requests['Cluster'] = kmeans.fit_predict(starting_coords[['Latitude', 'Longitude']])

# --------------------------------------------------
# 3) CALCULATE INVERSELY PROPORTIONAL WORKER DISTRIBUTION BASED ON AVERAGE `tdsp` PER REQUEST
# --------------------------------------------------

total_workers = 200  # Total available workers

# Step 1: Calculate total requests and total `tdsp` per cluster
cluster_request_counts = requests['Cluster'].value_counts().sort_index()
cluster_tdsp_sums = requests.groupby('Cluster')['tdsp'].sum().sort_index()

# Step 2: Compute **average tdsp per request** for each cluster
avg_tdsp_per_request = cluster_tdsp_sums / cluster_request_counts  # total tdsp / total requests

# Step 3: Compute **inverse proportions** (clusters with lower avg `tdsp` get more workers)
inverse_avg_tdsp = (1 / avg_tdsp_per_request) / (1 / avg_tdsp_per_request).sum()

# Step 4: Assign workers proportionally (rounding properly)
worker_allocations = np.round(inverse_avg_tdsp * total_workers).astype(int)

# Step 5: Adjust rounding to ensure exactly `total_workers` workers are assigned
while worker_allocations.sum() != total_workers:
    diff = total_workers - worker_allocations.sum()  # Compute adjustment needed
    if diff > 0:
        worker_allocations[np.argmax(inverse_avg_tdsp)] += 1  # Add worker to the best cluster
    else:
        worker_allocations[np.argmax(worker_allocations)] -= 1  # Remove from the largest assigned cluster

# --------------------------------------------------
# 4) SAVE CLUSTER FILES & PRINT WORKER DISTRIBUTION (SORTED)
# --------------------------------------------------

# Directory to save files
output_directory = "../parallel_clusters_haikou"

# Read the original workers file
workers_file_path = '../Data/Cainiao/LogisticWorkers.txt'
with open(workers_file_path, "r") as f:
    worker_lines = f.readlines()

# Extract first line details from the original workers file
first_line_parts = worker_lines[0].strip().split()
original_capacity = first_line_parts[1]  # Capacity of workers remains unchanged
gridL = first_line_parts[2]  # GridL remains unchanged
alpha = first_line_parts[3]  # Alpha remains unchanged

print("\nCluster Requests, Avg tdsp per Request & Worker Distribution (Inverse Proportions):")
print(f"{'Cluster':<10} {'Requests':<15} {'Total tdsp':<20} {'Avg tdsp':<15} {'Workers'}")
print("=" * 75)

for cluster_id in sorted(requests['Cluster'].unique()):
    # Filter requests for this cluster
    cluster_requests = requests[requests['Cluster'] == cluster_id]

    # Get total requests, total tdsp, and avg tdsp per request
    num_requests = cluster_request_counts[cluster_id]
    total_tdsp_cluster = cluster_tdsp_sums[cluster_id]
    avg_tdsp = avg_tdsp_per_request[cluster_id]
    workers = worker_allocations[cluster_id]

    # Save to request cluster file **with number of requests at the top**
    cluster_file = os.path.join(output_directory, f"requests_cluster_{cluster_id}.txt")
    with open(cluster_file, "w") as f:
        f.write(f"{num_requests}\n")  # Write only the number of requests
        cluster_requests.drop(columns=['Cluster']).to_csv(f, index=False, sep=' ', header=False)

    # Save to LogisticWorkers_k.txt file **with updated worker count**
    logistic_worker_file = os.path.join(output_directory, f"LogisticWorkers_{cluster_id}.txt")
    with open(logistic_worker_file, "w") as f:
        f.write(f"{workers} {original_capacity} {gridL} {alpha}\n")  # Update worker count in first line
        f.writelines(worker_lines[1:])  # Keep other worker details unchanged

    # Print worker allocation (sorted by cluster)
    print(f"{cluster_id:<10} {num_requests:<15} {total_tdsp_cluster:<20} {avg_tdsp:<15.2f} {workers}")

print("\nAll LogisticWorkers_k.txt files have been generated successfully.")

