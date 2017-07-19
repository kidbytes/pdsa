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



class Trie {

	struct Node {
		char c;
		map<char, Node*> childs;
		bool isWord;

		Node(char c = '*') {
			isWord = false;
			this->c = c;
		}
	};

public:
	Trie() {
		root = new Node();
	}

	void add(const string& name) {
		Node* curr = root;
		for (char c : name) {
			if (curr->childs.count(c) == 0) {
				Node* ptr = new Node(c);
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
		Node* nPtr = nullptr;

		que.push(curr);
		while(que.size() > 0) {
			nPtr = que.front();
			que.pop();
			if (nPtr->isWord)
				count++;

			for (auto& x : nPtr->childs) {
				que.push(x.second);
			}
		}

		return count;
	}

	void printWords() {
		string prefix;
		printWords(root, prefix);
	}
	void printWords(Node* nPtr, string& prefix) {
		if (!nPtr)
			return;

		if (nPtr != root)
			prefix.push_back(nPtr->c);

		if (nPtr->isWord)
			cout << prefix << endl;

		for (auto& x : nPtr->childs) {
			printWords(x.second, prefix);
		}

		prefix.pop_back();
	}

	static void run() {
	    int n;
	    cin >> n;

	    Trie trie;
	    for(int a0 = 0; a0 < n; a0++){
	        string op;
	        string contact;
	        cin >> op >> contact;

	        if (op == "add")
	            trie.add(contact);
	        else
	            cout << trie.find(contact) << endl;
	    }

	    trie.printWords();
	}

private:
	Node* root;
};



