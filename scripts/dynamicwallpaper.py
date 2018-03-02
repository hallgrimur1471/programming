#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
from random import randint
import commands

# get a base image
base = Image.open('/home/hallgrimur1471/programming/scripts/dynamicwallpaper_base.jpg').convert('RGBA')
imageWidth, imageHeight = base.size

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

n = 7 # number of projects

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

project4 = "Matasano crypto challenges"
project4TotalChallenges = 64+1 # +1 so we don't go to 100% when starting last challenge
project4CurrentChallenge = commands.getstatusoutput("cd /home/hallgrimur1471/programming/matasano_crypto_challenges/matasano_cryptography && ls | egrep '^s[0-9]_.+$' | xargs ls -1 | egrep -o '^c[0-9][0-9]' | uniq | wc -l")[1]
progress4 = 100*float(project4CurrentChallenge)/(int(project4TotalChallenges))
progress4 = "%.1f%%" % progress4

project5 = "Advent of code"
project5TotalChallenges = 25*2+1 # +1 so we don't go to 100% when starting last challenge
project5CurrentChallenge = commands.getstatusoutput("cd /home/hallgrimur1471/programming/advent-of-code && ls | egrep '^day(-|_)[0-9]+.*\.(py|hs)$' | wc -l")[1]
progress5 = 100*float(project5CurrentChallenge)/(int(project5TotalChallenges))
progress5 = "%.1f%%" % progress5

project6 = "Neural networks"
project6TotalCourses = 15
project6CompletedCourses = 1
progress6 = 100*float(project6CompletedCourses)/(int(project6TotalCourses))
progress6 = "%.1f%%" % progress6

project7 = "Fast reading course"
progress7 = "35.00%%"

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

projects = [project1, project2, project3, project4, project4, project6, project7]
progresses = [progress1, progress2, progress3, progress4, progress5, progress6, progress7]
for i in range(n):
    d.text((fx-12*len(projects[i]),(i+1)*vs), projects[i], font=fnt, fill=textColor)
    d.text((fx-12*len(progresses[i]),(i+1)*vs+60), progresses[i], font=fnt, fill=textColor)

out = Image.alpha_composite(base, txt)

# this will automatically update the background since gsettings knows this is the background file
out.save("/home/hallgrimur1471/programming/scripts/dynamicwallpaper.jpg", "jpeg")

