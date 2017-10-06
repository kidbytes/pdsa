/*
 * shortestPath.h
 *
 *  Created on: Jul 11, 2017
 *      Author: surya
 */

#ifndef SHORTESTPATH_H_
#define SHORTESTPATH_H_

#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;

using TwoD = vector< vector<int> >;

class Graph {

	class Node {
		int node;
		int parent;
		int dist;

		Node(int id, int parent_id, int dist) {
			node = id;
			parent = parent_id;
			this->dist = dist;
		}

		bool operator < (const Node& rhs) {
			return (this->dist <= rhs.dist);
		}
	};

    public:
        Graph(int n) {
        	m_2d.reserve(n);
        }

        void add_edge(int u, int v) {
        	m_2d[u].push_back(v);
        	m_2d[v].push_back(u);
        }

        vector<int> shortest_reach(int start);
        int read_input();

    private:
        TwoD m_2d;

};



#endif /* SHORTESTPATH_H_ */
