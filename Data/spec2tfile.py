import sys

f = open('KaolinpreproTrainingsset13021434v2.csv','r')

tfile = open('spectra2tfile.t','w')

# einlesen der ersten Zeile und kreieren eines Array mit den Wellenlängen,
# später Indices
ersteZeile = f.readline()
arrayOfNm = []
for nm in ersteZeile.split(','):
    arrayOfNm.append(nm[0:4])



for line in f:
    tfile.write(line.split(',')[0]+ " ")
    i = 0
    for values in line.split(','):
        if i != 0:
            tfile.write(" " + str(i) + ':' + values)
        i += 1
tfile.write("\n")
# for line in f:
#     print(line.split(',')[0]+ " ",end="")
#     #tfile.write(f.readline().split()[0])
#     i = 0
#     for values in line.split(','):
#         #print(str(i))
#         if i != 0:
#             print(arrayOfNm[i] + ':' + values + " ",end="")
#         i += 1