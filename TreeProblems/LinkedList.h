/*
 * LinkedList.h
 *
 *  Created on: Apr 19, 2017
 *      Author: macbook
 */

#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

#include <iostream>
using namespace std;



class LinkedList {

public:

	struct Node {
		int d;
		Node* next;

		Node(int d) {
			this->d = d;
			next = nullptr;
		}
	};

	LinkedList();

	LinkedList(const initializer_list<int>& il) {
		for (auto x : il) {
			this->push_back(x);
		}
	}

	virtual ~LinkedList() {
		Node* nd = root;
		Node* temp;
		cout << "Deleting: ";
		while (nd) {
			temp = nd->next;
			cout << nd->d << " ";
			delete nd;
			nd = temp;
		}
		cout << endl;

		root = nullptr;
	}

	LinkedList& push_back(int d) {
		Node* nd = new Node(d);
		if (root == nullptr) {
			root = nd;
		}
		else
			tail->next = nd;

		tail = nd;

		return *this;
	}


	bool isEmpty() const {
		return (root ? false : true );
	}

	static void test();


	// Data
	Node* root  = nullptr;
	Node* tail = nullptr;

};

inline ostream& operator << (ostream& os, const LinkedList& ll) {

	os << "\nLinkedList: ";

	LinkedList::Node* nd = ll.root;
	while (nd) {
		os << nd->d << " ";
		nd = nd->next;
	}

	os << endl;

	return os;
}

#endif /* LINKEDLIST_H_ */
