#include <bits/stdc++.h>
#include <stdio.h>
 
class node {
public:
    int d;
    node *left, *right;
node(int x)
  {
    d = x;
    left = nullptr;
    right = nullptr;
  }
};

void levelOrderTraversal(node * r);
void printCurrentLevel(node* root, int level);
int height(node* node);
node* newNode(int d);
 
void levelOrderTraversal(node * r)
{
    int tallness = height(r);
    for (int i = 1; i <= tallness; i++)
        printCurrentLevel(r, i);
}
 
void printCurrentLevel(node* root, int level)
{
    if (root == nullptr)
    {
      
    }
  else
    {
      if (level == 1)
      {
        printf("\n%d",root->d);
      }
      else if (level > 1) 
      {
        printCurrentLevel(root->left, level - 1);
        printCurrentLevel(root->right, level - 1);
      }
    }
}
 
int height(node* node)
{
    if (node == nullptr)
    {
      return 0;
    }
    else {
        int lheight = height(node->left);
        int rheight = height(node->right);
 
        if (lheight > rheight) 
        {
            return (lheight + 1);
        }
        else 
        {
            return (rheight + 1);
        }
    }
}

node* newNode(int d)
{
    node* Node = new node(d);
    return (Node);
}
 
int main()
{
    node* tree = newNode(1);
    tree->left = newNode(2);
    tree->right = newNode(3);
    tree->left->left = newNode(4);
    tree->left->right = newNode(5);
 
    printf ("This is the level order traversal: ");
    levelOrderTraversal(tree);
 
    return 0;
}