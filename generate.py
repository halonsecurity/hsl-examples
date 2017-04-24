# Usage: Generate a config file of all HSL examples that can then be imported to Halon

import base64
import re
import os

def fix_path(n):
    return re.sub(r'[^a-z0-9]', r'', n)[0:16]

def get_config_file(filepath):
    name = map(fix_path, filepath.replace('.hsl', '').split(os.path.sep))
    code = base64.b64encode(open(filepath, 'r').read())
    return 'file__examples' + '.'.join(name) + '="|text/x-hsl|' + code + '"'

def find_hsl_files(directory):
    f = []
    for (root, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.hsl':
                f.append(root + os.path.sep + filename)
    return f

for f in find_hsl_files('.'):
    print(get_config_file(f))