#include "insertionN.h"
#include <omp.h>

int main(int argc, char **args) {

    string requests_path;
    string workers_path;

    // Check if at least two arguments are provided
    if (argc < 3) {
        cerr << "Usage: " << args[0] << " <requests_path> <workers_path>" << endl;
        return 1;
    }

    // Assign values from command-line arguments
    requests_path = args[1];  // First argument
    workers_path = args[2];   // Second argument

    // Print the received arguments
    cout << "Requests file: " << requests_path << endl;
    cout << "Workers file: " << workers_path << endl;

    // Process input files
    readInput(requests_path, workers_path);
    initGrid();

		
	cout << "Start sharing..." << endl;
	clock_t tbegin = clock();
  	timeDependentInsertion();

	clock_t tend = clock();
	cout << "Finish sharing \t time cost: " + to_string((tend - tbegin) / CLOCKS_PER_SEC) + "s" << endl;
	
	ofstream of("./data/sharingn.txt");
	of << (tend - tbegin) / CLOCKS_PER_SEC << "\n";
	//recordTrajectory();
	freeMemory();
	
}