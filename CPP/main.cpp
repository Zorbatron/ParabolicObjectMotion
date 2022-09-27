//C++ Version of Parabolic Object Motion program
// @author: Velocities
// @version: 1.0
#include <iostream>
#include <cstdlib>
#include <cmath>
#include "choices.h"
#define pi 3.14159265358
#define object_ax 0.0
#define object_ay -9.81
using namespace std;

int main() {
  // Allocate necessary memory for values user will enter
  float object_vix;
  float object_viy;
  double object_vi;
  double object_thetaRadians;
  int choice;
  // Ensure user types a valid choice
  bool get_choice;
  do {
    try {
      cout << "Enter 1 for Viy and Vix and 2 for Vi and Θ.\n";
      cin >> choice;
      if (choice == 1 || choice == 2) {
        get_choice = false;
      }
      else {
        get_choice = true;
        cout << "Invalid choice" << endl;
      }
    } while (get_choice);
  
  switch (choice) {
    case 1:
      // Avoid dividing by 0 by ensuring user types a valid number (not 0)
      bool get_vix;
      do {
        cout << "Input object's initial horizontal velocity.\n";
        cin >> object_vix;
        if (object_vix == 0) {
          get_vix = true;
          cout << "Invalid horizontal velocity: Cannot divide by 0 in calculations!" << endl;
        }
        else {
          get_vix = false;
        }
      } while (get_vix);
      cout << "Input object's initial vertical velocity.\n";
      cin >> object_viy;
      choice_1(object_vix, object_viy);
      break;
    case 2:
      cout << "Input object's initial velocity.\n";
      cin >> object_vi;
      cout << "Input object's angle from the horizontal in degrees.\n";
      cin >> object_thetaRadians;
      choice_2(object_thetaRadians, object_vi);
      break;
  }
}
