//============================================================================
// Name        : dotsAndHashes.cpp
// Author      : Suryadev Ramidi
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <sstream>
#include <vector>
#include <exception>

using CharMatrix = std::vector < std::vector<char> >;
using IntMatrix = std::vector < std::vector<int> >;
using Matrix = CharMatrix;
using Marker = IntMatrix;
using Point = std::pair<int, int>;


std::string input =
		  ".............###....\n"
		  "............###.....\n"
		  "..######............\n"
		  ".......#............\n"
		  "....######..........\n"
		  "....................\n"
		  ;

/**
 *
 */
template <class T>
void print_matrix (const std::vector< std::vector<T> >& in, std::string header="")
{
	if (header.size())
		std::cout << "\n" << header << std::endl;

	for (const auto& e : in) {
		for (const auto& f : e) {
			std::cout << f;
		}

		std::cout << std::endl;
	}
}

/**
 *
 */
void print_point (const Point& pt)
{
	std::cout << "[" << pt.first << "," << pt.second << "]" << std::endl;
}

/**
 *
 */
void read_input (
		const std::string& in,
		Matrix& out
		)
{
	std::istringstream ss(in);
	std::string line;
	while (std::getline(ss, line)) {
		if (out.size() > 1) {
			if (out.back().size() != line.length()) {
				std::ostringstream emsg;
				emsg << "Invalid length at line number: " << out.size() + 1;
				throw std::runtime_error (emsg.str());
			}
		}

		out.push_back(std::vector<char>());
		for (auto c : line) {
			out.back().push_back (c);
		}
	}
}

/**
 *
 */
void get_unvisited_neigbors (
		const Point& pt,
		const Matrix& matrix,
		const Marker& marker,
		std::vector<Point>& out
		)
{
	static int delta[] = {-1, 0, 1};
	int maxX = marker.size();
	int maxY = marker[0].size();

	for (auto dx : delta) {
		for (auto dy : delta) {
			Point pt2(pt.first + dx, pt.second + dy);
			if (pt2.first >= 0 && pt2.first < maxX &&
				pt2.second >= 0 && pt2.second < maxY &&
				 matrix[pt2.first][pt2.second] == '#' &&
				!marker[pt2.first][pt2.second])
			{
				out.push_back(pt2);
			}
		}
	}
}

/**
 *
 */
void dfs (
		int x,
		int y,
		const Matrix& matrix,
		Marker& marker,
		int& count,
		std::vector<Point>& points
		)
{
	marker[x][y] = 1;
	points.push_back (Point(x, y));
	count++;

	std::vector<Point> neighbors;
	get_unvisited_neigbors (Point(x, y), matrix, marker, neighbors);

	for (const auto& pt : neighbors) {
		if (!marker[pt.first][pt.second]) {

			dfs (pt.first, pt.second, matrix, marker, count, points);
		}
	}
}

/**
 * MAIN ROUTINE
 */
int main() {

	try {


		// Read input into a matrix
		Matrix matrix;
		read_input (input, matrix);

		std::cout << "INPUT: \n" << input << std::endl;
		print_matrix(matrix, "MATRIX");

		// Build the marker matrix
		Marker marker(matrix.size());
		for (auto& x : marker) {
			x.assign (matrix[0].size(), 0);
		}

		// Run DFS
		int maxCount = 0;
		std::vector<Point> maxPoints;

		for (size_t x=0; x < matrix.size(); x++) {
			for (size_t y=0; y < matrix[0].size(); y++) {
				if (matrix[x][y] == '#' && !marker[x][y]) {
					int count = 0;
					std::vector<Point> points;
					dfs (x, y, matrix, marker, count, points);
					std::cout << "DFS[" << x << "," << y << "]" << "  --> " << count << std::endl;
					if (count > maxCount) {
						maxCount = count;
						maxPoints = points;
					}
				}
			}
		}


		// Erase maximum connected component
		std::cout << "Count:" << maxCount << std::endl;
		for (const auto& p : maxPoints) {
			matrix[p.first][p.second] = '.';
		}
		print_matrix (matrix, "MATRIX");
	}
	catch (std::exception& e) {
		std::cout << e.what() << std::endl;
		return -1;
	}


	return 0;
}
