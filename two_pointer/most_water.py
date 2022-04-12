import time
def maxArea(height):
    max_left = max(height[:-1])
    max_area = -56000
    
    j = len(height) - 1
    i = 0
    while i < j:
        height_ = height[j] if height[j] <= height[i] else height[i]
        area = height_ * (j - i)
        if height[i] >= height[j]:
            if area > max_area:
                max_area = area
                break
        else:
            if area > max_area:
                max_area = area
                i += 1
        if height[j] >= max_left and i == j - 1:
            print(max_left, height[j], j, i)
            break
        elif i == j - 1:
            i = 0
            j -= 1
    return max_area

def maxArea2(height):
    max_left = max(height)
    max_area = -56000
    
    j = len(height) - 1
    i = 0
    while i < j:
        print(i, j)
        height_ = height[j] if height[j] <= height[i] else height[i]
        area = height_ * (j - i)
        if max_area < area:
            max_area = area
        print(i)
        if height[j] == max_left:
            if i >= j - 1:
                break
        if height[i] >= height[j]:
            print("why")
            print(height[i], height[j])
            i = 0
            j -= 1
        
    return max_area

start = time.time_ns()                
height = [1,2,4,3]
print(maxArea2(height))
print(time.time_ns() - start)
