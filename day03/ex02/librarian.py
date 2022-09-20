import sys
import os
import subprocess

def main():
    if not os.getenv('VIRTUAL_ENV'):
        print('Can not find Virtual Environment')
    else:
        print('You are in Virtual Environment {}'.format(os.environ['VIRTUAL_ENV']))
    if os.environ['VIRTUAL_ENV'][-9:] != 'slaree_02':
        raise Exception('Wrong Virtual Environment')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'beautifulsoup4', 'Pytest'])
    subprocess.run([sys.executable, '-m', 'pip', 'freeze'], stdout=open('requirements.txt', 'w'))
    subprocess.run(['cat', 'requirements.txt'])

if __name__ == '__main__':
    main()
    subprocess.run(['tar', '-czf', 'slaree_02.tgz', 'slaree_02'])
    # tar -xvf slaree_02.tgz    