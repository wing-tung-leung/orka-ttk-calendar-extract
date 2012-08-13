#!/usr/bin/python

import sys

# Geldig voor seizoen 2011-2012 en 2012-2013.
# In het verleden ook al "ORKA" of "Orka TTK" geweest.
CLUB_NAME="Orka"

def shortenName(teamName):
	n = teamName.replace("<b>", "").replace("</b>", "")
	n = n.replace("TTK", "").replace("VZW", "")
	n = n.replace("T.T.K.", "").replace("TTC", "")
	n = n.replace("K.T.T.K", "")
	n = n.replace("T.T.K", "")
	#n = n.replace("PPC", "")
	return n.replace("  ", " ").strip()

def reformatDate(date):
	parts = date.split("-")
	day = parts[0]
	month = parts[1]
	year = "20%s" % parts[2].strip()
	return "%s-%s-%s" % (year, month, day)

def event(dateLine, homeLine, visitorLine):
	date = dateLine[29:38]
	date = reformatDate(date)
	homeEnd = homeLine.find("</td>")
	visitorEnd = visitorLine.find("</td>")
	home = homeLine[26:homeEnd]
	visitor = visitorLine[26:visitorEnd]
	home = shortenName(home)
	visitor = shortenName(visitor)
	subject = "%s - %s" % (home, visitor)
	print "%s,%s" % (subject, date)


line = sys.stdin.readline()
#print "Subject,Start Date"
while len(line) > 0:
	if line.find("DBTable_short_first") > 0:
		gameIdLine = line
		dateLine = sys.stdin.readline()
		homeLine = sys.stdin.readline()
		visitorLine = sys.stdin.readline()
		if (len(dateLine) > 50): # team is not free, playing
			if homeLine.find(CLUB_NAME) > 0 or visitorLine.find(CLUB_NAME) > 0:
				event(dateLine, homeLine, visitorLine)
	line = sys.stdin.readline()
	
