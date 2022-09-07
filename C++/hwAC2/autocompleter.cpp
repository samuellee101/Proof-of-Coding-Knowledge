#include <iostream>
#include <string>
#include <vector>
#include <string.h>
using namespace std;
#include "autocompleter.h"

//initialize
Autocompleter::Autocompleter()
{
	//cannot be nullptr need new Node()
	root = new Node();
	count = 0;
}

//insert into tree
void Autocompleter::insert(string x, int freq) {
	Node* blue = root;
	Entry e;
	e.s = x;
	e.freq = freq;
	/*if (root == nullptr)
	{
		blue = new Node();
	}
	else
	{*/
		for (int i = 0; i != x.size(); i++)
		{
			fun(blue->top, e);

			if (blue->children[x[i]] == nullptr)
			{

				blue->children[x[i]] = new Node();
				//makeEntry(blue->children[x[i]],e);
				//blue = blue->children[x[i]];
			}

			blue = blue->children[x[i]];
		}

	//}
	
	blue->marked = true;
	//blue->top.push_back(e);
	//blue->top[0] = e;
	fun(blue->top, e);
	count++;

};

/*void makeEntry(Node*& p, Autocompleter::Entry e) {
	p = new Node();
	p->top = e;
};*/

//return size
int Autocompleter::size()
{
	return count;
};

//find top three completions
void Autocompleter::completions(string x, vector<string>& T) {
	T.clear();
	Node* woof = root;

	for (int i = 0; i < x.size(); i++) {
		if (woof->children[x[i]] == nullptr)
		{
			woof->children[x[i]] = new Node;
		}
		woof = woof->children[x[i]];
	}
	simcity(woof->top, T);
};

//update the subtree
void Autocompleter::fun(vector<Entry>& v, Entry e) {
	v.push_back(e);
	if (v.size() == 2)
	{
		if (e.freq > v[0].freq)
		{
			swap(v[0], v[1]);
		}
	}
	else if (v.size() == 3)
	{
		if (e.freq > v[1].freq)
		{
			swap(v[2], v[1]);
		}
		if (e.freq > v[0].freq)
		{
			swap(v[1], v[0]);
		}
	}
	else if (v.size() == 4)
	{
		if (e.freq > v[2].freq)
		{
			swap(v[3], v[2]);
		}
		if (e.freq > v[1].freq)
		{
			swap(v[2], v[1]);
		}
		if (e.freq > v[0].freq)
		{
			swap(v[1], v[0]);
		}
		v.pop_back();
	}
	else
	{
	}
}

//entries to strings
void Autocompleter::simcity(vector<Entry> e, vector<string>& s) {
	for (int i = 0; i != e.size(); i++)
	{
		s.push_back(e[i].s);
	}
}