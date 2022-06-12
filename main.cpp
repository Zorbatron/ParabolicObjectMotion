//C++ Version of Parabolic Object Motion program
#include <iostream>
#include <cstdlib>
#include <cmath>
#define pi 3.14159265358
using namespace std;

void choice_1();
void choice_2();

int main() {
  float object_ay = -9.81;
  float object_ax = 0.0;
  float object_vix;
  float object_viy;
  double object_vi;
  double object_thetaRadians;
  int choice;
  cout << "Enter 1 for Viy and Vix and 2 for Vi and Θ.\n";
  cin >> choice;
  switch (choice) {
    case 1:
      choice_1();
      break;
    case 2:
      choice_2();
      break;
  }
  double object_vf = sqrt(pow(object_vix, 2) + pow((-object_viy), 2));
  double object_ty = (-object_viy)/(object_ay);
  double object_tx = 2 * object_ty;
  double object_dx = object_vix * object_tx;
  double object_dy = (object_viy * object_ty) + (0.5*object_ay*(pow(object_ty, 2)));
}

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
