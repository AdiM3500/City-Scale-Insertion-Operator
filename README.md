# All baseline C++ code made by Gong et. al. Repo link: https://github.com/gzyhkust/Insertion-Operator

# Guide to running code:

## Baseline:

- By default, this repo is primed for the _Cainiao dataset_.
- cd into code Directory
- make clean
- make n
- use linux command:time ./n <requests_path> <workers_path>
  - example: time ./n ../Data/Cainiao/requests_baseline.txt ../Data/Cainiao/LogisticWorkers.txt (for running the baseline insertion operator on the Cainiao requests and worker datasets)

- **If you wish to change the number of workers or requests**
  - Go to /Data/<Dataset>/requests_baseline.txt and change the top line to signify the number of requests
    - The individual request data is in the form <Requests appearance time, Start Node, End Node, Capacity, Deadline, time-dependent Shortest Path> for **Logistics** and <Request appearance time, start node, end node, capacity, time-dependent Shortest Path> for **Ridesharing**
      
  - Go to /Data/<Dataset>/LogisticWorkers.txt and change the first number in the first line (the first line signifies: NumofWorkers, Capacity of each worker, GridL (not relevant), alpha (not relevant)
    - The individual worker data is in the form <Worker Start Node, capacity (overriden by the first line)

- **If you wish to change Datasets**
  - change the 'tgraph_path' in _Constants.h_ to match the appropriate TDRN files in /Data/<Dataset>/<Dataset>_TDRN.txt.
  - change the 'vertexes_path' in _Constants.h_ to match the appropriate TDRN vertices (.co) files in /Data.
  - Build the TD-G-Tree and save it to the appropriate Dataset directory in Data (see: _ReadInput(...)_ function in _InsertionN.cpp_ to build the td-g-tree for Ridesharing datasets)
  - change the 'TDGT_tree_path' in _Constants.h_ to match the appropriate TD-G-Tree file in /Data.
  - Follow the steps above to run the code.
 
## Clustered Approach with Adaptive Allocation of workers:

### Pre-processing the data
- cd into code Directory
- run .py script: python3 cainiao_cluster.py
  -   By default this creates K = 20 clusters for splitting 12,487 requests (all requests in Cainiao requests dataset) and adaptively assigns 400 workers to the created clusters. The values of K, requests (n), and total_workers can be changed in this script
  -   These worker and request subset pairs (ordered pair denoted by their suffix) are stored in parallel_clusters_shanghai
 
### Running the executable via GNU parallel
- make clean
- make n
- move n to parallel_clusters_shanghai directory
- Within  parallel_clusters_shanghai :
  - Use GNU Parallel to run the maximum allowed number of parallel jobs (-j 0). This command will run the ordered worker-request subset pairs in parallel:
    - **time parallel -j 0 "./n requests_cluster_{}.txt LogisticWorkers_{}.txt > requests_{}.log" ::: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19**
    - The above example runs 20 jobs in parallel for 20 ordered worker-request subset pairs. You need to change the number of jobs depending on your chosen K value.
    - Once finished running you can check the number of requests served in the requests_{}.log files which will be created in parallel_clusters_shanghai directory.


 
  
