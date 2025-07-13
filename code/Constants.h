#ifndef TDGT_CONSTANTS_H
#define TDGT_CONSTANTS_H

#include <string>
#include <map>
#include <iostream>
#include <array>
#include <limits>
#include <cmath>
#include <cassert>


#define DE_INTV -2147483648 
#define INTV_CNTED -2147483647
#define DE_W 2147483647


static double EPSILON = 1e-5; //1/86400 =1.157e-5

static int TMAX = 86400;
//static int TMAX = 8640000;

// hyper parameters
static unsigned long LEAF_SIZE = 64; //64
static unsigned long FANOUT = 4; //4

static int delta = 1.2;
static double deltasecond = 50000;
static double MAX_speed = 26;
static double grid_value = 1000;
static double len = 600;
////////////////////////////////////////////////////////////////

//Haikou and Chengdu TDRNs (for Ridesharing Data)
//const std::string tgraph_path = "../Data/Haikou/haikou_TDRN.txt";
//const std::string tgraph_path = "../Data/Chengdu/Chengdu_TDRN.txt";

//Shanghai TDRN (for Logistics Data)
const std::string tgraph_path = "../Data/Cainiao/Shanghai_TDRN.txt";

//Not relevant for Insertion Operator algorithm//
const std::string tdgt_idx_path = "../Data/CAL.idx";
const std::string tdsp_query_path = "../Data/CALTDSP.demands";
const std::string tisp_query_path = "../Data/CALTISP.demands";
////////////////////////////////////////////////////////////////


//Shanghai Vertices
const std::string vertexes_path = "../Data/Cainiao/vertices.txt";

//Ridesharing Vertices (Chengdu and Haikou)
//const std::string vertexes_path = "../Data/Chengdu/Chengdu.co";
//const std::string vertexes_path ="../Data/Haikou/Haikou.co";

//TD-G-Tree Paths:
//Ridesharing:
//const std::string TDGT_tree_path = "/home/aadityamukherjee/Desktop/Insertion-Operator/haikou_tdgt.txt";
//const std::string TDGT_tree_path = "/home/aadityamukherjee/Desktop/Insertion-Operator/chengdu_decimal_tdgt_128.txt";

//Logistics:
const std::string TDGT_tree_path = "../Data/Cainiao/cainiao_tdgt.txt";

//Not relevant parameters//
const std::string dump_resultn3_path = "./data/dumpResultsn3.txt";
const std::string trajectory_n3_path = "./data/trajectoryn3.txt";

const std::string dump_resultn2_path = "./data/dumpResultsn2.txt";
const std::string trajectory_n2_path = "./data/trajectoryn2.txt";

const std::string dump_resultn_path = "./data/dumpResultsn.txt";
const std::string trajectory_n_path = "./data/trajectoryn.txt";

const std::string insertion_log_n = "./data/logn.txt";
const std::string insertion_log_n2 = "./data/logn2.txt";
const std::string insertion_log_n3 = "./data/logn3.txt";

#endif //TDGT_CONSTANTS_H
