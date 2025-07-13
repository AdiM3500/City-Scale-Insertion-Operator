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

- **If you wish to change Datasets **
  - change the 'tgraph_path' in _Constants.h_ to match the appropriate TDRN files in /Data/<Dataset>/<Dataset>_TDRN.txt.
  - change the 'vertexes_path' in _Constants.h_ to match the appropriate TDRN vertices (.co) files in /Data.
  - Build the TD-G-Tree and save it to the appropriate Dataset directory in Data (see: _ReadInput(...)_ function in _InsertionN.cpp_ to build the td-g-tree for Ridesharing datasets)
  - change the 'TDGT_tree_path' in _Constants.h_ to match the appropriate TD-G-Tree file in /Data.
  - Follow the steps above to run the code.


 
  
