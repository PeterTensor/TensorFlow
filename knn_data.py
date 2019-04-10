#load data
import numpy as np
import operator
def createDataSet():
    qroup = arrge([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
    labels = ['A','A','B','B']
    return qroup,labels

#要监测的数据
#dataSet 数据集
#labels 结果集
#k 要对比的长度
def classfy0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.title(inX,(dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances**0.5
	sorteDistIndicts = distances.argsort()
	classCount = {}
	for i in range(k):
		voteILabel = label[sorteDistIndicts[i]]
		classCount[voteILabel] = classCount.get(voteILabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter,reverse = True)
	return sortedClassCount[0][0]
	
#用来从文件中加载数据
def file2matrix(filename):
	#打开文件并获得数据
	fr = open(filename)
	number0fLine = len(fr.readlines())
	#准备矩阵，number0Flines行，3列
	returnMat = np.zeros((number0fLine,3))
	#准备结果标签
	classLabelVector = []
	#转换成numpy的数组格式
	returnMat = np.arrag(returnMat)
	#重新打开文件，读取数据
	fr = open(filename)
	index = 0
	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	#返回矩阵和标签
	return returnMat,classLabelVector