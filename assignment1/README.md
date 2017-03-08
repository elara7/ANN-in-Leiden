## An implementation for multi-class perceptron algorithm

The objective of this assignment is to develop and evaluate several algorithms for classifying images of handwritten digits. I worked with a simplied version of the famous MNIST data set: a collection of 2707 digits represented by vectors of 256 numbers that represent 16x16 images. The data is split into a training set (1707 images) and a test set (1000 images). These data sets are stored in 4 files: train in.csv, train out.csv, test in.csv, test out.csv, where in and out refer to the input records (images) and the corresponding digits (class labels)

Task 4: Implement a multi-class perceptron algorithm Implement (from scratch) a multi-class perceptron training algorithm and use it for training a single layer perceptron with 10 nodes (one per digit), each node having 256+1 inputs and 1 output. Train your network on the train set and evaluate on both the train and the test set, in the same way as you did in the previous steps.

## The algorithm for training:

First, we initialize 10 groups of weights w at random then we get 10 basic perceptrons.

Each basic perceptrons, for example basic perceptron k, only tell us whether the sample belongs to class k or not.

Using each basic perceptron, we calculate the score a_i =  w_0 + /sum_j x_{ij} * w_j for all the training sample, where i represents the sample, j represents the weight for the jth variable.
 
We set y_i = 0 for all a_i <0, otherwise y_i = 1, then for every sample, each basic perceptron will tell us a number, 0 or 1.

If the output of the basic perceptron matching with the correct class is 1, while others are 0, the sample is said to be correctly classified.

Otherwise the weights of the basic perceptron making wrong judgement need to be modified.

The modify algorithm is:

while (there are misclassified training examples):

- Select a misclassified example (x, ci) (some nodes are activated more than the node ci); 

- 1) update weights of these nodes by -x: w = w - x; 

- 2) update weights of the node ci by x: w = w + x; 

- 3) leave weights of all other nodes unchanged

end-while;

In prediction, we choose the basic perceptron with largest score, for example, perceptron b, as the best predictor for one sample, and then we classified the sample into the class b.

We can choose the the number of iterations to avoid over fitting. In this case, we simplily choose 676 as the number of iterations, which get 0 misclassified sample in training dataset. Finally, we get accuracy 87.8% in testing dataset.

