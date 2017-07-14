/*
 * main.cpp
 *
 *  Created on: Apr 9, 2017
 *      Author: macbook
 */


#include <iostream>
#include <sstream>
#include <vector>
#include <thread>
#include <set>
#include "LinkedList.h"
#include "BinaryTree.h"

using namespace std;

/**
 *
 * A B C D
 * E F G H
 * I J K L
 * M N O P
 *
 * Rotate 90 degrees
 * M I E A
 * N J F B
 * O K G C
 * P L H D
 *
 * 0,3 -> 3,0
 * 3,0 -> 3,3
 * 3,3 -> 3,0
 * 3,0 -> 0,3
 *
 * rotate(x, y, len):
 *   z = x + len-1
 *   m[x][z] = m[x][y]
 *
 *
 *  1 1 1 1       1 0 1 1
 *  1 0 1 1  =>   0 0 0 0
 *  1 1 1 1       1 0 1 1
 *  1 1 1 1       1 0 1 1
 *
 *  1,1 -> 0,1  1,0  1,2  1,3
 *         2,1  3,1
 *
 *  1 1 1 1       1 1 0 1
 *  1 1 0 1  =>   0 0 0 0
 *  1 1 1 1       1 1 0 1
 *  1 1 1 1       1 1 0 1
 *
 *  1,2  i==1 or j==2
 *
 *  	thread dummyThread(threadFunc);
	dummyThread.join();
 */


using CharMatrix = vector < vector<char> >;

string input =
		"1 1 1 1\n"
		"1 1 0 1\n"
	    "1 1 1 1\n"
		"1 1 1 1\n"
		;

/**
 *
 */
template <class T>
void print_matrix (
		const vector< vector<T> >& in,
		string header=""
		)
{
	if (header.size())
		cout << "\n" << header << endl;

	for (const auto& e : in) {
		for (const auto& f : e) {
			cout << f;
		}

		cout << endl;
	}
}

void read_input (const string& in, CharMatrix& out)
{
	istringstream ss(in);
	string line;
	while (getline(ss, line)) {
		if (out.size() > 1) {
			if (out.back().size() != line.length()) {
				ostringstream emsg;
				emsg << "Invalid length at line number: " << out.size() + 1;
				throw runtime_error (emsg.str());
			}
		}

		out.push_back(vector<char>());
		for (auto c : line) {
			if (c == ' ')
				continue;

			out.back().push_back (c);
		}
	}
}

void threadFunc()
{
	cout << "Welcome to Multithreading" << endl;
}


//6 7 1 2 3 4 5
//l     m     h
//6 9 10 1 2
//l    m   h
int find_rotated(vector<int>& A, int x, int l, int h)
{
	int m = (l + h) / 2;

	if (x == A[m])
		return m;

	// Increasing range
	if (A[m] < A[h]) {
		if (x >= A[m] && x <= A[h])
			l = m;
		else
			h = m-1;
	}
	else { // Decreasing Range
		if (x >= A[m] || x <= A[h])
			l = m;
		else
			h = m-1;
	}
}


void printPar (int l, int r, char* out, int count)
{
	if (l < 0 || r < l)
		return;

	if (l==0 && r==0)
		cout << out << endl;
	else {
		if (l > 0) {
			out[count] = '(';
			printPar(l-1, r, out, count+1);
		}
		if (r > l) {
			out[count] = ')';
			printPar(l, r-1, out, count+1);
		}
	}
}
int main()
{
	const int LEN = 3;

	char parens[2 * LEN];
	printPar(LEN, LEN, parens, 0);
//	LinkedList::test();
	//BinaryTree::test();

	/*int mat[4][4] = { {1,1,1,1}, {1,1,1,1}, {1,1,1,1}, {0,1,1,1} };

	set<int> ix, iy;

	for (const auto& line : mat) {
		for (auto x : line)
			cout << " " << x;

		cout << std::endl;
	}

	for (int i=0; i < 4; i++) {
		for (int j=0; j < 4; j++) {
			if (mat[i][j] == 0) {
				ix.insert(i);
				iy.insert(j);
			}
		}
	}
	for (int i=0; i < 4; i++) {
		for (int j=0; j < 4; j++) {
			if (ix.count(i) || iy.count(j))
				mat[i][j] = 0;
		}
	}


	cout << "\nOUTPUT" << std::endl;
	for (const auto& line : mat) {
		for (auto x : line)
			cout << " " << x;

		cout << std::endl;
	}
*/
	auto x = 10;
	cin >> x;

}

