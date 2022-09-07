#include "trendtracker.h"

Trendtracker::Trendtracker(string fileName)
{
    ifstream textFile;
    textFile.open(fileName);
    string ht;
    if (textFile.is_open())
    {
        while (!textFile.eof())
        {
            Entry newEntry;
            newEntry.hashtag = ht;
            newEntry.pop = 0;
            E.push_back(newEntry);
        }
    }
    textFile.close();
}

int Trendtracker::size()
{
    return E.size();
};

void Trendtracker::tweeted(string ht)
{
    E[search(ht)].pop++;

    if (search(ht) != -1)
    {
        for (int i = 0; i < S.size(); i++)
        {
            int j = i;
            while (j > 0 && E[S[j]].pop > E[S[j - 1]].pop)
            {
                int temp = S[j - 1];
                S[j - 1] = S[j];
                S[j] = temp;
                j--;
            }
        }
    }
    else
        return;
    if (S.size() > 3)
        S.pop_back();
};

int Trendtracker::popularity(string name)
{
    int index = search(name);
    if (index != -1)
        return E[index].pop;
    else
        return -1;
};

string Trendtracker::top_trend()
{
    if (E.size() > 0)
        return E[S[0]].hashtag;
    return "";
};

void Trendtracker::top_three_trends(vector<string>& T)
{
    T.clear();
    int n = S.size();

    if (E.size() == 0)
        T.push_back(E[n].hashtag);
    else
    {
        if (n == 0)
        {
            T.push_back(E[0].hashtag);
            T.push_back(E[1].hashtag);
            T.push_back(E[1].hashtag);
        }
        else if (n == 1)
        {
            T.push_back(E[S[0]].hashtag);
            T.push_back(E[1].hashtag);
            T.push_back(E[2].hashtag);
        }
        else if (n == 2)
        {
            T.push_back(E[S[0]].hashtag);
            T.push_back(E[S[1]].hashtag);
            T.push_back(E[2].hashtag);
        }
        else if (n == 3)
        {
            T.push_back(E[S[0]].hashtag);
            T.push_back(E[S[1]].hashtag);
            T.push_back(E[S[2]].hashtag);
        }
    }

};

int Trendtracker::search(string ht)
{
    int s = 0;
    int e = E.size() - 1;
    while (s <= e)
    {
        int m = (s + e) / 2;
        if (ht == E[m].hashtag)
            return m;
        if (ht < E[m].hashtag)
            e = m - 1;
        else
            s = m + 1;
    }
    return -1;
};