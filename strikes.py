import ast

def get_dict():
    with open('warnings.txt', 'r+') as f:
        data = f.read()
        fulldict = ast.literal_eval(data)
        return fulldict

def issue_warning(member):
    warnmember = '#'.join((member.name, member.discriminator))
    fulldict = get_dict()
    for entry in fulldict:
        if warnmember == entry:
            fulldict[entry] += 1
    if warnmember not in fulldict:
        fulldict[warnmember] = 1
    append_dict(fulldict)
    return fulldict

def append_dict(fulldict):
    with open('warnings.txt', 'r+') as f:
        f.truncate(0)
        f.seek(0)
        f.write(str(fulldict))

def check_timeout(member):
    fulldict = get_dict()
    search = '#'.join((member.name, member.discriminator))
    for entry in fulldict:
        if search == entry:
            if fulldict[entry] >= 3:
                return True
            else:
                return False