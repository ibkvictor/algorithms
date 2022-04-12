def flipAndInvertImage(image):
    n_rows = len(image)
    for row in range(n_rows):
        i = 0
        j = len(image[row]) - 1
        while i < j:
            temp = image[row][i]
            image[row][i] = complement(image[row][j])
            image[row][j] = complement(temp)
            i += 1
            j -= 1
            
            if i == j:
                image[row][i] = complement(image[row][j])
    return image
                
def complement(value):
    if value == 1:
        return 0
    return 1

image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))