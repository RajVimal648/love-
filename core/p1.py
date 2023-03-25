import random

print("Welcome Buddy..! Calculate your love percentage \n First Output is true one")

prince=input ("What is the name of prince :")

princess=input("What is the name of princess:")

boy=(len(prince))

girl=(len(princess))

rnd=random.randint(1,20)

percentage=100-(boy*girl)-rnd

print("Chances of true love together is"+str(percentage)+"%")