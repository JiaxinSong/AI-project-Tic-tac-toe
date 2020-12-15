This neural network module has 3 linear type layers and I used Tanh() as the activation function:

modules = Sequential(Flatten(),
                         Linear(3*board_size*board_size, 30),
                         Tanh(),
                         Linear(30, 10),
                         Tanh(),
                         Linear(10, 1))

input layer with 3*board size*board size units, Tanh activation function, then a hidden layer with 30 units, and a Tanh activation function, finally a output layer with 10 units and output size is 1. 
For the iteration time of gradient descent  to train this model: when the board size is 7,  I run 300 iterations; when the board size is smaller than 7, I run 500 iterations.
