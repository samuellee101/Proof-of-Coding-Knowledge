#include <bits/stdc++.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double medium(std::vector<double> &A,
std::vector<double> &B)
{
  int Alen = A.size();
  int Blen = B.size();
  if (Alen > Blen)
  {
    std::vector<double> temp = A;
    A=B;
    B=temp;
  }
  double leftHalfLen = (Alen + Blen + 1) / 2;
  int aMinCount = 0;
  int aMaxCount = Alen;
  while (aMinCount <= aMaxCount)
   {
     int aCount = aMinCount + ((aMaxCount - aMinCount) / 2);
     int bCount = leftHalfLen - aCount;
     if (aCount > 0 && A[aCount - 1] > B[bCount])
     {   
       aMaxCount = aCount - 1;
     }
     else if (aCount < Alen && B[bCount - 1] > A[aCount])
     {
       aMinCount = aCount + 1;
     }
     else
     {
     double leftHalfEnd = (aCount == 0)  
       ? B[bCount - 1] :         
     (bCount==0) ? A[aCount - 1] 
       : std::max(A[aCount - 1],B[bCount - 1]); 
     if ((Alen + Blen)%2==1)
     {
       return leftHalfEnd;
     }
     double rightHalfStart = (aCount == Alen)
                        ? B[bCount]
                        : (bCount == Blen)
                            ? A[aCount] 
                            : std::min(A[aCount], B[bCount]);
                return (leftHalfEnd + rightHalfStart) / 2.0;
     }
    }
  
}

int main(){
  std::vector<double> A = {2.3,4.6,6.4,8.3};
  std::vector<double> B = {1.2,2.3,3.4};
  double x = medium(A,B);
  cout << x << endl;
  return 0;
}