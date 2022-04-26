import math
from typing import List
import operator


def euclideanDistance(instance1: List[float], instance2: List[float], length: int):
    """Calculate Euclidean Distance.
    sqrt[(x2 – x1)^2 + (y2 – y1)^2]
    Args:
        instance1 (List[int]): An instance of int list used during metric calculation (x1).
        instance2 (List[int]): An instance of int list used during metric calculation (x2).
        length (int): An lenght of instance2 list.
    """
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def cosine_similarity(v1, v2, length):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(length):
        x = v1[i]
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / math.sqrt(sumxx * sumyy)


def get_neighbors(trainingSet: List[List[float]], testInstance: List[float], k: int):
    """Calculate Euclidean Distance and select K entries.
    Args:
        trainingSet (List[float]): An instance of float list used to pass metric calculation.
        testInstance (List[float]): An instance of float list used to pass metric calculation.
        k (int): k-nearest.
    """
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        # dist = cosine_similarity(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
