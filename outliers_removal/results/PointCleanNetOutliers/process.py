import sys

read = open(sys.argv[1])
write = open("result.xyz", 'w')

for line in read:
    splited = line.split()
    if (float(splited[3]) < 0.5):
    	print( splited[0] + ' ' + splited[1] + ' ' + splited[2], file=write)

read.close()
write.close()
