# ParseARCHIBUSLogFiles
#
# Description: Script to parse large log files from ARCHIBUS
#
# Author:     Marcel Seguin
# Date:       07-April-2021

# declare something to search for
searchString = "2021-06-02 15:10:26"

# variable for the log file name, read as utf-16, and look for the windows newline
logFileName = "archibus.log"
READONLYMODE = 'r'
decodeFormat = 'utf-8'
newLine='\r\n'



# variable for the log file name
errorLogFileName = "ARCHIBUSErrors.txt"
WRITEMODE= 'w'

# open the file
with open(logFileName, READONLYMODE, encoding=decodeFormat, newline = newLine) as fileHandler:
    # read in a line at a time, discard if not useful

    currentLine = fileHandler.readline()
    #currentLine = currentLineRaw.decode(decodeFormat)

    # count all the lines, create a string to hold
    lineNumber = 0
    allErrors = []

    while currentLine:
        lineNumber += 1

        #DEBUG
        #print(currentLine)

        # see if it has error in it, if not discard
        # if it is an error, grab the next line too (hold information)
        if currentLine.find(searchString) != -1:
            allErrors.append("[" + str(lineNumber) + "]  " + str(currentLine))
        
        # read in the next line in and loop
        try:
            currentLine = fileHandler.readline()
            #currentLine = currentLineRaw.decode(decodeFormat)
        except:
            print("[" + str(lineNumber) + "] is not readable")
           

# create a new file to output to
# write all the lines
with open(errorLogFileName, WRITEMODE,encoding=decodeFormat) as fileWriteHandler:
    for line in allErrors:
        fileWriteHandler.write(str(line))

# print it out to the console
for line in allErrors:
    print(line)
    