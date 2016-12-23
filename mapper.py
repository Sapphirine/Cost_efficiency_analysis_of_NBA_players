import sys

def mapper():
    count = 0
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on comma and put the data in an array
        data = line.strip().split(",")

        if len(data) == 5:

            count += 1
            player = data[0]
            per = data[1]
            ows = data[2]
            dws = data[3]
            ws = data[4]
        
            # Now print out the data that will be passed to the reducer
            if count >= 1:
                print "{0}\t{1}\t{2}\t{3}\t{4}".format(player, per, ows, dws, ws)

mapper()