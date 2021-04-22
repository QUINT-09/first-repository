import cv2
import numpy as np
import csv
import time

a=0
b=0
row=0

while (a < 12):

    while (b < 8):
        img_name_calc=(a,b)
        img_name=(str(img_name_calc) + ".png")
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

        with open('board.csv', newline='') as f:
            board = csv.reader(f)
            for row in board:
                print(row)
                

        """ read_csv = csv.reader(open('board.csv'))
        board = list(read_csv)
        print(board) """

        if r_value < 41 and g_value < 41 and b_value < 41:
            row[a][b] = 1
        
        elif r_value > 214 and g_value > 214 and b_value > 214:
            row[a][b] = 2

        else:
            row[a][b] = 0
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
        cv2.waitKey(0)



        b+=1
    
    a+=2
    b=0