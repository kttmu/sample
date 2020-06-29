filepath1 = "/raid/datasets/Hiroshima/predict_sequence.txt"
filepath2 = "/raid/datasets/Hiroshima/test_sample.txt"

#open written file
fil = open(outfile, mode="w" )

#convoluted list
with open(filepath) as f:
    datalist = f.readlines()

with open(filepath2) as f:
    datalist2 = f.readlines()

for i in range(len(datalist)):
    im_dir, rdr_dir, ano_dir = datalist2[i].split(' ')
    conv_dir = datalist[i]
    fil.write(conv_dir + ' ' + rdr_dir + ' ' + ano_dir)

