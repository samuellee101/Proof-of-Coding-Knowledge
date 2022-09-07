#pragma once

template <class T>

class queueLL
{
private:
	class node
	{
	public:
		node* n;
		//node* p;
		T data;
    

		node(T x)
		{
			data = x;
			n = nullptr;
			//p = nullptr;
		}
	};

	node* front;
	node* back;
  int size;

public:
	queueLL()
	{
		front = nullptr;
		back = nullptr;
	}

	~queueLL()
	{
		node* garbage;
		while (front != nullptr)
		{
			garbage = front;
			front = front->n;
			delete garbage;
		}
    size = 0;
	}

	void decimate()
	{
		node* one = front;
		node* two = nullptr;
		int temp = 1;


		while (one != nullptr)
		{
			if (temp==9)
			{
				if (one->n != nullptr)
				{
					two = one->n;
					two->n = one->n;
					//delete two->data;
					delete two;
					temp = -1;
				}
				else{
          break;
        }
			}
			else
      {
        one = one->n;
      }
			temp++;
		}
  }

	void enqueue(T x)
	{
		node* added;
		added = new node(x);
		if (front == nullptr)
		{
			front = added;
			back = added;
		}
		else
		{
			back->n = added;
			back = back->n;
		}
    size++;
	}

	T dequeue()
	{
		node* goaway;
		goaway = front;
		front = front->n;
		T a = goaway->data;
		delete[] goaway;
    size--;
		return a;
	}

	bool empty() 
	{
		if (front == nullptr)
		{
			return true;
		}
		return false;
	}

};