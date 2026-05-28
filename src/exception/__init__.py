import sys

def error_message_detail(error: Exception, error_detail:sys) -> str:
    """
    Extracts detailed error information including file name,
    line number and error message.
    """

    _, _, exc_tb = error_detail.exc_info()
    # sys.exc_info() returns tuples of 3 values - exception type, exception_value, traceback_object

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    # exc_tb -> traceback object (where did error occur)
    # .tb_frame.f_code.co_filename -> to get the file_path of that code

    error_message = (
        f"Error occured in python script: [{file_name}] at line number [{line_number}]:{str(error)}"
    )
    
    return error_message

class MyException(Exception):
    """
    Custom exception class for handling errors with detailed traceback info. 
    """
    def __init__(self, error_message, error_detail:sys):
        # Call the base Exception class constructor with the error message
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self) -> str:
        return self.error_message