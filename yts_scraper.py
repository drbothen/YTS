__author__ = 'jmagady'

from app import yts_api, parg
import sys

def main():

    if len(sys.argv) is 1:  # checks to see if any flags are present. if not display help sys.argv will always be atleats 1.
        parg.print_help()  # displays help
        sys.exit()  # exits the system

    rargs = parg.parse_args(sys.argv[1:])  # parse the args.

    rargs.update




if __name__ == '__main__':
    main()