import sys

def calculation():
    for line in sys.stdin:
        data = line.replace("'","").replace('*','').replace('"','').replace('\\',',').replace(' ','').split(",")
        avg_salary = 0
        max_salary = 0
        if len(data) == 10:

            fullname = data[0]

            if fullname == sys.argv[1]:
                
                avg_OWS = float(data[3])
                avg_DWS = float(data[4])
                max_OWS = float(data[6])
                max_DWS = float(data[7])
                seasons = int(data[9])

                avg_salary = 1485168.37294 * avg_OWS + 1794189.0838 * avg_DWS + 1842699.5473
                max_salary = 1485168.37294 * max_OWS + 1794189.0838 * max_DWS + 1842699.5473  

                int_avg_salary = int(avg_salary)
                int_max_salary = int(max_salary)
                
                print "\n\nPlayer Name: %s\n\nAssume him to be a current player:\n\nCareer Average Level: $%s\n\nBest Season: $%s\n\nActive Seasons: %s\n\n" % (fullname, int_avg_salary, int_max_salary, seasons)

calculation()