# Michael Godfrey 2020 - Free for use under MIT license. See LICENSE for more details

from collections import namedtuple
import argparse
import numpy as np
import datetime
import os
import urllib.request

ctx = {}

ctx['cache_loc'   ]         = r'C:/Users/<user_name>/FXCACHE/'
ctx['session_sym']          = "EURUSD"
ctx['session_start_date']   = "2019-04-01"
ctx['session_start_hour']   = 0
ctx['session_duration_hrs'] = 24

datetime_begin = datetime.datetime.strptime(ctx['session_start_date'] + ':' + str(ctx['session_start_hour']), '%Y-%m-%d:%H')

def _cached_file_name(sym, year, month, day, hour):
    return '{}_{}_{}_{}_{}h_ticks.bi5'.format(sym, year, '{:0>2}'.format(month), '{:0>2}'.format(day), '{:0>2}'.format(hour))

def cached_file_name(sym, date_time):
    return _cached_file_name(sym, date_time.year, date_time.month, date_time.day, date_time.hour)

    # http://datafeed.dukascopy.com/datafeed/EURUSD/2009/01/01/00h_ticks.bi5
def _dl_file(sym, year, month, day, hour, cache_loc="./cache/"):
    url = 'http://www.dukascopy.com/datafeed/{}/{}/{}/{}/{}h_ticks.bi5'.format(sym, year, '{:0>2}'.format(month - 1), '{:0>2}'.format(day), '{:0>2}'.format(hour))
    dest_file = cache_loc + '{}'.format(_cached_file_name(sym, year, month, day, hour))
    
    print("----------------")
    print("  Caching: " + url)
    print("Cache Loc: " + dest_file)
    print()

    if os.path.exists(dest_file):
        print("File Exists - Skipping: " + dest_file)
    else:
        urllib.request.urlretrieve(url, dest_file)
        print("Saved: " + dest_file)

def dl_file(sym, date_time, cache_loc="./cache/"):
    return _dl_file(sym, date_time.year, date_time.month, date_time.day, date_time.hour, cache_loc)


if __name__ == "__main__":

    for np__index_of_hour in np.arange(ctx['session_duration_hrs'], dtype=np.float64):
        if not os.path.exists(ctx['cache_loc']):
            os.makedirs(ctx['cache_loc'])
            print("Cache Directory does not exist! (creating): " + ctx['cache_loc'])

        time_offset = datetime.timedelta(0, 60 * 60 * np__index_of_hour)
        cache_time  = datetime_begin + time_offset

        cache_file = ctx['cache_loc'] + cached_file_name(ctx['session_sym'], cache_time)
        
        if not os.path.exists(cache_file):
            dl_file(ctx['session_sym'], cache_time, cache_loc=ctx['cache_loc'])
