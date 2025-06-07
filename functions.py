def new_point(p,r,fixed_points):
    '''This generates a new point which is rth distance away'''
    next_sub_iter = set()
    for point in fixed_points:
        next_sub_iter.add((point[0]*(1-r)+r*p[0],point[1]*(1-r)+r*p[1]))
    return next_sub_iter

def iterate(n,r,fixed_points):
    iter_list = [fixed_points]
    next_iter = set()
    # Itterate loop
    for i in range(n):
        for point in iter_list[-1]:
            next_iter = next_iter.union(new_point(point,r,fixed_points)) 
        iter_list.append(next_iter)
    return iter_list[-1]


