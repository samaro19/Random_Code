filein = open("addin.txt", "r")
fileout = open("addout.txt", "w")
split = filein.read().split()
split2 = str(int(split[0]) + int(split[1]))
fileout.write(split2)
