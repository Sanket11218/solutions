def cordinates(bottom,top):
    return [bottom,[top[0],bottom[1]],top,[bottom[0]],top[1]]

def intersection(bottom1,top1,bottom2,top2):
    result=False
    rec1=cordinates(bottom1,top1)
    rec2=cordinates(bottom2,top2)
    rec1_range=[[bottom1[0],top1[0]],[bottom1[1],top1[1]]]
    rec2_range=[[bottom2[0],top2[0]],[bottom2[1],top2[1]]]
    for item in rec2:
        if item[0] >= rec1_range[0][0] and item[0] <= rec1_range[0][1] and item[1] >= rec1_range[1][0] and item[1] <= rec1_range[1][1]:
            result = True
            break
    for item in rec1:
        if item[0] >= rec2_range[0][0] and item[0] <= rec2_range[0][1] and item[1] >= rec2_range[1][0] and item[1] <= rec2_range[1][1]:
            result= True
            break
    return result
    
if __name__ == "__main__": 
    print intersection(bottom1,top1,bottom2,top2)
