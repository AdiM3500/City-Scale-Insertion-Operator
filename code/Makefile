#
#	Makefile 
#	Author: zy based on Trasier
##
CC = gcc
CXX = g++
#yuxiang's method
LIBS = -D HELLINGER

METIS_INCLUDE = /usr/local/include
METIS_LIB = /usr/local/lib
METISLIB = -I$(METIS_INCLUDE) -L$(METIS_LIB) -lmetis
#-L /Users/gongcengyang/Desktop/TestTDGT/metis-5.1.0/build/Darwin-x86_64/libmetis -lmetis

CFLAGS = --std=c++11 -W -Wall -Wno-sign-compare -O3 -g -pipe -march=native#-mmmx -msse -msse2 -msse3 #-mcmodel=large
MEM = -D WATCH_MEM

all: n

insertionN.o: TDGT.h io.h insertionN.h insertionN.cpp PLF.h Constants.h TGraph.h TNode.h Segment.h misc.h TMatrix.h 
	$(CXX) $(CFLAGS) -c insertionN.cpp $(LIBS)$(METISLIB)
n: mainN.cpp insertionN.h insertionN.cpp insertionN.o TDGT.h io.h PLF.h Constants.h TGraph.h TNode.h Segment.h misc.h TMatrix.h TDDijkstra.h 
	$(CXX) $(CFLAGS) -o n insertionN.o mainN.cpp $(LIBS) $(METISLIB)


.PHONY: clean
clean:
		-@rm *.o *.gcno *~ 2> /dev/null || true
		-@rm n 2> /dev/null || true
##############################################################################################################
# ##
# #	Makefile 
# #	Author: zy based on Trasier
# ##
# CC = gcc
# CXX = g++
# #yuxiang's method
# LIBS = -D HELLINGER

# METISLIB = -I /homes/zgongae/metis-5.1.0/include -L /homes/zgongae/metis-5.1.0/build/Linux-x86_64/libmetis -lmetis
# #-L /Users/gongcengyang/Desktop/TestTDGT/metis-5.1.0/build/Darwin-x86_64/libmetis -lmetis

# CFLAGS = --std=c++11 -W -Wall -Wno-sign-compare -O3 -s -pipe -mmmx -msse -msse2 -msse3 # -mcmodel=medium
# MEM = -D WATCH_MEM

# all: TDGT

# insertion.o: TDGT.h io.h insertion.h insertion.cpp PLF.h Constants.h TGraph.h TNode.h Segment.h misc.h TMatrix.h 
# 	$(CXX) $(CFLAGS) -c insertion.cpp $(LIBS)$(METISLIB)
# TDGT: main.cpp insertion.h insertion.cpp insertion.o TDGT.h io.h PLF.h Constants.h TGraph.h TNode.h Segment.h misc.h TMatrix.h TDDijkstra.h 
# 	$(CXX) $(CFLAGS) -o TDGT insertion.o main.cpp $(LIBS) $(METISLIB)


# .PHONY: clean
# clean:
# 		-@rm *.o *.gcno *~ 2> /dev/null || true
# 		-@rm TDGT 2> /dev/null || true
