import string

def process_file(fin,header):
    hist = {}

    if header:
        skip_header(fin)

    for line in fin:
        process_line(line,hist)

    return hist

def skip_header(fin):
    for line in fin:
        if line.startswith('[Illustration:]'):
            break

def process_line(line,hist):
    line = line.replace('-',' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        hist[word] = hist.get(word,0) + 1

def main():
    fin = file('fairies_and_folk.txt')
    print process_file(fin, True)

if __name__ == '__main__':
    main()