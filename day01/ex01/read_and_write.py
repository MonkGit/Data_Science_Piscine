def read_and_write():
    file_csv = open('ds.csv')
    file_tsv = open('ds.tsv', 'w')
    file_tsv.write(file_csv.read().replace('\",', '\"\t')\
        .replace('false,', 'false\t'))
    file_csv.close
    file_tsv.close

if __name__ == '__main__':
    read_and_write()
