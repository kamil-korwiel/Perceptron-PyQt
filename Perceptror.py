# from random import random
# Learning Rate: Used to limit the amount each weight is corrected each time it is updated.
# Epochs: The number of times to run through the training data while updating the weight.

import numpy as np
# import matplotlib.pyplot as plt
from numpy.random.mtrand import randint


class Perceptron(object):


    def __init__(self, n_inputs, n_epoch=100, learning_rate=0.5):
        self.n_inputs = n_inputs
        self.weights = np.random.rand(self.n_inputs + 1) - 0.5
        self.n_epoch = n_epoch
        self.learning_rate = learning_rate

    def train(self, training_data, labels):
        for epoch in range(self.n_epoch):
            for input, label in zip(training_data, labels):
                prediction = self.predict(input)
                #print(f"label: {label}")
                if prediction != label:
                    error = self.error(prediction,label)
                    #print(f'weights1: {self.weights[1:]}')
                    self.weights[1:] += self.learning_rate * error * input
                    # print(f'weights2: {self.weights[1:]}')
                    # print(f"weights{self.weights[1:]}")
                    self.weights[0] += self.learning_rate * error * 1 #<-- baisa
            
    # def showGraf(self,setdata,labels):
    #     for p,l in zip(setdata,labels):
    #         if l==0:
    #             plt.scatter(p[0], p[1], color = "blue")
    #         else:
    #             plt.scatter(p[0], p[1], color = "green")
    #     a = -self.weights[1]/ self.weights[2]
    #     b=  -self.weights[0]/ self.weights[2]
    #     lt = [] 
    #     for i in range(10):
    #         lt.append(a*i+b)
    #     plt.plot(lt)

    #     plt.show()

    def trainWithPocket(self, training_data, targets):
        pocket = []
        pastaccuracy = 0.0
        for epoch in range(self.n_epoch):
            
            for input, target in zip(training_data, targets):
                prediction = self.predict(input)
                error = self.error(prediction,target)

                accuracy = self.accuracy(training_data,targets)
                if accuracy >= pastaccuracy:
                    pastaccuracy = accuracy
                    pocket = self.weights
                
                self.weights[1:] += self.learning_rate * error * input
                self.weights[0] += self.learning_rate * error
        self.weights = pocket
        # self.showGraf(training_data,targets)

    def trainWithPocket2(self, training_data, targets):
        
        t = 0
        t_prim = 0
        weights_prim = self.weights[1:]
        weight_zero_prim =  self.weights[0]
        for epoch in range(self.n_epoch):
            for input, target in zip(training_data, targets):
                prediction = self.predict(input)
                error = self.error(prediction,target)
                if prediction == target:
                    t = t + 1
                else:
                    if t > t_prim:
                        t_prim = t 
                        weights_prim = self.weights[1:]
                        weight_zero_prim =  self.weights[0]
                        self.updateWeights(input,error)
        # self.showGraf(training_data,targets)

    def trainWithPocket3(self, training_data, targets):
        t = 0
        t_prim = 0
        weights_prim = self.weights[1:]
        weight_zero_prim =  self.weights[0]
        for epoch in range(self.n_epoch):
            for i in self.randListInts(len(training_data)):

                prediction = self.predict(training_data[i])
                error = self.error(prediction,targets[i])
                if prediction == targets[i]:
                    t = t + 1
                else:
                    if t > t_prim:
                        t_prim = t 
                        weights_prim = self.weights[1:]
                        weight_zero_prim =  self.weights[0]
                        self.updateWeights(training_data[i],error)
        self.weights[1:] = weights_prim
        self.weights[0] = weight_zero_prim
        # self.showGraf(training_data,targets)
        
        # self.showGraf(training_data,targets)

    def randListInts(self, size):
        rand_ints = []
        rn = 0
        for _ in range(size):
            rn = np.random.randint(0,size)
            while rn in rand_ints:
                rn = np.random.randint(0,size)
            # print(rn in rand_ints)
            rand_ints.append(rn)
        return rand_ints

    def updateWeights(self,input,error):
        self.weights[1:] += self.learning_rate * error * input
        self.weights[0] += self.learning_rate * error
    # #First
    def predict(self,inputs):
        sumation = 0.0
        sumation = self.weights[0]
        for input,weight in zip(inputs,self.weights[1:]):
            sumation += input*weight
        return self.acctivation_fn(sumation)

    def accuracy(self,inputs,targets):
        errors = 0.0
        for input, target in zip(inputs, targets):    
            prediction = self.predict(input)
            errors += abs(self.error(prediction,target))
        return 1 - (errors/len(inputs))
    #   _|-
    def acctivation_fn(self,variable):
        threshold = 0.0
        return 1.0 if (variable>=threshold) else 0.0

    def error(self,prediction,target): # Zad. 5. Napisac funkcj Error
        return target - prediction





# dataset = np.array([
#         [2.7810836,2.550537003,0],
#         [1.465489372,2.362125076,0],
#         [3.396561688,4.400293529,0],
#         [1.38807019,1.850220317,0],
#         [3.06407232,3.005305973,0],
#         [7.627531214,2.759262235,1],
#         [5.332441248,2.088626775,1],
#         [6.922596716,1.77106367,1],
#         [8.675418651,-0.242068655,1],
#         [7.673756466,3.508563011,1]
#     ])


# perceptron = Perceptron(2)

# print("____________FIRST_____________")
# for vec in dataset:
#     p = perceptron.predict(vec[:-1])
#     print("Predic {0}  Answer = {1}".format(p,vec[-1]))


# print(f"accuracy: {perceptron.accuracy(dataset[:,:-1],dataset[:,-1:])}")
# # perceptron.showGraf(dataset[:,:-1],dataset[:,-1:])
# print("\n____________LAST_____________")

# perceptron.trainWithPocket3(dataset[:,:-1],dataset[:,-1:])

# for vec in dataset:
#     p = perceptron.predict(vec[:-1])
#     print("Predic {0}  Answer = {1}".format(p,vec[-1]))

# print(f"accuracy: {perceptron.accuracy(dataset[:,:-1],dataset[:,-1:])}")

# print(perceptron.randListInts(10))