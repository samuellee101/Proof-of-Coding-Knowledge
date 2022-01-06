//***********************************************************************// Team #23 CSCI/CMPE 2380 Fall 2021 Homework # 1
// Samuel Lee
//
//***********************************************************************

#include "pokemon.h"

string Pokemon :: name(){
return _name;
};

int Pokemon :: Ndex(){
return _ndex;
}

bool Pokemon :: is_multitype(){
  if (this->types[1]!=0){
    return true;
  }
  else{
    return false;
  }
  
}

Pokemon::Type Pokemon :: type1(){
  return this->types[0];
}

Pokemon::Type Pokemon :: type2(){
if (this->types[1]==0)
{
  return this->types[0];
}
else
{
  return this->types[1];
}
};

//switch case used, where every case is a Type
float Pokemon :: damage_multiplier(Type attack_type){
switch(attack_type){
  case Fighting:
    if (this->types[0]==Pokemon::Normal || this->types[1]==Pokemon::Normal)
    {
      if (this->types[0]==Pokemon::Flying || this->types[1]==Pokemon::Flying)
      {
        return 1.0;
      }
      else if (this->types[0]==Pokemon::Poison || this->types[1]==Pokemon::Poison)
      {
        return 1.0;
      }
      else
      return 2.0;
    }
    else if (this->types[0]==Pokemon::Flying || this->types[1]==Pokemon::Flying)
    {
      if (this->types[0]==Pokemon::Poison || this->types[1]==Pokemon::Poison)
      {
        return 0.25;
      }
      else
      {
        return 0.5;
      }
    }
    else if (this->types[0]==Pokemon::Poison || this->types[1]==Pokemon::Poison)
    {
      if (this->types[0]==Pokemon::Flying || this->types[1]==Pokemon::Flying)
      {
        return 0.25;
      }
      else
      {
        return 0.5;
      }
    }
    //attempt to solve the test errors pertaining to //fighting
    /*if (this->types[0]==Poison || this->types[0]==Flying)
    {
      return 0.5;
    }
    if (this->types[0]==Fighting)
    {
      return 1.0;
    }
    else
    return 0.5;*/


  case Flying:
    if (this->types[0]==Fighting || this->types[1]==Fighting)
    {
      return 2.0;
    }
    else
    return 1.0;
  case Poison:
    if (this->types[0]==Poison || this->types[1]==Poison)
    {
      return 0.5;
    }
    else
    return 1.0;
  case Normal:
  return 1.0;
  default:
  return 1.0;
}


};

//simple code, just use this-> and the variable
Pokemon :: Pokemon(string name, int ndex, Type type1){
this->_name = name;
this-> _ndex = ndex;
this->types[0] = type1;
}

Pokemon :: Pokemon(string name, int ndex, Type type1, Type type2){
this->_name = name;
this-> _ndex = ndex;
this->types[0] = type1;
this->types[1] = type2;
}