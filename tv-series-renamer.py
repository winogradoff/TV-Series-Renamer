import os
import re
import collections
import argparse
from collections import Counter
from typing import Dict, Tuple, List, Any

RENAME_PATTERN = r'(.*)\s*(S\d{2}E\d{2}).*(\..*)'


def parse_args():
    parser = argparse.ArgumentParser(description='Rename series files. Useful for services like Plex.')
    parser.add_argument('path', type=str, help='path to directory with files')
    parser.add_argument('-i', '--info', help="do not make changes, just show rename suggestions", action="store_true")
    args = parser.parse_args()
    return args


def create_suggestions(file_names: List[str]) -> Tuple[List[str], Dict[str, str]]:
    prefix_counter: Counter[str] = collections.Counter()
    suggestions: Dict[str, str] = dict()

    print('Looking for files in a directory...')
    for filename in sorted(file_names):
        match = re.search(RENAME_PATTERN, filename, flags=re.IGNORECASE)
        if match:
            series_name = re.compile(r'(\W+)').sub(' ', match[1]).strip()
            prefix_counter[series_name] += 1
            season_and_episode = match[2].lower()
            extension = match.groups()[-1][1:]
            suggestion = "{}.{}".format(season_and_episode, extension)
            suggestions[filename] = suggestion
        else:
            print("[WARN] File name does not match renaming pattern: {}".format(filename))

    common_prefixes = [x[0] for x in prefix_counter.most_common(3)]
    return common_prefixes, suggestions


def rename_files(dir_path: str, prefix: str, suggestions: Dict[str, str]):
    print("Renaming...")
    for old_filename, suggestion in suggestions.items():
        old_path = os.path.abspath("{}/{}".format(dir_path, old_filename))
        new_path = os.path.abspath("{}/{}".format(dir_path, "{} {}".format(prefix, suggestion)))
        os.rename(old_path, new_path)
    print("Done!")


def main():
    args = parse_args()
    (dir_path, _, file_names) = next(os.walk(args.path))

    common_prefixes, suggestions = create_suggestions(file_names)

    if len(common_prefixes) > 1:
        print("Common prefixes:")
        for p in common_prefixes:
            print(p)

    most_common_prefix = common_prefixes[0]

    input_prefix = input('Enter prefix (empty for "{}"): '.format(most_common_prefix)).strip()
    prefix = most_common_prefix if input_prefix == '' else input_prefix

    print('Rename suggestions:')
    for old_filename, suggestion in suggestions.items():
        print("{} -> {}".format(old_filename, "{} {}".format(prefix, suggestion)))

    if args.info:
        return

    answer = input("Press y for continue: ").lower().strip()
    if answer != 'y':
        print("Сanceled.")
        return

    rename_files(dir_path, prefix, suggestions)


if __name__ == '__main__':
    main()
