#include <iostream>
#include <cmath>
#define object_ay -9.81
#define pi 3.14159265358
using namespace std;

void finish(float obj_vix, float obj_viy) {
  double object_vf = sqrt(pow(obj_vix, 2) + pow((-obj_viy), 2));
  double object_ty = (-obj_viy)/(object_ay);
  double object_tx = 2 * object_ty;
  double object_dx = obj_vix * object_tx;
  double object_dy = (objt_viy * object_ty) + (0.5*object_ay*(pow(object_ty, 2)));
}

void choice_1(float vix, float viy) {
  object_vi = sqrt(pow(vix, 2) + pow(viy, 2));
  object_thetaRadians = atan(viy/vix);
  finish(vix, viy);
}

void choice_2(double obj_thetaRadians, double obj_vi) {
  obj_thetaRadians *= pi/180;
  object_vix = obj_vi * cos(obj_thetaRadians);
  object_viy = obj_vi * sin(obj_thetaRadians);
  finish(object_vix, object_viy);
}
