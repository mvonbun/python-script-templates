#!/usr/bin/env python

# define functions and classes here
# can also be used as a module

# if using python 2.7
from __future__ import print_function



# # files
# def file_operations():
#     with open('somefile', 'r') as f:
#         data_read = f.read()

#     with open('somefile', 'w') as f:
#         f.write("Huhu")

#     import pickle
#     with open('somefile.p', 'rb') as f:
#         data_read = pickle.load(f)

#     with open('somefile.p', 'wb') as f:
#         pickle.dump(data_write, f)    


# def 
# # dictionaries
# new_dict = dict()
# new_dict = {}
# new_dict['key1'] = 'Value1'
# new_dict['key2'] = [1,2,3]

# new_dict = dict(key1='Value1',
#                 key2=[1,2,3])
# new_dict = {'key1':'Value1',
#             'key2':[1,2,3]}
    
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
                        help='optional input file')
    parser.add_argument('outfile',
                        nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='optional output file')

    # options with arguments
    parser.add_argument('-z', '--zeroplus',
                        nargs='*',
                        help='zero or more arguments')
    parser.add_argument('-o', '--oneplus',
                        nargs='+',
                        help='one or more arguments')
    parser.add_argument('-v', '--variable',
                        nargs='?',
                        default='option not provided',
                        const='option without argument provided',
                        help='zero or one arguments')


    # switch
    parser.add_argument('-s', '--switch',
                        help='this is a switch',
                        action='store_true', default=False)

    args = parser.parse_args()

    if args.zeroplus:
        print("Huhu")

    if args.infile == sys.stdin:
        print("Input is stdin")
    else:
        print("File input")
        
