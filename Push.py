import os
os.chdir(os.path.dirname(__file__))
os.system('git log')
commit = input('commit:')
os.system(f'git add . && git commit -m{commit} && git push origin master')
