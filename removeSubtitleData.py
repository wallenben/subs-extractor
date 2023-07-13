import re
import sys

def clean_srt(file_name, output_file):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        # Check if the line is not an empty line, a timestamp line or an index line
        if line.strip() and not re.match('^\d+$', line.strip()) and not re.match('^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$', line.strip()):
            cleaned_lines.append(line.strip())

    cleaned_text = ' '.join(cleaned_lines)

    with open(output_file, 'w') as f:
        f.write(cleaned_text)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    clean_srt(input_file, output_file)

