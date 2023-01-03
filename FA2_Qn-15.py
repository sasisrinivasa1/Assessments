import sys

P = int(input("Principle (amount): "))
T = int(input("Time: "))
R = float(input("Rate: "))


Compound_Interest = P * (pow((1 + R/100), T))
print("Compound Interest = " + str(Compound_Interest))
print("Round CI = " + str(int(Compound_Interest)))

# Output:-
# PS C:\Users\Sasikumar S\PythonAssessments\Assessments> python .\FA2_Qn-15.py
# Principle (amount): 1200
# Time: 2
# Rate: 5.4
# Compound Interest = 1333.0992
# Round CI = 1333