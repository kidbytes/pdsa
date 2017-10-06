#include "shortestPath.h"
#include <queue>
#include <set>
#include <cmath>


int Graph::read_input() {
    int queries;
    cin >> queries;

    for (int t = 0; t < queries; t++) {

      int n, m;
        cin >> n;
        // Create a graph of size n where each edge weight is 6:
        Graph graph(n);
        cin >> m;
        // read and set edges
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            u--, v--;
            // add each edge to the graph
            graph.add_edge(u, v);
        }
      int startId;
        cin >> startId;
        startId--;
        // Find shortest reach from node s
        vector<int> distances = graph.shortest_reach(startId);

        for (int i = 0; i < distances.size(); i++) {
            if (i != startId) {
                cout << distances[i] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}


vector<int>
Graph::shortest_reach(int start) {
	vector<int> ret(m_2d.size(), -1);

	ret[start] = 0;
	set<int> solnSet;
	set<Node> neighborSet;

	neighborSet.insert(Node(start, start, 0));

	const int dist = 6;
	int prev = start;

	while (neighborSet.size() > 0) {
		int top = *(neighborSet.begin());

		solnSet.insert(top);

		for (auto n : m_2d[top]) {
			if (solnSet.count(n) > 0)
				continue;

			if (ret[n] == -1) {
				ret[n] = ret[top] + 6;
			} else {
				ret[n] = min(ret[n], ret[top] + 6);
			}
		}

		neighborSet.erase(neighborSet.begin());

	}

	solnSet.insert(start);

	auto& neighbors = m_2d[start];
	for (auto n : neighbors) {

	}


	queue<int> que;
	que.push(start);
	int depth = 0;
	int sz = 1;

	while (que.size()) {
		for (int i=0; i < sz; i++) {
			int top = que.front();
			que.pop();
			m_1d[top] = depth;

			depth += 6;
			for (int j=0; j<m_n; j++) {
				if (m_2d[top][j] > 0) {
					if (m_1d[j] != -1 && m_1d[j] > depth)
						que.push(j);
				}
			}

			sz = que.size();
		}

	}
	return ret;
}
