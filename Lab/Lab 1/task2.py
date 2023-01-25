#TASK_2_of_19101444

region_matrix = []

with open('Question2 input1.txt') as text:

    text_lines_1 = text.readlines()[0:2]
    print(text_lines_1)

with open('Question2 input1.txt') as text:

    text_lines_2 = text.readlines()[2:]
    print(text_lines_2)

for text_line in text_lines_2:
    region_matrix.append(text_line.split())
#region_matrix
time=0
for column in range(len(region_matrix)):
    for row in range(len(region_matrix[column])):

        if region_matrix[column][row] =='A':
            region_matrix[column][row] = 1
        elif region_matrix[column][row] =='H':
            region_matrix[column][row] = 0
        else:
            region_matrix[column][row] = -1

        #row_size = len(region_matrix)
        #column_size = len(region_matrix[0])

def track(region):
    result = 0
    
    for c in range(len(region)):
        for r in range(len(region[c])):

            if region[c][r] == 0:
               counter = BFS(region, c, r)
               result = max(result, counter)

    return result

def BFS(region, c, r):
    global time
    if any([c<0, r<0, c>=len(region), r>=len(region[0])]):
        return 0
    
    if region[c][r] == 0:
        return 0
    count = 0

    region[c][r] = 0

    position = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for column, row in enumerate(position):
    
            if any( [column!=c, row!=r]):
                region[column][row]= 1
                if region[c][r] == 0:
                    count = count +1
                    time= time+1

            count = count + BFS( region, column, row)

    return count
   

survived = track(region_matrix)

print("Time:", time, "minutes")
print(survived, "survived")