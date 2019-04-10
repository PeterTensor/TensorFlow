from math import log

#创建数据集
def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','fipper']
    return dataSet,labels

#构建信息熵为度量
def shang(dataSet):
    numEntries = len(dataSet)
    labelsCount = {}
    #currentLabel = []
    for i in dataSet:
        currentLabel = i[-1]
        if currentLabel not in labelsCount.keys():
            labelsCount[currentLabel] = 0
            labelsCount[currentLabel] += 1
    shangEnt = 0.0
    for j in labelsCount:
        #P(x)
        prob = float(labelsCount[j])/numEntries
        #H(x) = -∑P(x)*logP(x)
        shangEnt -= prob * log(prob,2)
    return shangEnt

#split data
def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVector in dataSet:
        if featVector[axis] == value:
            reduceFeat = featVector[:axis]
            reduceFeat.extend(featVector[axis+1:])
            retDataSet.append(reduceFeat)
    return retDataSet

#选择最佳分类器
def chooseBestFeaturnToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = shang(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featlist = [example[i] for example in dataSet]
        uniqueVal = set(featlist)
        newEntropy = 0.0
        for value in uniqueVal:
            subDataSet = splitDataSet(dataSet,i,value)
            prob= len(subDataSet)/float(len(dataSet))
            newEntropy += prob * shang(subDataSet)
        infoGain = baseEntropy - newEntropy
        #print(infoGain)
        if (infoGain > bestInfoGain) :
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

#计算每个标签的频率，类似投票
def majorityCnt(classlist):
    classCount = {}
    for vote in classCount.keys():
        if vote in classlist:
            calssCount[vote] = 0
        calssCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),key = opertor.iteritems(1),reverse = True)
    return sortedClassCount[0][0]

#构建树
def createTree(dataSet,labels):
    classlist = [example[-1] for example in dataSet]
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classlist)
    bestFeat = chooseBestFeaturnToSplit(dataSet)
    bestlabel = labels[bestFeat]
    myTree = {bestlabel : {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestlabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

#分类
def classify(inputTree,featLabels,testVac):
    firstStr_1= inputTree.keys()
    firstStr = (tuple(firstStr_1))[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVac[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classlabel = classify(secondDict[key],featLabels,testVac)
            else:
                classlabel = secondDict[key]
    return classlabel

#保存函数
def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fe.close()

def loadTree(filename):
    import pickle
    fr = open(filename,'r')
    return pickle.load(fr)
    
