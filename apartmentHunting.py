blocks = [
    {
        "gym": False,
        "school": True,
        "store": False,
    },
    {
        "gym": True,
        "school": False,
        "store": False,
    },
    {
        "gym": True,
        "school": True,
        "store": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,        
    },
    {
        "gym": False,
        "school": True,
        "store": True,
    },
]
reqs = ["gym", "school", "store"]

# Can I update the blocks array ? 
"""
Algorithm:
1) Will update the proximity of the reqs whereever it is set to False, will replace this bool information with the facility's availability how many blocks away.
2) Will navigate the blocks from left to right once and right to left once and update the minProximity, that way if in the second travel we get a better proximity we could 
take min(both)
3) Now average distance to walk will be average of the proximities of all 3 requirements given. True = 0.
4) Whichever block has the lowest average is the answer.

"""

# Time: O(b * r) where b is the number of blocks and r is the number of reqs.
# Space: O(b) 
def apartmentHunting(blocks, reqs):  
    checkDistancesFromLeftToRight(blocks, reqs)
    checkDistancesFromRightToLeft(blocks, reqs)
    updateBlockDataToPureDistances(blocks, reqs)
    preferredBlockIdx = getPreferredBlockIdx(blocks, reqs)
    return preferredBlockIdx

def checkDistancesFromLeftToRight(blocks, reqs):
    for req in reqs:
        reqIdx = None 
        for blockIdx in range(len(blocks)):
            if blocks[blockIdx][req] == True:
                reqIdx = 0
            else:
                if reqIdx is not None:
                    reqIdx += 1
                    blocks[blockIdx][req] = reqIdx    

def checkDistancesFromRightToLeft(blocks, reqs):
    for req in reqs:
        reqIdx = None 
        for blockIdx in reversed(range(len(blocks))):
            if blocks[blockIdx][req] == True:
                reqIdx = 0
            else:
                if reqIdx is not None:
                    reqIdx += 1
                    blocks[blockIdx][req] = reqIdx           

def updateBlockDataToPureDistances(blocks, reqs):
    for block in blocks:
        for req in reqs:
            if type(block[req]) is bool and block[req]:
                block[req] = 0 

def getPreferredBlockIdx(blocks, reqs):
    maxWalkDistanceOfBlocksToReqs = []
    preferredBlockIdx = None
    preferredBlockWithMinDistance = float("inf")
    for blockIdx in range(len(blocks)):
        maxWalkDistanceOfReqs = float("-inf")
        for req in reqs:
            if blocks[blockIdx][req] > maxWalkDistanceOfReqs:
                maxWalkDistanceOfReqs = blocks[blockIdx][req]

        maxWalkDistanceOfBlocksToReqs.append(maxWalkDistanceOfReqs)
        if maxWalkDistanceOfReqs < preferredBlockWithMinDistance:
            preferredBlockWithMinDistance = maxWalkDistanceOfReqs
            preferredBlockIdx = blockIdx

    return preferredBlockIdx            
        

print(apartmentHunting(blocks, reqs))

