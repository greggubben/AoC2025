#
# Advent of Code Template
#
import argparse
import sys
import time
from datetime import datetime

#
# Define the arguments for today's puzzle
# Default:
#   filename as the puzzle input
#   verbose for printing extra information
#
parser = argparse.ArgumentParser(
                    description='Advent of Code template.')
#                    epilog='Text at the bottom of help')
parser.add_argument('filename')
parser.add_argument('-d', '--debug',
                    action='store_true',
                    help='print extra information while running')


#
# Global Variables
#

class COLOR:
   BLACK = '\033[30m'
   RED = '\033[31m'
   BRIGHTRED = '\033[91m'
   GREEN = '\033[32m'
   BRIGHTGREEN = '\033[92m'
   YELLOW = '\033[33m'
   BRIGHTYELLOW = '\033[93m'
   BLUE = '\033[34m'
   BRIGHTBLUE = '\033[94m'
   MAGENTA = '\033[35m'
   PURPLE = '\033[95m'
   CYAN = '\033[36m'
   BRIGHTCYAN = '\033[96m'
   WHITE = '\033[37m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#
# Print only if debugging
#
DEBUG = False
def debugPrint(s=""):
    if DEBUG:
        print(s)


#
# Load the file into a data array
#
def loadData(filename):

    lines = []

    f = open(filename)
    for line in f:
        line = line.strip()
        lines.append(line)
    f.close()

    return lines


#
# Print Array
#
def printLines(lines):

    for line in lines:
      debugPrint(line)


#
# Main
#
def main():
    global DEBUG

    args = parser.parse_args()
    
    filename = args.filename
    print(f"Input File: {filename}")
    
    DEBUG = args.debug
    print(f"     Debug: {DEBUG}")

    print()

    # Load data
    lines = loadData(filename)
    debugPrint(f"Lines Read: {len(lines)}")
    debugPrint()
    printLines(lines)

    # Do Part 1 work
    print()
    answer = "X"
    print()
    print(f"{COLOR.CYAN}Part 1 Answer: {COLOR.YELLOW}{answer}{COLOR.END}")

    # Do Part 2 work
    #print()
    answer = "X"
    #print()
    #print(f"{COLOR.CYAN}Part 2 Answer: {COLOR.YELLOW}{answer}{COLOR.END}")


if __name__ == "__main__":
    now = datetime.now()
    print(f"Started at: {now.strftime("%Y-%m-%d %H:%M:%S")}")
    print()

    start = time.perf_counter()
    main()
    end = time.perf_counter()

    elapsedTime = end - start

    # Format the elapsed time into something more human readable
    elapsedTimeStr = f"{elapsedTime}"
    if elapsedTime < 10**-3:
      elapsedTime = elapsedTime * 10**6
      elapsedTimeStr = f"{elapsedTime:.03f} micro secs"
    elif elapsedTime < 1:
      elapsedTime = elapsedTime * 10**3
      elapsedTimeStr = f"{elapsedTime:.03f} milli secs"
    elif elapsedTime < 60:
      elapsedTimeStr = f"{elapsedTime:.03f} seconds"
    else:
      millis = elapsedTime % 1
      millis = int(millis*10**3)
      elapsedTime = int(elapsedTime)
      seconds = int(elapsedTime % 60)
      elapsedTime = int(elapsedTime/60)
      minutes = int(elapsedTime % 60)
      hours = int(elapsedTime/60)
      elapsedTimeStr = f"Elapsed time: {hours:0d}:{minutes:02d}:{seconds:02d}.{millis:03d}"

    print()
    print(f"Elapsed time: {elapsedTimeStr}")
    now = datetime.now()
    print(f"Ended at: {now.strftime("%Y-%m-%d %H:%M:%S")}")
