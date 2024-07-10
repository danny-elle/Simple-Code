import sys

# Check if file is an argument
if len(sys.argv) < 2:
    print("Usage: python read_even_lines.py <input_file>")
    sys.exit(1)

# Open file and print even numbered lines
with open (sys.argv[1]) as infile:
    line_num = 1;

    for line in infile.readlines():
        if line_num % 2 == 0:
            print(line_num,":", line.strip())
        line_num = line_num + 1
