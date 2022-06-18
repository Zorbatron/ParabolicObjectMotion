//C++ Version of Parabolic Object Motion program
#include <iostream>
#include <cstdlib>
#include <cmath>
#include "choices.h"
#define pi 3.14159265358
#define object_ax 0.0
#define object_ay -9.81
using namespace std;

int main() {
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
  finish();
}
