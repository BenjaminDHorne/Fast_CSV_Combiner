
### assume three files 1.txt, 2.txt. 3.txt, all comma separated
### with id as the first column.

def get_vals(fname):
    vals = {}
    f = open(fname)
    m = f.readline().strip().split(",")
    header = ",".join( m[1:] )
    for line in f:
        m = line.strip().split(",")
        vals[ m[0] ] = ",".join(m[1:])
    return vals, header


if __name__ == "__main__":
    feat1, header1 = get_vals("")
    feat2, header2 = get_vals("")
    feat3, header3 = get_vals("")
    empty1 = ",".join( ["None"]*102 )  ## change to number of features in file1
    empty2 = ",".join( ["None"]*5 )  ## change to number of features in file2
    empty3 = ",".join( ["None"]*25)  ## change to number of features in file3
    allids = set(feat1.keys() + feat2.keys() + feat3.keys())# + feat4.keys() + feat5.keys())

    fout = open("", "w")
    fout.write( "pid,%s,%s,%s\n" %(header1, header2, header3))

    for userid in allids:
        
        if userid in feat1:
            line1 = feat1[userid]
        else:
            line1 = empty1

        if userid in feat2:
            line2 = feat2[userid]
        else:
            line2 = empty2

        if userid in feat3:
            line3 = feat3[userid]
        else:
            line3 = empty3

        fout.write("%s,%s,%s,%s\n" %(str(userid),line1,line2,line3))
    fout.close()

            
