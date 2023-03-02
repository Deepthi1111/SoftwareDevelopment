redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    i = 0
    while i < len(redShirtHeights):
        if redShirtHeights[i] < blueShirtHeights[i]:
            isRedShirtFrontRow = True
            break
        elif redShirtHeights[i] > blueShirtHeights[i]:
            isRedShirtFrontRow = False 
            break
        else:
            i += 1
    
    if isRedShirtFrontRow:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False 
    
    if not isRedShirtFrontRow:
        for i in range(len(redShirtHeights)):
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False 
    
    return True 

print(classPhotos(redShirtHeights, blueShirtHeights))
                
                

    