import re
from operator import itemgetter
from sys import argv
import os
# Regex patterns
H1 = re.compile(r'(?<!#)#\s.+') # negative lookbehind
Hx = re.compile(r'##+\s.+') 
EQ = re.compile(r'\$\$\s*.+[\s]*[^\$]*\$\$')

readfile = argv[1] # note: pass with quotes if spaces in file name

if (not readfile.find(".md")):
    print("File must be .md")
    exit
    
# make out file
outfile = readfile.replace(".md", ".tex")

# put output file in specified path
if (len(argv) == 3):
    outfile = os.path.split(readfile)[1] # get last component in path
    out_path = argv[2]
    outfile = out_path + outfile.replace(".md",".tex")


# open file
with open(readfile, "r") as r:
    notes=r.read() # could overload memory?
    Iter_H1 = H1.finditer(notes)
    Iter_Hx = Hx.finditer(notes)
    Iter_EQ = EQ.finditer(notes)


lines = []
# clean up and load to list
for h in Iter_H1:
    section = "\\sectiontitle{" + h.group(0).replace("#","").replace("_",".") + "}"
    lines.append([h.start(0), section])
for hx in Iter_Hx:
    subsection = "\\sectionsubtitle{" + hx.group(0).replace("#","").replace("_",".") + "}"
    lines.append([hx.start(0), subsection])
for eq in Iter_EQ: # could regex process the output file to format it nicer, having problems with align env
    equation = "\\[" + eq.group(0).replace("$", "").replace("align","aligned") + "\\]"
    lines.append([eq.start(0), equation])

# sort by .start(0)
lines.sort(key=itemgetter(0)) 

# write to outfile
with open(outfile,'w') as w:
    for line in lines:
        w.write(line[1])
        w.write("\n")
print("Completed!\nOutput file:", outfile)

# TODO: limit size of input files allowed, or work the file in chunks.
# TODO: Regex process the output file because obsidian latex is not compatible with "normal latex". fx \tag{} doesnt work with \{aligned}