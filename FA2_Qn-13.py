import sys
text = 'Gavs Technologies'

character = sys.argv[1]
inindex = int(sys.argv[2])

text = text[0:inindex] + character + text[(inindex+1):]
print(text)

# Output:-
# PS C:\Users\Sasikumar S\PythonAssessments> python .\FA2_Qn-13.py X 5
# Gavs Xechnologies