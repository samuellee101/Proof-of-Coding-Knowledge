#pragma once

class stackLL
{
private:
	class node
	{
	public:
		node* past;
		int a;

		node(int x)
		{
			a = x;
			past = nullptr;
		}
	};

	node* top;

public:

	void insertAt(int x, int i)
	{
		node* temp1;
		temp1 = top;
		for (int c = 0; c <= i + 1; c++)
		{
			if (c == i) 
			{
				node* temp2;
				temp2 = new node(x);
				temp1->past = temp2;
			}
			if (temp1 != nullptr && temp1->past != nullptr)
				break;
			else
				temp1 = temp1->past;
		}
	}

	stackLL()
	{
		top = nullptr;
	}

	~stackLL()
	{
		node* temporary;
		while (top!=nullptr)
		{
			temporary = top;
			top = top->past;
			delete temporary;
		}
	}

	bool empty()
	{
		if (top==nullptr)
		{
			return true;
		}
		return false;
	}

	void push(int x)
	{
		node* tempNode;
		tempNode = new node(x);

		tempNode->past = top;
		top = tempNode;
	}

	int pop()
	{
		node* temporary;
		temporary = top;
		top=top->past;
		return temporary->a;
	}

};