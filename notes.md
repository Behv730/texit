# Notes
## Functionality
this program reads my Obsidian notes (.md) and transfers all the latex equations to a external file so I can easily transfer the equations to a latex equation sheet.
###
I want this to work from the terminal in any folder, maybe i have to make a zsh script that calls this python file.

## Pseudocode
ég er að lesa textann, taka út og breyta og setja inn
*gæti mögulega copyað allt yfir í out, eytt óþarfa og síðan breytt?*

1. open .md file
3. make/open out.tex/out.txt file
4. when read .md
   1. find headings1
   2. find headingsx smaller than 1
   3. find equations 
5. sort the equations in order between headings
6. write the contents between equations inside \[    \]
7. write the headings1 inside \sectiontitle{      }
8. write the headingsx inside \sectionsubtitle{    }
   1. write the headings matches raw and then just replace "#" with ""

later i want to pass in args
## learning goals
- I want to use regex
- I want to rewrite this in C

### Regex
* matches preceding char 0 or more times
+ matches preceding char 1 or more times
. matches everything exept a newline character
$ matches new line 

í python eru regex pattern compiluð
þarf að nota r string (r'') því annars hundsar python \ og ég þarf að hafa \\ fyrir hvert \
* \ í byrjun er f/ markdown formatið*
re.findall() skilar list með öllum expressions sem matcha, þeas strings
re.finditer() skilar lista af Match object. nota MATCH.start() til að finna byrjun

get notað replace() í headings fyrir ##?

(tested)
#### HEADING 1 pattern
\ (?<=#\s).+ 
#### HEADING 2+ pattern
\ #+\s.+'
#### EQUATION pattern
\ (?<=\$\$\s)\s*.+\s*(?=\s\$\$)
*þarf að sleppa lookahead því hún les ekki $$ og tekur því $$ oftar en 1x*
(?<=\$\$\s)\s*.+\s*(?=\s\$\$)

## Debug
er að lenda í veseni með regexið, það er ekki að matcha neitt í notes breytunni
held að það sé því að þegar við erum að lesa með open() þá fáum við ehv formattaðan string, ekki raw eins og við viljum.