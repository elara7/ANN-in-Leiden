## An implementation for multi-class perceptron algorithm

The objective of this assignment is to develop and evaluate several algorithms for classifying images of handwritten digits. I worked with a simplied version of the famous MNIST data set: a collection of 2707 digits represented by vectors of 256 numbers that represent 16x16 images. The data is split into a training set (1707 images) and a test set (1000 images). These data sets are stored in 4 files: train in.csv, train out.csv, test in.csv, test out.csv, where in and out refer to the input records (images) and the corresponding digits (class labels)

Task 4: Implement a multi-class perceptron algorithm Implement (from scratch) a multi-class perceptron training algorithm (to be discussed on 15 Feb.) and use it for training a single layer perceptron with 10 nodes (one per digit), each node having 256+1 inputs and 1 output. Train your network on the train set and evaluate on both the train and the test set, in the same way as you did in the previous steps.

The algorithm:

initialize weights w at random 

while (there are misclassified training examples):

- Select a misclassified example (x, ci) 
	
- Then some nodes are activated more than the node ci 

- 1) update weights of these nodes by -x: w = w - x; 

- 2) update weights of the node ci by x: w = w + x; 

- 3) leave weights of all other nodes unchanged

end-while;

