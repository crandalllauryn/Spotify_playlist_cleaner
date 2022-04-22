# ask user for how many streaming files they have
# add all the files of streaming data from spotify
# make new file with every single song data to cross reference
# ask for playlist name
# cross reference sings with input playlist name
# if the songs in playlist match songs from streaming put into dic
# sort data
# compare streaming hours and give the user top 50 least listened to songs

import argparse
import json
import os
import sys

DEFAULT_SPOTIFY_DATA = ''
DEFAULT_SPOTIFY_PLAYLIST = ''


def get_user_spotify_data():
    parser = argparse.ArgumentParser(
        description="Get user input",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-j", "--jsonfile", default='',
                        help='JSON file to users spotify data')
    args = parser.parse_args()

    if not os.path.isfile(args.jsonfile):
        print(f'Error: {args.jsonfile} does not exist')
        sys.exit(1)


def get_user_spotify_playlist():
    parser = argparse.ArgumentParser(
        description="Get user input",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-j", "--jsonfile", default='',
                        help='JSON file to users spotify playlist they want cleaned')
    args = parser.parse_args()

    if not os.path.isfile(args.jsonfile):
        print(f'Error: {args.jsonfile} does not exist')
        sys.exit(1)


def read_spotify_data(filepath):
    with open(filepath, 'rt', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    return json.loads(txt)


def read_playlist_data(filepath):
    with open(filepath, 'rt', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    return json.loads(txt)


def write_txt_file(text, filepath, show_message=True):
    with(open(filepath, 'w', encoding='utf-8')) as f:
        f.write(text)
    if show_message:
        print(f'Generated {filepath}')

