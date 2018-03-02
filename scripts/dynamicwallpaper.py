#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
from random import randint
import commands


# get an image
base = Image.open('/home/hallgrimur1471/bashscripts/dynamicwallpaper_base.jpg').convert('RGBA')
imageWidth, imageHeight = base.size

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

n = 3
project1 = "The C Programming Language"
project1TotalExercises = commands.getstatusoutput('cat /home/hallgrimur1471/c/exercise-count.txt | awk \'{sum += $3} END {print sum}\'')[1]
project1CurrentExercise = commands.getstatusoutput('ls /home/hallgrimur1471/c | egrep \'^ex.-.*\.c$\' | wc -l')[1]
progress1 = 100*float(project1CurrentExercise)/(int(project1TotalExercises)+1)
progress1 = "%.1f%%" % progress1
project2 = "Learn you a Haskell"
project2TotalChapters = 14
project2CurrentChapter = commands.getstatusoutput('ls /home/hallgrimur1471/programming/learn-you-a-haskell | egrep \'^c[0-9]+-.*\.hs$\' | egrep -o \'^c[0-9]+-\' | uniq | wc -l')[1]
progress2 = 100*float(project2CurrentChapter)/(int(project2TotalChapters)+1)
progress2 = "%.1f%%" % progress2
project3 = "Scheme interpreter written in Haskell"
project3TotalChapters = commands.getstatusoutput('cat /home/hallgrimur1471/programming/scheme-interpreter-written-in-haskell/project.progress | wc -l')[1]
project3CurrentChapter = commands.getstatusoutput('cat /home/hallgrimur1471/programming/scheme-interpreter-written-in-haskell/project.progress | awk \'{sum += $2} END {print sum}\'')[1]
progress3 = 100*float(project3CurrentChapter)/(int(project3TotalChapters))
progress3 = "%.1f%%" % progress3

project4 = "Fast reading course"
project5 = "Linear regression"
project6 = "Cryptopals"
project7 = "Advent of code"

fx = float(imageWidth)/2
vs = imageHeight/(n+2)
color1 = randint(0,1)*255
color2 = randint(0,1)*255
color3 = randint(0,1)*255
if color1==0 and color2==0 and color3==0:
    color1=255
    color2=255
    color3=255
color1 = 255
color2 = 255
color3 = 255
textColor = (color1,color2,color3,255)

d.text((fx-12*len(project1),1*vs), project1, font=fnt, fill=textColor)
d.text((fx-12*len(progress1),1*vs+60), progress1, font=fnt, fill=textColor)

d.text((fx-12*len(project2),2*vs), project2, font=fnt, fill=textColor)
d.text((fx-12*len(progress2),2*vs+60), progress2, font=fnt, fill=textColor)

d.text((fx-12*len(project3),3*vs), project3, font=fnt, fill=textColor)
d.text((fx-12*len(progress3),3*vs+60), progress3, font=fnt, fill=textColor)

out = Image.alpha_composite(base, txt)
out.save("/home/hallgrimur1471/bashscripts/dynamicwallpaper.jpg", "jpeg")

