# nn_L2.py
# Python 3.x

import numpy as np
import random
import math

# helper functions

def showVector(v, dec):
  fmt = "%." + str(dec) + "f" # like %.4f
  for i in range(len(v)):
    x = v[i]
    if x >= 0.0: print(' ', end='')
    print(fmt % x + '  ', end='')
  print('')
  
def showMatrix(m, dec):
  fmt = "%." + str(dec) + "f" # like %.4f  
  for i in range(len(m)):
    for j in range(len(m[i])):
      x = m[i,j]
      if x >= 0.0: print(' ', end='')
      print(fmt % x + '  ', end='')
    print('')
	
def showMatrixPartial(m, numRows, dec, indices):
  fmt = "%." + str(dec) + "f" # like %.4f
  lastRow = len(m) - 1
  width = len(str(lastRow))
  for i in range(numRows):
    if indices == True:
      print("[", end='')
      print(str(i).rjust(width), end='')
      print("] ", end='')	  
  
    for j in range(len(m[i])):
      x = m[i,j]
      if x >= 0.0: print(' ', end='')
      print(fmt % x + '  ', end='')
    print('')
  print(" . . . ")

  if indices == True:
    print("[", end='')
    print(str(lastRow).rjust(width), end='')
    print("] ", end='')	  
  for j in range(len(m[lastRow])):
    x = m[lastRow,j]
    if x >= 0.0: print(' ', end='')
    print(fmt % x + '  ', end='')
  print('')	  
  
# -----

def makeData(genNN, numRows, inputsSeed):
  # create train or test data for experimentation
  # using a generating NN with arch and weights supplied
  rnd = random.Random(inputsSeed)  # to create random input values
  lo = -8.0; hi = 8.0  # range of input values
  numFeatures = genNN.ni
  numClasses = genNN.no

  result = np.zeros(shape=[numRows, (numFeatures+numClasses)], dtype=np.float32)  # matrix with both features and classes
  for i in range(numRows):
    for j in range(numFeatures):
      result[i, j] = (hi - lo) * rnd.random() + lo  # could use rnd.uniform(lo, hi) for [lo, hi) OR rnd.gauss(mu, sigma)
    classesCalc = genNN.computeOutputs(result[i])  # only first numFeatures cols used
    maxIdx = np.argmax(classesCalc)  # index of largest value
    result[i, numFeatures + maxIdx] = 1.0  # set the single 1 value for 1-of-N encoding
  return result

# -----
	
class NeuralNetwork:

  def __init__(self, numInput, numHidden, numOutput, seed):
    self.ni = numInput
    self.nh = numHidden
    self.no = numOutput
	
    self.iNodes = np.zeros(shape=[self.ni], dtype=np.float32)
    self.hNodes = np.zeros(shape=[self.nh], dtype=np.float32)
    self.oNodes = np.zeros(shape=[self.no], dtype=np.float32)
	
    self.ihWeights = np.zeros(shape=[self.ni,self.nh], dtype=np.float32)
    self.hoWeights = np.zeros(shape=[self.nh,self.no], dtype=np.float32)
	
    self.hBiases = np.zeros(shape=[self.nh], dtype=np.float32)
    self.oBiases = np.zeros(shape=[self.no], dtype=np.float32)
	
    self.rnd = random.Random(seed) # allows multiple instances
    self.initializeWeights()
 	
  def setWeights(self, weights):
    if len(weights) != self.totalWeights(self.ni, self.nh, self.no):
      print("Warning: len(weights) error in setWeights()")	

    idx = 0
    for i in range(self.ni):
      for j in range(self.nh):
        self.ihWeights[i,j] = weights[idx]
        idx += 1
		
    for j in range(self.nh):
      self.hBiases[j] = weights[idx]
      idx += 1

    for j in range(self.nh):
      for k in range(self.no):
        self.hoWeights[j,k] = weights[idx]
        idx += 1
	  
    for k in range(self.no):
      self.oBiases[k] = weights[idx]
      idx += 1
	  
  def getWeights(self):
    tw = self.totalWeights(self.ni, self.nh, self.no)
    result = np.zeros(shape=[tw], dtype=np.float32)
    idx = 0  # points into result
    
    for i in range(self.ni):
      for j in range(self.nh):
        result[idx] = self.ihWeights[i,j]
        idx += 1
		
    for j in range(self.nh):
      result[idx] = self.hBiases[j]
      idx += 1

    for j in range(self.nh):
      for k in range(self.no):
        result[idx] = self.hoWeights[j,k]
        idx += 1
	  
    for k in range(self.no):
      result[idx] = self.oBiases[k]
      idx += 1
	  
    return result
 	
  def initializeWeights(self):
    numWts = self.totalWeights(self.ni, self.nh, self.no)
    wts = np.zeros(shape=[numWts], dtype=np.float32)
    lo = -0.01; hi = 0.01
    for idx in range(len(wts)):
      wts[idx] = (hi - lo) * self.rnd.random() + lo
    self.setWeights(wts)

  def computeOutputs(self, xValues):
    hSums = np.zeros(shape=[self.nh], dtype=np.float32)
    oSums = np.zeros(shape=[self.no], dtype=np.float32)

    for i in range(self.ni):
      self.iNodes[i] = xValues[i]

    for j in range(self.nh):
      for i in range(self.ni):
        hSums[j] += self.iNodes[i] * self.ihWeights[i,j]

    for j in range(self.nh):
      hSums[j] += self.hBiases[j]
	  
    for j in range(self.nh):
      self.hNodes[j] = self.hypertan(hSums[j])

    for k in range(self.no):
      for j in range(self.nh):
        oSums[k] += self.hNodes[j] * self.hoWeights[j,k]

    for k in range(self.no):
      oSums[k] += self.oBiases[k]
 
    softOut = self.softmax(oSums)
    for k in range(self.no):
      self.oNodes[k] = softOut[k]
	  
    result = np.zeros(shape=self.no, dtype=np.float32)
    for k in range(self.no):
      result[k] = self.oNodes[k]
	  
    return result
	
  def train(self, trainData, maxEpochs, learnRate, L2=False, lamda=0.0):
    hoGrads = np.zeros(shape=[self.nh, self.no], dtype=np.float32)  # hidden-to-output weights gradients
    obGrads = np.zeros(shape=[self.no], dtype=np.float32)  # output node biases gradients
    ihGrads = np.zeros(shape=[self.ni, self.nh], dtype=np.float32)  # input-to-hidden weights gradients
    hbGrads = np.zeros(shape=[self.nh], dtype=np.float32)  # hidden biases gradients
	
    oSignals = np.zeros(shape=[self.no], dtype=np.float32)  # output signals: gradients w/o assoc. input terms
    hSignals = np.zeros(shape=[self.nh], dtype=np.float32)  # hidden signals: gradients w/o assoc. input terms

    epoch = 0
    x_values = np.zeros(shape=[self.ni], dtype=np.float32)
    t_values = np.zeros(shape=[self.no], dtype=np.float32)
    numTrainItems = len(trainData)  # often just 'n'
    indices = np.arange(numTrainItems)  # [0, 1, 2, . . n-1]  # rnd.shuffle(v)
	
    while epoch < maxEpochs:
      self.rnd.shuffle(indices)  # scramble order of training items
	  
      for ii in range(numTrainItems):
        idx = indices[ii]  # get curr training item

        for j in range(self.ni):
          x_values[j] = trainData[idx, j]  # get the input values	
        for j in range(self.no):
          t_values[j] = trainData[idx, j+self.ni]  # get the target values
        self.computeOutputs(x_values)  # results stored internally
		
        # 1. compute output node signals
        for k in range(self.no):
          derivative = (1 - self.oNodes[k]) * self.oNodes[k]  # softmax
          oSignals[k] = derivative * (t_values[k] - self.oNodes[k])  # t - o 





        # 2. compute hidden-to-output weight gradients using output signals
        for j in range(self.nh):
          for k in range(self.no):
            hoGrads[j,k] = oSignals[k] * self.hNodes[j]
            if L2 == True:
              hoGrads[j,k] += lamda * self.hoWeights[j,k]



			
        # 3. compute output node bias gradients using output signals
        for k in range(self.no):
          obGrads[k] = oSignals[k] * 1.0  # 1.0 dummy input can be dropped
		  
        # 4. compute hidden node signals
        for j in range(self.nh):
          sum = 0.0
          for k in range(self.no):
            sum += oSignals[k] * self.hoWeights[j,k]
          derivative = (1 - self.hNodes[j]) * (1 + self.hNodes[j])  # tanh activation
          hSignals[j] = derivative * sum
		 
        # 5 compute input-to-hidden weight gradients using hidden signals
        for i in range(self.ni):
          for j in range(self.nh):
            ihGrads[i,j] = hSignals[j] * self.iNodes[i]
            if L2 == True:
              ihGrads[i,j] += lamda * self.ihWeights[i,j]

        # 6. compute hidden node bias gradients using hidden signals
        for j in range(self.nh):
          hbGrads[j] = hSignals[j] * 1.0  # 1.0 dummy input can be dropped

        # update weights and biases using the gradients
		
        # 1. update input-to-hidden weights
        for i in range(self.ni):
          for j in range(self.nh):
            delta = learnRate * ihGrads[i,j]
            self.ihWeights[i,j] += delta
			
        # 2. update hidden node biases
        for j in range(self.nh):
          delta = learnRate * hbGrads[j] * 1.0  # can drop the dummy 1.0 input
          self.hBiases[j] += delta      
		  
        # 3. update hidden-to-output weights
        for j in range(self.nh):
          for k in range(self.no):
            delta = learnRate * hoGrads[j,k]
            self.hoWeights[j,k] += delta
			
        # 4. update output node biases
        for k in range(self.no):
          delta = learnRate * obGrads[k]
          self.oBiases[k] += delta
 		  
      epoch += 1
	  
      if epoch % 100 == 0:
        mse = self.meanSquaredError(trainData)
        print("epoch = " + str(epoch) + " ms error = %0.4f " % mse)
        # ws = self.getWeights()
        # showVector(ws, 8)
    # end while
   
    result = self.getWeights()
    return result
  # end train
  
  def accuracy(self, tdata):  # train or test data matrix
    num_correct = 0; num_wrong = 0
    x_values = np.zeros(shape=[self.ni], dtype=np.float32)
    t_values = np.zeros(shape=[self.no], dtype=np.float32)

    for i in range(len(tdata)):  # walk thru each data item
      for j in range(self.ni):   # peel off input values from curr data row 
        x_values[j] = tdata[i,j]
      for j in range(self.no):  # peel off target values from curr data row
        t_values[j] = tdata[i, j+self.ni]

      y_values = self.computeOutputs(x_values)  # computed output values
      max_index = np.argmax(y_values)  # index of largest output value 

      if abs(t_values[max_index] - 1.0) < 1.0e-5:
        num_correct += 1
      else:
        num_wrong += 1

    return (num_correct * 1.0) / (num_correct + num_wrong)

  def meanSquaredError(self, tdata):  # on train or test data matrix
    sumSquaredError = 0.0
    x_values = np.zeros(shape=[self.ni], dtype=np.float32)
    t_values = np.zeros(shape=[self.no], dtype=np.float32)

    for ii in range(len(tdata)):  # walk thru each data item
      for jj in range(self.ni):  # peel off input values from curr data row 
        x_values[jj] = tdata[ii, jj]
      for jj in range(self.no):  # peel off target values from curr data row
        t_values[jj] = tdata[ii, jj+self.ni]

      y_values = self.computeOutputs(x_values)  # computed output values
	  
      for j in range(self.no):
        err = t_values[j] - y_values[j]  # (t-o)^2 - t-o is most common order
        sumSquaredError += err * err
		
    return sumSquaredError / len(tdata)
          
  @staticmethod
  def hypertan(x):
    if x < -20.0:
      return -1.0
    elif x > 20.0:
      return 1.0
    else:
      return math.tanh(x)

  @staticmethod	  
  def softmax(oSums):
    result = np.zeros(shape=[len(oSums)], dtype=np.float32)
    m = max(oSums)
    divisor = 0.0
    for k in range(len(oSums)):
       divisor += math.exp(oSums[k] - m)
    for k in range(len(result)):
      result[k] =  math.exp(oSums[k] - m) / divisor
    return result
	
  @staticmethod
  def totalWeights(nInput, nHidden, nOutput):
   tw = (nInput * nHidden) + (nHidden * nOutput) + nHidden + nOutput
   return tw

# end class NeuralNetwork

def main():
  print("\nBegin NN L2 regularization demo \n")
  
  print("Generating dummy training and test data \n")
  genNN = NeuralNetwork(10, 15, 4, 0)  # a 10-15-4 NN with seed = 0
  genNumWts = NeuralNetwork.totalWeights(10,15,4)
  # make weights for the generating NN
  genWeights = np.zeros(shape=[genNumWts], dtype=np.float32)
  genRnd = random.Random(3)
  genWtHi = 9.9; genWtLo = -9.9
  for i in range(genNumWts):
    genWeights[i] = (genWtHi - genWtLo) * genRnd.random() + genWtLo
  genNN.setWeights(genWeights)
  
  dummyTrainData = makeData(genNN, numRows=200, inputsSeed=11)  # 200 rows train data
  dummyTestData = makeData(genNN, 40, 13)  # 40 rows of test data, different input values
  print("Dummy training data: \n")
  showMatrixPartial(dummyTrainData, 4, 1, True)  # show first 4 rows to 1 decimals with indexes shown 
   
  numInput = 10
  numHidden = 8
  numOutput = 4
  print("\nCreating a %d-%d-%d neural network classifier" % (numInput, numHidden, numOutput) )
  nn = NeuralNetwork(numInput, numHidden, numOutput, seed=0)  # set  
  
  maxEpochs = 500
  learnRate = 0.01
  print("\nSetting maxEpochs = " + str(maxEpochs))
  print("Setting learning rate = %0.3f " % learnRate)
  
  print("\nStarting training without L2 regularization")
  nn.train(dummyTrainData, maxEpochs, learnRate)  # no L2
  print("Training complete")
  
  accTrain = nn.accuracy(dummyTrainData)
  accTest = nn.accuracy(dummyTestData)
  
  print("\nAccuracy on train data no L2 regularization = %0.4f " % accTrain)
  print("Accuracy on test data no L2 regularization  = %0.4f " % accTest)
  
  L2_rate = 0.005
  nn = NeuralNetwork(numInput, numHidden, numOutput, seed=0)  # reset 
  print("\nStarting training with L2 regularization ( L2 rate = %0.3f ) " % L2_rate)
  nn.train(dummyTrainData, maxEpochs, learnRate, L2=True, lamda=L2_rate)  # with regularization
  print("Training complete")
  
  accTrain = nn.accuracy(dummyTrainData)
  accTest = nn.accuracy(dummyTestData)
  
  print("\nAccuracy on train data with L2 regularization = %0.4f " % accTrain)
  print("Accuracy on test data with L2 regularization = %0.4f " % accTest)
  
  print("\nEnd demo \n")
   
if __name__ == "__main__":
  main()

# end script
