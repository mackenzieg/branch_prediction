#~/usr/bin/python

import random;

number_of_branches = 10000;
memory_size_bytes = 256;

data = open("training_data.txt", "w");

for i in range(number_of_branches):
    data.write(str(random.randint(0, memory_size_bytes - 1)) + " " 
        + str(random.randint(0, 1)) + "\n");

