import sys
import os
import csv
import copy


def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        data = data[0]
    data = [int(i) for i in data]
    process(data)

def process(data):
    original_data = data[:]
    noun = 0
    while(noun <= 99):
        # reset data array
        i = 0
        verb = 0
        data = original_data[:]
        while(verb <= 99):
            # reset data array
            i = 0
            data = original_data[:]
            data[i+1] = noun
            data[i+2] = verb
            while(data[i] != 99):
                index1 = data[i+1]
                index2 = data[i+2]
                index3 = data[i+3]
                if (data[i] == 1):    
                    data[index3] = data[index1] + data[index2]
                    i = i+4
                elif (data[i] == 2):
                    data[index3] = data[index1] * data[index2]
                    i = i+4
            if (data[0] == 19690720):
                print(noun)
                print(verb)
                break
            else:
                verb += 1
        noun += 1

        






if __name__ == '__main__':
    main()