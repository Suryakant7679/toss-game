import random
design='''
   _____
  / _ _ \  
(o / | \ o)
 || o|o ||
 | \_|_/ |
 |  ___  |
 | (___) |
 |\_____/|
 | \___/ |
 \       /
  \__ __/
     U 
     '''
print(design)
chance=["Ravi", "Shweeta", "Sneha", "Sahil" , "puja"]
result=random.choice(chance)
print(result,"will play first")
chance.remove(result) 
result=random.choice(chance)
print(result,"will play second")
chance.remove(result) 
result=random.choice(chance)
print(result,"will play third")
chance.remove(result) 
result=random.choice(chance)
print(result,"will play forth")
chance.remove(result) 
result=random.choice(chance)
print(result,"will play fifth")
