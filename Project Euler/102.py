file = open('p102_triangles.txt','r')
triangles = [];
def quad(point):
    if point[0] >= 0:
        if point[1] >= 0:
            return 1
        else:
            return 4
    else:
        if point[1] >= 0:
            return 2
        else:
            return 3
def quadtest(points):
    a = quad(points[0])
    b = quad(points[1])
    c = quad(points[2])
    if a != b:
        return True
    if b != c:
        return True
    if a != c:
        return True
    return False
def testa(points):
    a = points[0]
    b = points[1]
    c = points[2]
    m = a[1] / a[0]
    if b[1] >= b[0] * m and c[1] <= c[0] * m: 
        return True
    if b[1] <= b[0] * m and c[1] >= c[0] * m: 
        return True
    return False
def testb(points):
    b = points[0]
    a = points[1]
    c = points[2]
    m = a[1] / a[0]
    if b[1] >= b[0] * m and c[1] <= c[0] * m: 
        return True
    if b[1] <= b[0] * m and c[1] >= c[0] * m: 
        return True
    return False
def testc(points):
    c = points[0]
    b = points[1]
    a = points[2]
    m = a[1] / a[0]
    if b[1] >= b[0] * m and c[1] <= c[0] * m: 
        return True
    if b[1] <= b[0] * m and c[1] >= c[0] * m: 
        return True
    return False
count = 0
for line in file:
    line = line.strip('\n')
    axis = line.split(',');
    triangle = []
    for i in range(0,len(axis),2):
        triangle.append((int(axis[i]), int(axis[i + 1])))
    if quadtest(triangle):
        if testa(triangle) and testb(triangle) and testc(triangle):
            
            count += 1
print(count)












        
##        triangle.append((int(axis[i]), int(axis[i + 1])))
##    triangles.append(triangle)
##print(triangles)
