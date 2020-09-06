# Michael Godfrey 2020 - Free for use under MIT license. See LICENSE for more details

from collections import namedtuple
import datetime
import argparse
import struct
import lzma
import csv
import os

import numpy as np

# https://quant.stackexchange.com/a/35005
TICK_CHUNK_SZ = 20

Tick  = namedtuple('Tick', 'time ask_p bid_p ask_v bid_v')

fn_chunk_parser   = lambda chunk: Tick._make(struct.unpack('>LLLff', chunk))
fn_lzma_iterator  = lambda file, chunk_size: iter(lambda: file.read(chunk_size), b'')
fn_file_not_empty = lambda file: os.stat(file).st_size

def do_it(in_file, out_file):
        bi5_file     = lzma.LZMAFile(in_file, mode="rb")
        bi5_iterator = fn_lzma_iterator(bi5_file, TICK_CHUNK_SZ)
        bi5_tics     = [fn_chunk_parser(chunk) for chunk in bi5_iterator]

        with open(out_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(bi5_tics)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='bi5-csv')

    parser.add_argument('--in_file', required=True, type=str, help='input file or directory [ --in, --i]')
    parser.add_argument('--out_file', type=str, help='output file [--out, --o] (optional: otherwise will be input file ____.csv)')

    args = parser.parse_args()

    if os.path.isdir(args.in_file):
        in_dir = args.in_file
        bi5_files = [bi5_file for bi5_file in os.listdir(in_dir) if bi5_file.endswith('.bi5')]
        for in_file in bi5_files:
            if fn_file_not_empty(in_dir + "\\" + in_file):
                out_file = in_dir +"\\" + in_file[:-3] + "csv"
                do_it(in_dir + "\\"+ in_file, out_file)

    elif fn_file_not_empty(args.in_file):
        out_file = args.out_file if args.out_file else args.in_file[:-3] + "csv"
        do_it(args.in_file, out_file)