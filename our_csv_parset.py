

import os 

#myfilename = "housing.data.txt"

#if os.path.isfile(myfilename):
#    print("Yay, i have a file")
#else:
#    print("boo, no files for me")

with open(myfilename, 'r') as file_handle:
    # line = file_handle.readlines()
     for line in file_handle.readlines():
         line_clean = line.replace('   ' , ' ').replace('  ', ' ')
         line_clean = line_clean.strip()
         print(values)
         for value in values:
             print(float(value))
      # print(line)
      # print(line.split(' '))
        print ( 'finished!')
