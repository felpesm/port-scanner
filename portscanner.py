#!/usr/bin/env python3

import json

from portscanner.argumentparser import ArgumentParser, help_message
from portscanner.core import ScanController, ScanTarget


def main():
    arg_parser = ArgumentParser()

    if not arg_parser.has_valid_args():
        help_message()

    st = ScanTarget(arg_parser.ip, arg_parser.methods_ports)
    ps = ScanController(st)

    if arg_parser.json:
        results = ps.scan_to_list(arg_parser.threads)
        json_object = json.dumps(results, default=lambda sr: sr.__dict__(), indent=4)
        print(json_object)

    else:
        print('Scanning for IP {}'.format(arg_parser.ip))
        print('METHOD\tPORT\tSTATUS')
        ps.scan(arg_parser.threads)


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        exit()
