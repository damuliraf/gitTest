import random,os,csv
from datetime import datetime
# create object that has an error entry
input = {
        1: [0.92449172417756, 0.3879508659737114, 0.027867387295444246, 0.6125289126019289, 0.6343409925023675, 0.4920967019367889, 0.9802862512361544, 0.3248427035488546, 0.26764532990118295, 0.713024808398727, 0.1131698261075692, 0.5410136697292157, 0.6780778496737824, 0.8472970343818814, 0.3742918575554446, 0.7382195438860794],
        2: [0.6996090503072266,0.8055522911678762 , 0.8055522911678762,'err', 0.5514886555237676, 0.3957714209161518, 0.1478432528559971, 0.13713312160086188, 0.14892603049767383, 0.2829003114347103, 0.021186696333209798, 0.7878090223683613, 0.2893392558558976, 0.8040089736638477, 0.005481304932905107, 0.4961591959000998, 0.17714731824582042]
    }

# function to search for occurance of text in submitted
def find_by_value(data, target):
    for key, value in data.items():
         for i in range(len(value)):
            if value[i] == target:
                #print(value[i], i, key)
                return [key,i]

# function to write to log file
def write_to_file(dataframe,filename,times):
    if os.path.exists(filename):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not
    #print(append_write)
    highscore = csv.writer(open(filename, append_write))
    highscore.writerow([times,dataframe])


if __name__ == '__main__':

    x = find_by_value(input, 'err') # Text Search

   # If statement to process response
    if x is None:
        print("no error")
    else:
        now = datetime.now()
        y = "Error is at sensor {} and node {}".format(x[0], x[1])
        write_to_file(y,"log_file",now)