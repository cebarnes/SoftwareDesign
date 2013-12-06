import string

def process_file(fin,header):
    t = []

    if header:
        skip_header(fin)

    for line in fin:
        process_line(line,t)

    return t

def skip_header(fin):
    for line in fin:
        if line.startswith('[Illustration:]'):
            break

def process_line(line,t):
    line = line.replace('-',' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        t.append(word)

def name(t, pre_len):
    d = {}
    for i in list(range(len(t)))[::pre_len]:
        f = tuple(t[i:i+pre_len])
        if f[:-1] in d.keys():
            d[f[:-1]].extend(f[-1])
        else:
            d[f[:-1]] = [f[-1]]

    return  d

def main():
    fin = file('fairies_short.txt')
    t = process_file(fin, True)
    print name(t,3)

if __name__ == '__main__':
    main()