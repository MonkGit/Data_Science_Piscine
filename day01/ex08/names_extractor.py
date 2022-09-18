import sys

def names_extractor():
  with open('employees.tsv', 'a') as file_to_write: 
    file_to_write.write('Name\tSurname\tE-mail\n') 
    with open(sys.argv[1], 'r') as file_to_read:
      line = file_to_read.readlines()
      for l in line:
          if l.isspace():
            return
      for i in range(len(line)):
        name = line[i].split('@')[0].split('.')[0]
        surname = line[i].split('@')[0].split('.')[1]
        file_to_write.write(f'{name.capitalize()}\t{surname.capitalize()}\t{line[i]}')

if __name__ == '__main__':
  if len(sys.argv) != 2:
    raise Exception("Error argument")
  names_extractor()