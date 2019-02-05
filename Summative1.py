import random,os,csv
from datetime import datetime

inputfile = 'input.txt'

# function to create sublists for a range
def generate_list(array1):
    # store all the sublists
    sublist = []
    # first loop
    for i in range(len(array1) + 1):
        # second loop
        for j in range(i, len(array1) + 1):
            # call function to generate random numbers between 0 and 1 and append to your list
            sub = generate_floats(0,1)
            sublist.append(sub)
    return sublist

def generate_floats(low, high):
    """ Return a list of unique random floats
        in the range of low <= x <= high
    """
    result = []
    seen = set()
    # generate random 16 random floats
    for i in range(16):
        x = random.uniform(low, high)
        while x in seen:
            x = random.uniform(low, high)
        seen.add(x)
        result.append(x)
    return result

def write_to_file(dataframe,filename,times):
    if os.path.exists(filename):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not
    print(append_write)
    highscore = csv.writer(open(filename, append_write))
    for key,val in dataframe.items():
        highscore.writerow([key,val,times])



if __name__ == "__main__":
# driver code
# generate sequential range of object to hold data
 region = list(range(1,33))
# generate 16 float readings for each of the object between 0 and 1
 sensor_readings = generate_list(region)
 print(region)
 # generate dictionary to combine the two lists with region objects being the key and sensor readings as the values
 sensor_data = dict(zip(region, sensor_readings))
 print(sensor_data)
 # time stamp
 now = datetime.now()
 print("timestamp =", now)
 write_to_file(sensor_data,inputfile,now)




