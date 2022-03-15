from sre_constants import SUCCESS
from symtable import Symbol
from sys import flags

print("+ = Addition")
print("- = Subtraction")
print("x = Multiplication")
print("/ = Division")
print("^ = To the power of")

Number1=input("Number1: ")
Math_Symbol=input("Math Symbol: ")
Number2=input("Number2: ")

if Math_Symbol==("+"):
   sam=float(Number1) + float(Number2)
   print("Addition Answer: "+str(sam))

if Math_Symbol==("-"):
   sum=float(Number1) - float(Number2)
   print("Subtraction Answer: "+str(sum))

if Math_Symbol==("x"):
   som=float(Number1) * float(Number2)
   print("Multiplication Answer: "+str(som))

if Math_Symbol==("/"):
   sim=float(Number1) / float(Number2)
   print("Division Answer: "+str(sim))

if Math_Symbol==("^"):
   sem=float(Number1) ** float(Number2)
   print ("N1 to the power of N2 Answer: "+str(sem))