#!/usr/bin/env python

# script usage
if __name__ == "__main__":
    # execute only if run as a script

    # command line interface
    # https://docs.python.org/3/library/argparse.html
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Some Description.')

    # positional arguments: input output file
    parser.add_argument('infile',
                        nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin,
                        help='Input file. Use stdin if empty.')
    parser.add_argument('-o', '--outfile',
                        nargs='?', type=argparse.FileType('wt'),
                        default=None,
                        const=True,
                        help='Output file. Derive from input file if not speciefied.')

    args = parser.parse_args()

    if args.outfile:
        if type(args.outfile) == bool:
            # derive from infile
            if args.infile == sys.stdin:
                outfile = sys.stdout
            else:
                outfile = args.infile.rsplit('.',1)
        else:
            outfile = args.outfile

        # print outfile

        # write text to outfile
        text = 'Huhu there!'
        if outfile == sys.stdout:
            outfile.write(text)
        else:
            # file opened by add_argument type parameter already
            # with open(outfile, 'wt') as f:
            outfile.write(text)

