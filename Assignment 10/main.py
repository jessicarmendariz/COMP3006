import argparse
import os
from program.autompg import AutoMPGData
from program.custom_logger import my_logger

#Takes No Arguments And Creates And Returns An Argument Parser With log, save, y, and m
def my_parser():
    parser = argparse.ArgumentParser(description="Process auto-mpg Data.")
    parser.add_argument("log", type=str, help="Name of Log File my_log.log")
    parser.add_argument("save", type=str, help="Store Output In Log File.")
    parser.add_argument("-y", "--year", action="store_true", help="Sort Data By Year")
    parser.add_argument("-m", "--mpg", action="store_true", help="Sort Data By MPG")
    return parser

if __name__ == "__main__":
    args = my_parser().parse_args()
    log_file = os.path.join(args.log, "my_log.log")
    save_folder = args.save
