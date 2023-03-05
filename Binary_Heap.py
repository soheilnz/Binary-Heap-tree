# Binary_heap:
# { each node can have at most 2children.
#   the value of root node in Min Binary heap is the lowest value among all values of binary tree.
#   & the same for Max binary-heap, root node has the Maximum value among all values of binary-tree.
#   It is complete binary-tree: all levels are completely filled except the last level.}
# WHY WE NEED BINARY-HEAP:
# { finding the Max & the Min value of a tree which takes no longer than o(log N) time and inserting a node
# doesn't take more time than O (log N).}


class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

# Time: O(1)
# Space: O(n=size)


def peekHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

# Time: O(1)
# Space: O(1)


def sizeHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# time: O(1)
# Space: O(1)


def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])

# Time : O(N)
# Space : O(1)


def heapifyInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyInsert(rootNode, parentIndex, heapType)

# Time: O(log N)
# Space: O(log N)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Full"
    else:
        rootNode.customList[rootNode.heapSize + 1] = nodeValue
        rootNode.heapSize += 1
        heapifyInsert(rootNode, rootNode.heapSize, heapType)
        return "Success"

# Time : O(log N)
# Space : O(log N)


def heapifyExtract(rootNode, index, heapType):
    leftIndex = 2 * index
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtract(rootNode, 1, heapType)
        return extractedNode


# Time : O(log N)
# Space : O(log N)


def deleteEntireNode(rootNode):
    rootNode.customList = None

# Time : O(1)
# Space : O(1)


newBHeap = Heap(5)
insertNode(newBHeap, 4, "Max")
insertNode(newBHeap, 5, "Max")
insertNode(newBHeap, 2, "Max")
insertNode(newBHeap, 1, "Max")
# extractNode(newBHeap, "Max")
deleteEntireNode(newBHeap)
levelOrder(newBHeap)
# print(sizeHeap(newBHeap))
