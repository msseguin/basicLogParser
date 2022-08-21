# ParseLogFileLogFiles
#
# Description: Script to parse large log files from LogFile
#
# Author:     Marcel Seguin
# Date:       07-April-2021


from distutils.log import error


# class XLLog:
# Class to define large logfiles and methods to parse them
class XLLog:

    # CONSTANTS
    READONLYMODE = 'r'
    WRITEMODE= 'w'

    # DEBUG VARIABLES
    # declare something to search for
    searchString = "2021-06-02 15:10:26"

    # variable for the log file name, read as utf-16, and look for the windows newline
    log_file_name = "LogFile.log"
    decode_format = 'utf-8'
    new_line='\r\n'

    # variable for the log file name
    error_log_file_name = "LogFileErrors.txt"
    

    # def __init__(self,log_file_name, decode_format, new_line, error_log_file_name):
    # constructor
    def __init__(self,log_file_name, decode_format, new_line, error_log_file_name):
        self.log_file_name = log_file_name
        self.decode_format = decode_format
        self.new_line = new_line
        self.error_log_file_name = error_log_file_name



    def search_lines(self):
        # open the file
        with open(self.log_file_name, self.READONLYMODE, encoding=self.decode_format, newline = self.new_line) as fileHandler:
            # read in a line at a time, discard if not useful
            currentLine = fileHandler.readline()

            # count all the lines, create a string to hold
            lineNumber = 0
            allErrors = []

            while currentLine:
                lineNumber += 1

                # see if it has error in it, if not discard
                # if it is an error, grab the next line too (hold information)
                if currentLine.find(searchString) != -1:
                    allErrors.append("[" + str(lineNumber) + "]  " + str(currentLine))
                
                # read in the next line in and loop
                try:
                    currentLine = fileHandler.readline()
                except:
                    print("[" + str(lineNumber) + "] is not readable")

            
    # def write_results(results):
    # create a new file to output to
    # write all the lines
    def write_results(results):
        with open(self.error_log_file_name, self.WRITEMODE,encoding=self.decode_format) as fileWriteHandler:
            for line in results:
                fileWriteHandler.write(str(line))


    # def print_lines_log(lines)
    # print it out to the console
    def print_lines_log(lines):
        for line in lines:
            print(line)



    # def  read_first_x_lines(log,count_lines):
    # Allow for manual inspection
    def  read_first_x_lines(self,line_count):


        with open(self.log_file_name, self.READONLYMODE, encoding=self.decode_format, newline = self.new_line) as fileHandler:
        # read in a line at a time, discard if not useful

            current_line = fileHandler.readline()

            # count all the lines, create a string to hold
            line_number = 0

            while line_count > line_number and current_line:
                line_number += 1

                # read in the next line in and loop
                try:
                    current_line = fileHandler.readline()
                except:
                    print("[" + str(lineNumber) + "] is not readable")
            