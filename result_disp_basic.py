import sys

def calculation():
    for line in sys.stdin:
        data = line.replace('"','').replace('\\',',').replace(' ','').split(",")
        salary = 0
        if len(data) == 11:

            fullname = data[0]
            other = data[1]

            if fullname == sys.argv[1]:
                
                pts = float(data[2])
                efg = float(data[3])
                trb = float(data[4])
                ast = float(data[5])
                stl = float(data[6])
                blk = float(data[7])
                tov = float(data[8])
                fls = float(data[9])
                real_salary = int(data[10])
                salary = pts*684444.855969+efg*9839921.01093+trb*757039.214731+ast*533534.390447-stl*-394590.475556+blk*875621.762752-tov*316303.440869-fls*1602925.19751-5334004.93775

                int_salary = int(salary)
                distance = real_salary - int_salary
                
                print "\n\nPlayer: %s\n\nCalculated Salary: %s\n\nReal Salary: %s\n\n\nDistance: %s\n\n" % (fullname, int_salary, real_salary, distance)

calculation()