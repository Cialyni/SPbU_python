import functools
import sys
import warnings
import traceback


def traceback_parser(traceback):
    error_place = ""
    tb = traceback.split("\n")[1:]
    tb_line2 = tb[2].split()
    error_place += (
        tb_line2[-4] + " " + tb_line2[-3] + " " + tb_line2[-2] + " " + tb_line2[-1]
    )
    error_place += " in " + tb[3].replace(" ", "")
    return error_place


def safe_call(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            ex_type = str(sys.exc_info()[0]).replace("<class '", "").replace("'>", "")
            ex_comment = str(sys.exc_info()[1])
            ex_place = traceback_parser(traceback.format_exc())
            warnings.warn(
                "\n\033[33mError type: {}\nError text: {}\nError place: {}\033[31m".format(
                    ex_type, ex_comment, ex_place
                )
            )
            return None

    return inner
