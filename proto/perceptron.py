#~/usr/bin/python

class perceptron:
    def __init__(self, depth):
        self.weights = [0] * depth;
        self.training = True;

    def give_prediction(self, history, branched):
        # give a initial weight of 1 give initial offset
        weight = 1;
        for i in range(len(history)):
            '''
            since branch taken or not is 0 for not and 1 for taken we need to
            map 0 to -1 since neural network needs to either add or subtract
            a weight
            '''
            weight += self.weights[i] * (-1 if history[i] == 0 else 1);
        # branch if weight is above 0 else treat as no branch 

        if (weight <= training_theta and self.training):
            self.train(history, branched);
        else:
            self.training = False;
            
        return weight > 0;

    def train(self, history, branched):
        if (not self.training):
            return;

        for i in range(len(history)):
            self.weights[i] = self.weights[i] + (1 if branched > 0 else -1) * history[i];

    def is_training(self):
        return self.training;

class stack:
    def __init__(self, depth):
        self.depth = depth;
        self.__storage = [0] * depth;

    def push(self, p):
        if (len(self.__storage) >= self.depth):
            self.__storage = self.__storage[:-1];
        self.__storage.append(p);

    def get_as_array(self):
        return self.__storage;


history_depth = 64;
num_perceptrons = 4;
memory_size_bytes = 256;
training_theta = 10.0;     

history_reg = stack(history_depth);

data = open("training_data.txt");

perceptrons = [];

for i in range(num_perceptrons):
    perceptrons.append(perceptron(history_depth));

for line in data:
    line     = line.rstrip('\n');
    address  = int(line.split(' ')[0]);
    branched = int(line.split(' ')[1]);
    
    map_mem_percep = address / (memory_size_bytes / num_perceptrons);

    active_perceptron = perceptrons[map_mem_percep];

    predicted = active_perceptron.give_prediction(history_reg.get_as_array(), branched);

    if (predicted == branched):
        print "Gussed correctly: " + str(map_mem_percep);
    else:
        print "Gussed incorrectly: " + str(map_mem_percep);

    history_reg.push(branched);

data.close();

