//***********************************************************************
// Team # CSCI 2380 Fall 2021 Homework # 7
// Samuel Lee
// Dante Villarreal
//
//***********************************************************************

#include "browserhistory.h"

//basically, empty everything
//also make sure the default is set
BrowserHistory::BrowserHistory(string default_url)
{
head = new Node();
head->url = default_url;
head->prev = nullptr;
head->next = nullptr;
tail = head;
current = head;
}

//simple, return the current url. name explains action.
string BrowserHistory::current_url()

{
 if(current != nullptr){
  return current->url;
}
return "";

}

//tricky. need to set up linked list such that
//head is previous url, tail is next url, current is current
void BrowserHistory::go_to_url(string url){

Node *bossman = new Node;
bossman->url = url;
bossman->next = nullptr;

if(current == nullptr)

{
bossman->next = head;
head->prev = bossman;
head = bossman;
current = bossman;

}
else{

 Node *temp = head;
 while(temp != current){
  temp = temp->next;
}
//tail->prev=current;
bossman->prev = current;
current->next = bossman;
current = bossman;
}

}

//current becomes next
//previous becomes current
void BrowserHistory::back(){
if(can_go_back()){
current = current->prev;
}
}

//check if previous exists
bool BrowserHistory::can_go_back(){
if(current->prev != nullptr)
return true;
return false;
}

//sum all the nodes of head
int BrowserHistory::past_url_count()
{
int i=0;
Node *temp = current;
//deleted i++ at current!=nullptr, extraneous
while(temp->prev != nullptr)
 {
  temp = temp->prev;
  i++;
 }
return i;
}

//next becomes current
//current becomes previous
void BrowserHistory::forward(){

 if(can_go_forward())

  current = current->next;

}

//check if next exists
bool BrowserHistory::can_go_forward(){

if(current->next != nullptr)
{
  return true;
}

return false;

}

//sum future url
int BrowserHistory::future_url_count()

{
int i=0;
Node *temp = current;
//deleted i++ at current!=nullptr, extraneous
while(temp->next != nullptr){
temp = temp->next;
i++;
}

return i;

}