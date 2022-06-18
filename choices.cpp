#include "choices.h"
#include <iostream>
#include <cmath>
#define pi 3.14159265358
using namespace std;

void choice_1() {
  cout << "Input object's initial horizontal velocity.\n";
  cin >> object_vix;
  cout << "Input object's initial vertical velocity.\n";
  cin >> object_viy;
  object_vi = sqrt(pow(object_vix, 2) + pow(object_viy, 2));
  object_thetaRadians = atan(object_viy/object_vix);
}

void choice_2() {
  cout << "Input object's initial velocity.\n";
  cin >> object_vi;
  cout << "Input object's angle from the horizontal in degrees.\n";
  cin >> object_thetaRadians;
  object_thetaRadians *= pi/180;
  object_vix = object_vi * cos(object_thetaRadians);
  object_viy = object_vi * sin(object_thetaRadians);
}
