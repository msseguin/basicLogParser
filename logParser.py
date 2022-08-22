from XLLog import XLLog


def main(log_file_name="log.log", decode_format="utf-8", new_line='\n', error_log_file_name="error.txt"):
    log = XLLog(log_file_name,decode_format,new_line,error_log_file_name)

    # ask the user for lines to print
    line_count = int(input("Please Enter # of Lines to print(0-1000): "))

    # print those lines
    log.print_lines_log(line_count)

    # ask if they want to write all errors
    search_string = str(input("Please Enter a String to Search for:"))

    log.write_results(search_string)


if __name__ == "__main__":
    main()