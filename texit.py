import re
import itertools
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
with open(outfile,'w') as w:
    for h in Iter_H1:
        w.write("\\sectiontitle{")
        w.write(h.group(0))
        w.write("}\n")
    for hx in Iter_Hx:
        w.write("\\sectiontsubitle{")
        w.write(hx.group(0).replace("#", ""))
        w.write("}\n")
    for eq in Iter_EQ:
        w.write("\\[ ",)
        w.write(eq.group(0).replace("$", "").replace("\n","")) 
        w.write(" \\]\n")
    # for il in Iter_Il:
    #     w.write(il.group(0))
    #     w.write("\n")
        
print("Completed!\n Output .tex file:", outfile)
