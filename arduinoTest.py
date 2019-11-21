from pyfirmata import Arduino, util
import time
import sys
from os import system, name

#/******************************************************/
#/* Name of the project:Real-time restraining order   */
#/* Author:Moulid Ahmed     	                     */
#/* 		-Any other info-                        */
#/* Date : 11/08/2019                              */
#/*************************************************/

board = Arduino('/dev/ttyACM0')
print('Start')
arr = []
count = 0
try:
    while 1:
        board.digital[8].write(1)
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
        print(count)
        count += 1
        time.sleep(1)
        board.digital[8].write(0)
        time.sleep(.1)
except KeyboardInterrupt:
    print ('\nEnd')
    board.digital[8].write(0)
