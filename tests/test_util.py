from movie_recommendation.script import util


def test_euclidean_distance():
    instance1 = [0.1, 0.2, 0.8]
    instance2 = [0.1, 0.8, 0.2]

    return_value = util.euclideanDistance(instance1, instance2, len(instance2))
    expected = 0.8485281374238571
    assert return_value == expected


def test_get_neighbors():
    trainingSet = [[0.1, 0.2, 0.8, 1], [0.6, 0.9, 0.2, 2]]
    testInstance = [0.1, 0.3, 0.8]
    k=2
    return_value = util.get_neighbors(trainingSet, testInstance, k)
    expected = [[0.1, 0.2, 0.8, 1], [0.6, 0.9, 0.2, 2]]
    assert return_value == expected
