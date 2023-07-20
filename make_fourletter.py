PATHNAME = '/Users/ajz/Dropbox/personal/etexts-dropbox/mwords/CROSSWD.TXT'

with open(PATHNAME) as fh:
    for line in fh:
        line = line.strip()
        if not line.isalpha():
            continue
        if len(line) == 4:
            print(line)
