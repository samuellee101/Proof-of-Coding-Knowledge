#include <bits/stdc++.h>
using namespace std;

class node {
public:
  double d;
  node *left;
  node *right;
  node(double x)
  {
    d = x;
    left = nullptr;
    right = nullptr;
  }
};

node *newNode(double d);

node *buildTree(double arr[], int start, int end) {
  if (start > end) {
    return nullptr;
  }
  int middle = (start + end) / 2;
  node *root = newNode(arr[middle]);
  root->left = buildTree(arr, start, middle - 1);
  root->right = buildTree(arr, middle + 1, end);
  return root;
}

node *newNode(double d) {
  node *Node = new node(d);
  return Node;
}

void showTree(node *node) {
  if (node == nullptr) {
    return;
  }
  showTree(node->left);
  cout << node->d << endl;
  showTree(node->right);
}

int main() {
  double arr[] = {1.00, 2.23, 3.00, 4.40, 4.90, 5.11, 6.41,         7.67, 7.77};
  int n = sizeof(arr) / sizeof(arr[0]);
  node *root = buildTree(arr, 0, n - 1);
  showTree(root);
  return 0;
}