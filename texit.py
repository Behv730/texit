import re
from operator import itemgetter
# Regex patterns
H1 = re.compile(r'(?<=#\s).+')
Hx = re.compile(r'#+\s.+') # lookahead requires fixed length (i.e. not #+)
EQ = re.compile(r'\$\$\s*.+\s*\$\$') # (?<= xxx) er lookahead og sleepir því að setja með, fæ því bara eq
# Il = re.compile(r'\$.+\$') # inline math

# make it an arg, import argc argv from system?
readfile = "files/8 Kafli copy.md"
# open file
with open(readfile, "r") as r:
    notes=r.read() # les allan fileinn, gæti overloadað memory ef ég passa mig ekki.
    Iter_H1 = H1.finditer(notes)
    Iter_Hx = Hx.finditer(notes)
    Iter_EQ = EQ.finditer(notes)
    #Iter_Il = Il.finditer(notes)
# make out file
outfile = readfile.replace(".md", ".tex")



# not in order
## use h.start(0) to sort?, need to rewind/seek iters?

lines = []
# clean up and load to list
for h in Iter_H1:
    h.group(0).replace("#","")
    section = "\\sectiontitle{" + h.group(0) + "}"
    lines.append([h.start(0), section])
for hx in Iter_Hx:
    hx.group(0).replace("#","")
    subsection = "\\sectionsubtitle{" + hx.group(0) + "}"
    lines.append([hx.start(0), subsection])
for eq in Iter_EQ:
    eq.group(0).replace("$$","").replace("\n","")
    equation = "\\[" + eq.group(0) + "\\]"
    lines.append([eq.start(0), equation])

lines.sort(key=itemgetter(0)) # sort by .start(0)

with open(outfile,'w') as w:
    for line in lines:
        w.write(line[1])
        w.write("\n")
print("Completed!\n Output .tex file: }")
