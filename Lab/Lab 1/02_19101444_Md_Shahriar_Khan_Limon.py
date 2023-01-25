#Task_1_of_19101444

region_matrix = []

with open('input.txt') as text:

    text_lines = text.readlines()
    #print(text_lines)

for text_line in text_lines:
    region_matrix.append(text_line.split())
#region_matrix

for column in range(len(region_matrix)):
    for row in range(len(region_matrix[column])):

        if region_matrix[column][row] =='Y':
            region_matrix[column][row] = 1
        else:
            region_matrix[column][row] = 0

#row_size = len(region_matrix)
#column_size = len(region_matrix[0])

def track(region):
    result = 0
    
    for c in range(len(region)):
        for r in range(len(region[c])):

            if region[c][r] == 1:
               counter = DFS(region, c, r)
               result = max(result, counter)

    return result

def DFS(region, c, r):

    if any([c<0, r<0, c>=len(region), r>=len(region[0])]):
        return 0
    
    if region[c][r] == 0:
        return 0

    count = 1

    region[c][r] = 0

    for column in range( c-1,c+2):
        for row in range( r-1, r+2):

            if any( [column!=c, row!=r]):
                count = count + DFS( region, column, row)

    return count
   

maximum_region = track(region_matrix)

print("Maximum region is:", maximum_region)