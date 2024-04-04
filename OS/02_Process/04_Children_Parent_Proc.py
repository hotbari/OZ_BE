import psutil

for proc in psutil.process_iter():
    ps_name = proc.name()

    if "Chrome" in ps_name:
        child = proc.children()
        parents = proc.parent()

        print('프로세스 이름: ',ps_name)
        print('프로세스 상태: ',proc.status())
        print('자녀: ', child, '부모: ', parents)
        print()

        if child:
            print(f'{ps_name}의 자식 프로세스', child)
            print()
            print()
