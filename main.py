import argparse
import json

import check
import gui
import installer

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=argparse.FileType('r'), default=None)
parser.add_argument('--nogui', action='store_true')
args = parser.parse_args()

if args.config is not None:
    config = json.load(args.config)
else:
    config = None

if args.nogui and config is not None:
    if not all(check.configuration(config)):
        raise Exception('Invalid configuration')
    else:
        installer.run(config)
else:
    window = gui.MainWindow(config)
    window.run()

exit(0)
