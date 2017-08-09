/*
 * BinaryTree.cpp
 *
 *  Created on: Apr 21, 2017
 *      Author: macbook
 */

#include "BinaryTree.h"
#include <vector>
#include <list>
#include <deque>

using Node = BinaryTree::Node;

BinaryTree::BinaryTree() {
	// TODO Auto-generated constructor stub

}


BinaryTree::BinaryTree (const initializer_list<int>& il)
{
	vector<int> temp(il);
	root = buildBST(temp, 0, temp.size());
	BinaryTree::bfsPrint(root);
}

BinaryTree::~BinaryTree() {
	cout << "dtr:";
	visitInorder(root);
}

Node* BinaryTree::buildBST(
		const vector<int>& in,
		size_t start,
		size_t end
		)
{

	if (end <= start)
		return nullptr;

	size_t mid = start + (end - start) / 2;
	Node* newNode = new Node(in[mid]);
	newNode->left = buildBST(in, start, mid);
	newNode->right = buildBST(in, mid+1, end);

	return newNode;
}


Node* BinaryTree::insert(int l, Node* nd) {
	nd->left = new Node(l);
	return nd->left;
}

Node* BinaryTree::insert(Node* nd, int r) {
	nd->right = new Node(r);
	return nd->right;
}


pair<Node*, Node*>
BinaryTree::insert(int l, Node* nd, int r) {
	pair<Node*, Node*> ret;

	ret.first = BinaryTree::insert(l, nd);
	ret.second = BinaryTree::insert(nd, r);

	return ret;
}

pair<Node*, Node*>
BinaryTree::insert(Node* nd, int* left, int* right) {
	pair<Node*, Node*> ret;

	if (left) {
		nd->left = new Node(*left);
		ret.first = nd->left;
	}

	if (right) {
		nd->right = new Node(*left);
		ret.second = nd->right;
	}

	return ret;
}


void BinaryTree::visitInorder(Node* nd)
{
	if (!nd)
		return;

	visitInorder(nd->left);
	cout << nd->d << SPACE;
	delete nd;
	visitInorder(nd->right);
}

void BinaryTree::setSibling() {
	deque<Node*> deq;
	deq.push_back(root);
	int sz = 1;
	Node* prev = nullptr;

	while (deq.size()) {

		while (sz) {
			Node* top = deq.front();
			deq.pop_front();
			if (prev)
				prev->sibling = top;

			prev = top;

			if (top->left)
				deq.push_back(top->left);
			if (top->right)
				deq.push_back(top->right);
			sz--;
		}

		sz = deq.size();
	}
}

void BinaryTree::bfsPrint(Node* nd)
{
	list<Node*> que;
	que.push_back(nd);
	int sz = que.size();
	Node* curr = nullptr;

	while (que.size()) {
		curr = que.front();
		que.pop_front();
		cout << curr->d << SPACE;
		sz--;

		if (curr->left)
			que.push_back(curr->left);
		if (curr->right)
			que.push_back(curr->right);

		if (sz == 0) {
			cout << endl;
			sz = que.size();
		}
	}

}

bool BinaryTree::treeMatch(
		const Node* lhs,
		const Node* rhs
		)
{
	if (lhs == rhs)
		return true;

	if (!lhs || !rhs)
		return false;

	if (lhs->d != rhs->d)
		return false;

	if (treeMatch(lhs->left, rhs->left) &&
		treeMatch(lhs->right, rhs->right))
	{
		return true;
	}

	return false;
}

bool BinaryTree::subTreeFind(
		const Node* parent,
		const Node* child
		)
{
	if (parent == child)  //both can be null
		return true;

	if (parent && !child) //okay if child is smaller
		return true;

	if (!parent && child) //not okay if parent is smaller
		return false;

	if (parent->d == child->d) {
		if (subTreeFind(parent->left, child->left) &&
			subTreeFind(parent->right, child->right))
		{
			return true;
		}
	}

	if (subTreeFind(parent->left, child) ||
		subTreeFind(parent->right, child))
	{
		return true;
	}

	return false;
}


/*
		5
	12		6
 3     8 1     7
*/
void BinaryTree::test() {

	BinaryTree one = {5};
	pair<Node*, Node*> ret;

	ret = BinaryTree::insert(12, one.root, 6);
	BinaryTree::insert(3, ret.first, 8);
	BinaryTree::insert(1, ret.second, 7);
	BinaryTree::bfsPrint(one.root);

	BinaryTree two = {6};
	BinaryTree::insert(1, two.root);

	bool match = BinaryTree::subTreeFind(one.root, two.root);
	cout << "\nisSubTreeFind: " << match << endl;

	/*one.root = BinaryTree::insert(one.root, 5, Direction::LEFT);
	Node* left = BinaryTree::insert(one.root, 7, Direction::LEFT);
	Node* right = BiaryTree::insert(one, root, 3, Direction::LEFT);

	BinaryTree::insert(left, 18, Direction::RIGHT);

	cout << "\nCalling BinaryTree::test" << endl;
	BinaryTree tree = {10,20,30,40,50};
	BinaryTree tree2 = {10,20,30,40,50,60};


	bool match = BinaryTree::treeMatch(tree2.root, tree.root);
	cout << "\nTreeMatch: " << match << endl;

	match = BinaryTree::subTreeMatch(tree2.root, tree.root);
	cout << "\nisSubTree: " << match << endl;

	match = BinaryTree::subTreeMatch(tree.root, tree2.root);
	cout << "\nisSubTree2: " << match << endl; */

}

