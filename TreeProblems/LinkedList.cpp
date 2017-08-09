/*
 * LinkedList.cpp
 *
 *  Created on: Apr 19, 2017
 *      Author: macbook
 */

#include "LinkedList.h"
using Node = LinkedList::Node;

Node* find_nth_from_last(const LinkedList& ll, int n) {

	cout << "\n" << n << " from last: ";

	Node* curr, *prev;
	curr = prev = ll.root;
	int count = 0;

	while (curr && count < n) {
		curr = curr->next;
		count++;
	}

	if (!curr) {
		cout << "nullptr";
		return nullptr;
	}

	while (curr->next) {
		prev = prev->next;
		curr = curr->next;
	}

	cout << prev->d;
	return prev;
}


void LinkedList::test() {

	LinkedList ll = { 1, 2, 3 ,4, 5};
	find_nth_from_last(ll, 0);
	find_nth_from_last(ll, 4);
	find_nth_from_last(ll, 5);


	cout << ll;
}
