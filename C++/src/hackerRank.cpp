/*
 * hackerRank.cpp
 *
 *  Created on: Jun 19, 2017
 *      Author: surya
 */
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

//4
//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
//Expected Output: Yes
struct Node {
   int data;
   Node* left;
   Node* right;
};

bool checkBST(Node* root) {

    if (!root)
        return true;

    if (!checkBST(root->left) || !checkBST(root->right))
        return false;

    if (root->left && root->data < root->left->data)
        return false;

    if (root->right && root->data > root->right->data)
        return false;

     return true;

}

int number_needed(string a, string b) {
    unordered_map<char, int> um1, um2;
    for (char c : a) {
        if (um1.count(c)) {
            um1[c]++;
        } else {
            um1[c] = 1;
        }
    }

    for (char c : b) {
        if (um2.count(c)) {
            um2[c]++;
        } else {
            um2[c] = 1;
        }
    }

    int deletes = 0;
    for (const auto& e : um1) {
    	const auto it = um2.find(e.first);
    	if (it != um2.end())
    		deletes += abs(e.second - it->second);
    	else
    		deletes += e.second;
    }

    for (const auto& e : um2) {
    	const auto it = um1.find(e.first);
    	if (it == um1.end())
    		deletes += e.second;
    }

    return deletes;
}




//---------------------------+
// Matching Braces           |
//---------------------------+
bool is_left_brace(char c) {
    if (c == '[' || c == '{' || c == '(')
        return true;
    else
        return false;
}

bool is_right_brace(char c) {
    if (c == ']' || c == '}' || c == ')')
        return true;
    else
        return false;
}

bool is_matching_brace(char left, char right)
{
    if (!is_left_brace(left))
        return false;

    if (!is_right_brace(right))
        return false;

    if (left == '[' && right != ']')
        return false;

    if (left == '{' && right != '}')
        return false;

    if (left == '(' && right != ')') {

        return false;
    }

    return true;
}

bool is_balanced(string expression) {
    stack<char> stk;

    for (auto c : expression) {
        if (is_left_brace(c)) {
        	cout << "\npushing " << c;
            stk.push(c);
        }
        else {
            char d = stk.top();
            stk.pop();
            cout << "\npopped " << d << endl;
            if (!is_matching_brace(c,d))
                return false;
        }
    }

    if (stk.size())
        return false;

    return true;
}

//int main(){
////    string a;
////    cin >> a;
////    string b;
////    cin >> b;
////    cout << number_needed(a, b) << endl;
//
//	Graph graph(5);
//	graph.read_input();
////	cout << is_balanced("()");
//    return 0;
//}



