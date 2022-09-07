#pragma once

template <class T>

class priorityQueueLL
{
private:
    class node
    {
    public:
        node* p;
        node* n;
        T dtype;
        node(T x)
        {
            p = nullptr;
            n = nullptr;
            dtype = x;
        }

    };

    node* h;
public:

    priorityQueueLL()
    {
        h = nullptr;
    }

    ~priorityQueueLL()
    {
        while (h != nullptr)
        {
            node* temp = h;
            h = h->n;
            h->p = nullptr;
            delete temp;
        }
    }

    //delete the minimum
    T extractMin()
    {
        node* f = h;
        h = h->n;
        T dtype = f->dtype;
        delete f;
        return dtype;
    }

    bool empty()
    {
        if (h != nullptr)
        {
            return false;
        }
        return true;
    }

    void insert(T x)
    {
        node* n = new node(x);

        if (h == nullptr) {
            h = n;
            return;
        }

        if (x < h->dtype) {
            n->n = h;
            h = n;
            return;
        }

        node* p = h, * curr = h->n;

        while (curr != nullptr) {

            if (x < curr->dtype) {
                break;
            }

            p = curr;
            curr = curr->n;
        }

        p->n = n;
        n->n = curr;
    }

};