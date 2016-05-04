import csv
import sys
from collections import Counter
from operator import itemgetter

def open_file(filename):
    '''
    Open the USD_CAD.csv file and arrange the data
    into a list of lists

    Returns: list of lists
    '''

    data_list = []
    with open(filename) as f:
        exchange_reader = csv.reader(f)
        for line in exchange_reader:
            data_list.append(line)
    return data_list



def clean_data(data_list):
    '''
    Take the list of lists from the USD_CAD.csv file
    and select the usable data.

    Returns: list of tuples
    '''


    tup_list = []
    for row in data_list:
        try:
            tup_list.append((str(row[0]), float(row[2])))
        except:
            pass
    return tup_list


def calculate_diffs(tup_list):
    '''
    Take the list of tuples and create relevant
    engineered data.  The data is to focus on
    dates and a difference between exchange rate and
    rate given at the airport.

    Returns: list of tuples
    '''

    new_tups = []
    for i in xrange(len(tup_list)-1):
        new_tups.append((tup_list[i+1][0], tup_list[i+1][1]-tup_list[i][1]))
    return new_tups




def pretty_output(new_tups):
    '''
    Implement a counter on differences and join the dictionary
    on a return to format the histogram. Prints the result.

    Prints a date of greatest difference.

    Returns: None
    '''
    rounded_tups = []
    for tup in new_tups:
        rounded_tups.append((tup[0], round(tup[1],2)))

    max_date = max(new_tups, key=itemgetter(1))[0]
    max_val = max(new_tups, key=itemgetter(1))[1]

    c = Counter(zip(*rounded_tups)[1])
    s = "\n".join(["{}: {}".format(k,v) for k,v in sorted(c.iteritems())])
    s1 = "\nDay(s) with biggest gain ({}): {}".format(max_val, max_date)
    return s+s1

def main():
    if len(sys.argv) < 2:
        print "Please select a file for import"
        return
    if (str(sys.argv[1]) != "data/usd_cad.csv"):
        print "Please select the appropriate .csv file for import"
        return
    #print len(sys.argv)
    #print str(sys.argv[0])

    filename = sys.argv[1]
    data_list = open_file(filename)
    tup_list = clean_data(data_list)
    new_tups = calculate_diffs(tup_list)
    print pretty_output(new_tups)



if __name__ == "__main__":
    main()
