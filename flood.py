#! /usr/bin/python

""" ENTER HELP HERE """

import math

def rad(x):
      """ Converts degree to radian"""
      a = x * math.pi * 2 / 360
      return a

if __name__ == "__main__":

  SF = float(raw_input(" Enter saftey factor (1.5-2.0) : "))

  GH = float(raw_input(" Enter wet unit weight : "))

  GHS = float(raw_input(" Enter submerged unit weight : "))

  PHI = float(raw_input(" Enter angle of friction : "))

  Fall = float(raw_input(" Enter alowable stress for sheet pile : "))
 
  H = float(raw_input(" Enter exposed length of sheeting : "))

  HE = float(raw_input(" Enter water level from top ground level : "))

  """ CALCULATIONS """
  
  Ka = (math.tan(rad(45-PHI/2)))**2
  
  Kp = 1/(Ka * SF)
  
  HW = H - HE
  
  P1 = GH * HE * Ka
  
  P2 = Ka * (GH * HE + GHS * HW)
  
  HU = P2 / (GHS*(Kp - Ka))
  
  PA = 0.5 * (P1 * HE + P2 * HU + (P1 +P2) * HW)
  
  Z1 = HE/3 + HW + HU
  Z2 = HW/2 + HU
  Z3 = HU * 2/3
  Z = ( 0.5*P1*HE*Z1 + 0.5*P2*HU*Z3 + 0.5*(P1+P2)*HW*Z2) / PA
  
  if PHI < 28:
     D = 2*H
     print "Very loose"
  elif 28 <= PHI < 30:
       D = 1.5 * H
       print " Loose"
  elif 30<= PHI < 36:
       D = 1.28 *H
       print " Medium Dense"
  elif 36 <= PHI < 41:
       D = 1.0 * H
       print "Dense"
  elif 41 <= PHI :
       D = 0.75 * H
       print " Very Dense"
       
  n = int(raw_input(" Enter maximum number of iterations : "))
  
  for i in range (0, n):
      print "---> i: ", i, "D: ", D
      HB = D - HU
      P4 = GHS*HB*(Kp - Ka)
      Z4 = HB/3
      Ma = PA*(Z + HB)
      Mp = P4 * Z4
      if math.fabs(Mp) > math.fabs(Ma):
         break
      else:
           D = 1.01 * D
  
  Z5 = math.sqrt(2*PA/(GHS * (Kp - Ka)))
  Mmax = PA * (Z + Z5) - (0.5*GHS*(Z5**2)*(Kp*(Kp-Ka)))*0.33*Z5
  S = Mmax/Fall
  
  print " Wet unit weight ", GH
  print " Penetration Depth ", D
  print " Maximum moment ", Mmax
  print " Section modulus ", S    
  




