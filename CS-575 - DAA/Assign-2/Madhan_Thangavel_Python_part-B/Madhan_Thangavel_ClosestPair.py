# A divide and conquer program in Python3  to find the smallest distance from a given set of points.
from operator import itemgetter
import math

# Function to load the co-ordinates.
def load_coordinate_pairs(file_name):
    with open(file_name) as file:
        return [tuple(map(float, i.split(' '))) for i in file]

# Function to sort the points.
def y_sort(points):
    return sorted(points, key=itemgetter(1))

# A utility function to find the distance between two points
def distance(pi, pj):
    return math.sqrt(((pi[0] - pj[0]) ** 2) + ((pi[1] - pj[1]) ** 2))

# A utility function to find the distance beween the closest points of strip of given size.
# They all have an upper bound on minimum distance as d.
# Note that this method seems to be a O(n^2) method, but it's a O(n) method as the inner loop runs at most 6 times
def min_distance(points):
    # Default minimum distance: distance between first two points
    d = distance(points[0], points[1])
    pair = points[0], points[1]

    # Pick all points one by one and  try the next points till the difference
    # between y coordinates is smaller than d.
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if distance(points[i], points[j]) < d:
                d = distance(points[i], points[j])
                pair = points[i], points[j]
    return d, pair

# All points in # strip[] are sorted accordint to y coordinate.
def strip_min_distance(strip, d):
    # Default to current min distance and pair
    min_d = d[0]
    pair = d[1]

    # i+j specifies index that strip[i] is being compared to
    # If i+j > len(strip), then comparison index is out of range
    # strip[i] will be compared to next 7 points OR to remaining points in strip, whichever is shorter
    for i in range(len(strip)):
        for j in range(1, 8):
            if i + j < len(strip) and distance(strip[i], strip[i + j]) < min_d:
                min_d = (distance(strip[i], strip[i + j]))
                pair = strip[i], strip[i + j]
    return min_d, pair

# A recursive function to find the smallest distance. The array  contains
# all points sorted according to its coordinate using Divide and Conquer algorithm
def closest(x, y):
    if len(x) <= 3:
        return min_distance(x)
    # Divide and Conquer
    middle = math.ceil(len(x) / 2)

    # Partitioned x and y lists
    xl = x[:middle]
    xr = x[middle:]
    yl = []
    yr = []

    # Creates partitioned y lists
    for point in y:
        if point in xl:
            yl.append(point)
        else:
            yr.append(point)

    dl = closest(xl, yl)
    dr = closest(xr, yr)

    min_d = min(dl, dr)

    # Define strip
    strip = []

    # Appends coordinate if within d of vertical line
    for point in y:
        if abs(point[0] - x[middle][0]) < min_d[0]:
            strip.append(point)

    min_d = min(min_d, strip_min_distance(strip, min_d))
    return min_d


# Driver Code
if __name__ == '__main__':
    print("Program Starts to determine closest pair both in 2-D & 3-D")
    test_files = ['InputFile.txt']
    coordinate_planes = [load_coordinate_pairs(file) for file in test_files]

    # Opening the output file
    file = open("OutputFile.txt", "w")

    # Sort coordinate_planes by x coordinate in-place
    [plane.sort() for plane in coordinate_planes]
    y_sorted = [y_sort(plane) for plane in coordinate_planes]

    solutions = [closest(x_sorted_plane, y_sorted_plane)
                 for x_sorted_plane, y_sorted_plane in zip(coordinate_planes, y_sorted)]
    # Writing in the output file
    for i in range(len(solutions)):
        file.write('\nThe closest distance between two pairs in {0} is:\n{1:.10f}: {2}<--->{3}\n'
                .format(test_files[i], solutions[i][0],solutions[i][1][0], solutions[i][1][1]))
    print("Program Ends !")
    print("output is saved in OutputFile.txt")
    # Closing the output file
    file.close()