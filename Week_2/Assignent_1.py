import re


def main():
    regex_file = open('regex_sum_296653.txt', 'r')
    regex_file_buffer = regex_file.read()
    result = re.findall('[0-9]+', regex_file_buffer)

    summy = 0
    for item in result:
        summy += int(item)

    print summy

if __name__ == "__main__":
    main()

