import cv2
import numpy as np
import csv
import time
import itertools

read_csv = csv.reader(open('src/default_board.csv'))
board = list(read_csv)

a=0
b=0
row=0

while (a < 12):

    while (b < 8):
        img_name_calc=(a,b)
        img_name=("src/" + str(img_name_calc) + ".png")
        print(img_name)
        img = cv2.imread(img_name)
        height, width, _ = np.shape(img)

        # calculate the average color of each row of our image
        avg_color_per_row = np.average(img, axis=0)

        # calculate the averages of our rows
        avg_colors = np.average(avg_color_per_row, axis=0)

        # avg_color is a tuple in BGR order of the average colors
        # but as float values
        print(f'avg_colors: {avg_colors}')

        # so, convert that array to integers
        int_averages = np.array(avg_colors, dtype=np.uint8)
        r_value = int_averages[2]
        g_value = int_averages[1]
        b_value = int_averages[0]

        """ with open("board.csv") as csvBoard:
            board=list(csv.reader(csvBoard)) """

        """ with open('board.csv', newline='') as f:
            board = csv.reader(f)
            for row in board:
                print(row) """

        

        
        print(board)
        print(type(board))
        print(board[b][a])


        if r_value < 41 and g_value < 41 and b_value < 41:
            board[b][a] = 1
        
        elif r_value > 214 and g_value > 214 and b_value > 214:
            board[b][a] = 2

        else:
            board[b][a] = 0

        print(board[b][a])
        print(board)

        """ while row < 8:
            csv.writer(open('board.csv', 'w')).writerow(board[row])
            time.sleep(0.1)
            row+=1
        row=0
         """

        # create a new image of the same height/width as the original
        average_image = np.zeros((height, width, 3), np.uint8)
        # and fill its pixels with our average color
        average_image[:] = int_averages

        # finally, show it side-by-side with the original
        cv2.imshow("Avg Color", np.hstack([img, average_image]))
        cv2.waitKey(250)



        b+=1
    
    a+=1
    b=0


with open('src/board.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=',')
    writer.writerows(board)

#pieces = [x for x in board if x != 0]

pieces = board

pieces = list(itertools.chain.from_iterable(pieces))

while pieces.count(0) > 0:
    pieces.remove(0)

def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

pieces_amount = get_number_of_elements(pieces)

if (pieces_amount != 32):
    pass
    #TODO add logic to retake foto
else: 
    print("bob")