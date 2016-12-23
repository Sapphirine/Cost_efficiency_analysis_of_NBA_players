
"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.
"""

import sys
import csv
from collections import defaultdict


def construct_line( label, line ):
	new_line = []


	new_line.append( label )

	for i, item in enumerate( line ):
		if item == '':
			continue
		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
	label_index = int( sys.argv[3] )
except IndexError:
	label_index = 0

try:
	skip_headers = sys.argv[4]
except IndexError:
	skip_headers = 0

i = open( input_file, 'rb' )
o = open( output_file, 'wb' )

reader = csv.reader( i )

if skip_headers:
	headers = reader.next()

for line in reader:
	label = line.pop( label_index )
	if int(label) < 2000000:
		label = "0"
	elif int(label) < 6000000:
		label = "1"
	elif int(label) < 10000000:
		label = "2"
	elif int(label) < 15000000:
		label = "3"
	elif int(label) < 20000000:
		label = "4"
	else:
		label = "5"  
	new_line = construct_line( label, line )
	o.write( new_line )