/*
 * BinaryTree.h
 *
 *  Created on: Apr 21, 2017
 *      Author: macbook
 */

#ifndef TREEPROBLEMS_BINARYTREE_H_
#define TREEPROBLEMS_BINARYTREE_H_

#include <iostream>
#include <utility>
using namespace std;

#define SPACE  " ";


class BinaryTree {
public:

	struct Node {
		int d;
		Node* left;
		Node* right;
		Node* sibling;

		Node(int d) {
			this->d = d;
			left = right = sibling = nullptr;
		}
	};

	BinaryTree();
	BinaryTree (const initializer_list<int>& il);
	virtual ~BinaryTree();

	void visitInorder(Node* nd);
	void setSibling();

	static void bfsPrint(Node* nd);
	static Node* insert(int l, Node* nd);
	static Node* insert(Node* nd, int r);
	static pair<Node*, Node*> insert(int l, Node* nd, int r);


	static pair<Node*, Node*> insert(Node* nd, int* left, int* right);
	static bool treeMatch(const Node* lhs, const Node* rhs);
	static bool subTreeFind(const Node* parent, const Node* child);
	static void test();

	//Data
	Node* root = nullptr;

private:
	Node* buildBST(
			const vector<int>& in,
			size_t start,
			size_t end
			);
};

#endif /* TREEPROBLEMS_BINARYTREE_H_ */
