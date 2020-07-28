read = open("outliers_value_galera100k_outliers_gaussian_0.info")
write = open("pc.xyz", 'w')

for line in read:
    splited = line.split(' ')
    if (float(splited[3]) < 0.5):
    	print(splited[0] + ' ' + splited[1] + ' ' + splited[2], file=write)
    
read.close()
write.close()

