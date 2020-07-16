import re # regex lib

pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+),.*$')

f = open("results.csv", "r")

for line in f:
  match = re.match(pattern, line)
  if match:
    total = int(match.group(4)) + int(match.group(5))
    if total > 30:
      print( "%d, %s %s-%s %s" % ( total, match.group(2), match.group(4), match.group(5), match.group(3) ) )

f.close()