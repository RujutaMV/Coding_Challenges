# Find all task codes in the text with using regular expression

import re
q8_input = '''Working on QA-456 task.
Trying to finish soon. Then will continue
with GH-12.'''
q8_output = re.findall(r'[A-Z]+-[0-9]*', q8_input)  # change it
print(f'{q8_output=}')
print(f'\n{"=" * 10}\n')
