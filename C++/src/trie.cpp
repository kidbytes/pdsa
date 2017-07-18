/*
 * trie.cpp
 *
 *  Created on: Jul 17, 2017
 *      Author: surya
 */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
#include <string>

using namespace std;

struct Node {
	char c;
	map<char, Node*> childs;
	bool isWord;

	Node() {
		isWord = false;
		c = ' ';
	}
};

class Trie {

public:
	Trie() {
		root = new Node();
	}

	void add(const string& name) {
		Node* curr = root;
		for (char c : name) {
			if (curr->childs.count(c) == 0) {
				Node* ptr = new Node();
				curr->childs[c] = ptr;
			}
			curr = curr->childs[c];
		}
		curr->isWord = true;
	}

	int find(const string& partial) {
		Node* curr = root;
		for (char c : partial) {
			if (curr->childs.count(c) == 0 )
				return 0;

			curr = curr->childs[c];
		}

		int count = 0;
		queue<Node*> que;
		Node* ndPtr = nullptr;

		que.push(curr);
		while(que.size() > 0) {
			ndPtr = que.front();
			que.pop();
			if (ndPtr->isWord)
				count++;

			for (auto& x : ndPtr->childs) {
				que.push(x.second);
			}
		}

		return count;
	}

private:
	Node* root;
};


void read_input() {
    int n;
    cin >> n;
    for(int a0 = 0; a0 < n; a0++){
        string op;
        string contact;
        cin >> op >> contact;

        Trie trie;
        if (op == "add")
            trie.add(contact);
        else
            cout << trie.find(contact) << endl;
    }
}
