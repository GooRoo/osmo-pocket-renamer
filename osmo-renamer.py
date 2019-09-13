import argparse
import os
import sys

from datetime import datetime
from dateutil.tz import tzlocal
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        prog='osmo-renamer.py',
        description='The tool scans the folder (recursively) and renames the files imported from DJI Osmo Pocket to a more human-readable format (i.e. YYYYMMDD_hhmmss)',
    )
    parser.add_argument('dir', metavar='DIR', type=Path, help='The folder to scan')

    return parser.parse_args()

def get_timestamp(path):
    return int(path.stem.rsplit('_', 1)[-1]) / 1000

def get_nice_date(path):
    ugly_date = get_timestamp(path)
    return datetime.fromtimestamp(ugly_date, tz=tzlocal()).strftime('%Y%m%d_%H%M%S')

def update_date(path, date):
    os.utime(path, (date, date))

def rename_file(old_path, new_path):
    timestamp = get_timestamp(old_path)
    print(f'{old_path.name} => {new_path.name}')
    old_path.replace(new_path)
    update_date(new_path, timestamp)

def rename_osmo_file(path):
    nice_date = get_nice_date(path)

    new_path = path.with_name(f'{nice_date}{path.suffix}')
    rename_file(path, new_path)

def rename_osmo_pano(path):
    nice_date = get_nice_date(path)

    new_path = path.with_name(f'{nice_date}_pano_{path.stem.split("_")[1]}{path.suffix}')
    rename_file(path, new_path)

def main():
    dir = parse_args().dir

    if dir.is_dir():
        print(f'Scanning "{dir.resolve()}":')

        for file in dir.rglob('org_*'):
            rename_osmo_file(file)

        for file in dir.rglob('pano_*'):
            rename_osmo_pano(file)
    else:
        print(f'The path {dir} does not represent a directory', file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
