import os,sys

def cls():
 os.system('cls')
 print('\n{:^135}\n\n{:^135}\n\n'.format(' '.join("python @ mehta's"),' '.join('version - '+sys.winver)))

sys.ps1='hm> '
sys.ps2='--> '

cls()
  