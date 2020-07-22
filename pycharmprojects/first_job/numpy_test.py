import numpy as np

from numpy.linalg import *


def main():
    print(np.ones([3,2]))
    print(np.random.randn(2,4))
    print(np.random.randint(4,6,9))
    print(np.random.choice([34,54,54],2))
    lst = np.arange(1,5).reshape([2,-1])
    print(np.log(2))
    print(lst)
    print(lst**3)
    print(np.dot(lst,lst))
    lst2=np.hstack((lst,lst))
    print(lst2)
    print(np.split(lst2, 2))

    print(np.copy(lst))
    print(np.eye(3))
    print(lst)
    print(inv(lst))
    print(lst.transpose())
    print(det(lst))
    print(eig(lst))
    print()
    y = np.array([[5.],
                  [7.]])
    print("solve")
    print(solve(lst,y))

if __name__ == '__mai_':
    main()