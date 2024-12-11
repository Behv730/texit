import re

sample =   "8\n---\n# Hliðtengdar RLC Eðlissvörun\n$$\n\\tag{ neper tíðni} \\alpha = \\frac{1}{2RC}\n$$\n$$\n\\tag{eig"
reg = re.compile(r'(?<=#\s).+')

alist = reg.finditer("# halloa \n # hallob")
blist = reg.finditer(sample)

for item in blist:
   print(item.group(0))