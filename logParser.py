from XLLog import XLLog


def main(log_file_name="log.log", decode_format="utf-8", new_line="\r\n", error_log_file_name="error.txt"):
    log = XLLog(log_file_name,decode_format,new_line,error_log_file_name)

    # ask the user for lines to print
    input("Please Enter # of Lines to print(0-1000): ")

    log.

if __name__ == "__main__":
    main()