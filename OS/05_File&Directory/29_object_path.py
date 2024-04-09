import os
import pathlib

# current working dir
for p in pathlib.Path.cwd().glob('*.txt'):
    # 전체 경로
    new_p = os.path.join(p.parent, p.name)
    print(new_p)