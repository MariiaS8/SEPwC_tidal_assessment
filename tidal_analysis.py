#!/usr/bin/env python3

# import the modules you need here
import argparse
import os
import pandas as pd
import numpy as np


def read_tidal_data(filename_or_directory):
    """
    Read tidal data from file or directory.

    Args:
        filename_or_directory (str): Path to file or directory.

    Returns:
        pd.DataFrame: Tidal data.
    """
    data = []

    if os.path.isdir(filename_or_directory):
        # If directory is provided, read all files within the directory
        directory = filename_or_directory
        filenames = [os.path.join(directory, f)
                     for f in os.listdir(directory) if f.endswith(".txt")]
    else:
        # If a single file is provided, use that file
        filenames = [filename_or_directory]

    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Skip headers
            data_lines = lines[11:]
            # Parse data
            for line in data_lines:
                parts = line.split()
                if len(parts) >= 5:
                    date_time = parts[1] + ' ' + parts[2]

                    # parsing sea level
                    sea_level_str = parts[3]
                    if sea_level_str.endswith(('M', 'T', 'N')):
                        sea_level = np.nan
                    else:
                        sea_level = float(sea_level_str)

                    data.append((date_time,  sea_level))

    data_frame = pd.DataFrame(data, columns=['Time', 'Sea Level'])
    data_frame['Time'] = pd.to_datetime(data_frame['Time'], format='%Y/%m/%d %H:%M:%S')
    data_frame.set_index('Time', inplace=True, drop=False)

    return data_frame




def extract_single_year_remove_mean(year, data):
    """
    Extract data for a single year and remove mean sea level.

    Args:
        year (str): Year to extract.
        data (pd.DataFrame): Tidal data.

    Returns:
        pd.DataFrame: Year data with mean sea level removed.
    """
    year_data = data[data.index.year == int(year)]

    mean_sea_level = year_data['Sea Level'].mean()

    year_data['Sea Level'] -= mean_sea_level

    return year_data


def extract_section_remove_mean(start, end, data):
    """
    Extract data for a section and remove mean sea level.

    Args:
        start (str): Start date.
        end (str): End date.
        data (pd.DataFrame): Tidal data.

    Returns:
        pd.DataFrame: Section data with mean sea level removed.
    """
    start_date = pd.to_datetime(start)
    end_date = pd.to_datetime(end, format='%Y%m%d') + \
        pd.DateOffset(days=1) - pd.DateOffset(seconds=1)

    section_data = data[(data.index >= start_date) & (data.index <= end_date)]

    mean_sea_level = section_data['Sea Level'].mean()

    section_data['Sea Level'] -= mean_sea_level

    return section_data


def join_data(data1, data2):

    return 



def sea_level_rise(data):

                                                     
    return 

def tidal_analysis(data, constituents, start_datetime):


    return 

def get_longest_contiguous_data(data):


    return 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                     prog="UK Tidal analysis",
                     description="Calculate tidal constiuents and RSL from tide gauge data",
                     epilog="Copyright 2024, Jon Hill"
                     )

    parser.add_argument("directory",
                    help="the directory containing txt files with data")
    parser.add_argument('-v', '--verbose',
                    action='store_true',
                    default=False,
                    help="Print progress")

    args = parser.parse_args()
    dirname = args.directory
    verbose = args.verbose
    


