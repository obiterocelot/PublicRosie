import ast

def new_warning(member):
    warnmember = '#'.join((member.name, member.discriminator))
    with open('warnings.txt', 'r+') as f:
        data = f.read()
        fulldict = ast.literal_eval(data)
        f.truncate(0)
        f.seek(0)
        for entry in fulldict:
            if warnmember == entry:
                fulldict[entry] += 1
                check_timeout(fulldict[entry])
        if warnmember not in fulldict:
            fulldict[warnmember] = 1
        f.write(str(fulldict))

def check_timeout(strikeno):
    if strikeno >= 3:
        print("timeout")
    else:
        print("send warning")