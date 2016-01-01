import base64

def obfusc(filelocation, outfile = None):
    if isinstance(filelocation,basestring):
        try:
            return obfusc_string(file(filelocation).read())
        except:
            return obfusc_string(filelocation)

    if isinstance(filelocation,file):
        return obfusc_string(filelocation.read())

def dobfusc(filelocation, outfile = None):
    if isinstance(filelocation,basestring):
        try:
            return dobfusc_string(file(filelocation).readl())
        except:
            return dobfusc_string(filelocation)
    if isinstance(filelocation,file):
        return dobfusc_string(filelocation.read())


def obfusc_string(s):
    return base64.b64encode(s.encode('zlib'))

def dobfusc_string(s):
    return base64.b64decode(s).decode('zlib')
