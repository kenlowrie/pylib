import os

__all__ = ['context', 'ntpx', 'TEMPDIR', 'USER', 'COMPUTER']

TEMPDIR = '/temp'
USER = ''
COMPUTER = ''

class context:
    """
    Provides context to a Python module with several useful methods.

    The context object provides methods to give useful context to a Python module.
    Things like current location, fully qualified script name, an alias and more.

    when you instantiate one of these, you pass in __file__ if defined,
    otherwise sys.argv[0]
    """

    def __init__(self, foo, alias=None):
        self._whoami = os.path.abspath(foo)
        self._whereami,whocares = os.path.split(self._whoami)
        
        name,ext = os.path.splitext(whocares)

        if alias is None:
            self._alias = name
        else:
            self._alias = alias

    def whoami(self):
        """Returns the fully qualified name of the current module"""
        return self._whoami

    def alias(self):
        """Returns the alias (shortname) of the current module"""
        return self._alias

    def whereami(self):
        """Returns the fully qualified path where the current module is stored"""
        return self._whereami

    def pyVersionStr(self):
        """Returns the version of the Python Interpreter running my script"""
        from sys import version_info

        return "Python Interpreter Version: {}.{}.{}".format(version_info.major,
                                                             version_info.minor,
                                                             version_info.micro)

try:
    me = context(__file__)
except:
    from sys import argv
    me = context(argv[0])
    
def _init():
    global USER, COMPUTER, TEMPDIR

    if os.name == 'nt':
        ENVUSERNAME = 'USERNAME'
        ENVTMPDIR = 'TEMP'
    else:   # assume os.name == 'posix'
        ENVUSERNAME = 'LOGNAME'
        ENVTMPDIR = 'TMPDIR'

    if ( ENVUSERNAME in os.environ):
        USER = os.environ[ENVUSERNAME]

    from platform import node
    
    COMPUTER = node()

    if (ENVTMPDIR in os.environ):
        TEMPDIR = os.environ[ENVTMPDIR]

    TEMPDIR = os.path.normcase(TEMPDIR)


class ntpx:
    """implements the NT-style path manipulation support for arguments.
    
    example:
    
        print ntpx('c:/dir/foo.ext').format('dp')  - prints 'c:/dir/'
        print ntpx('c:/dir/foo.ext').format('nx')  - prints 'foo.ext'"""

    def __init__(self,path,normalize=1):
        """object constructor takes a path, and optionally, whether to normalize the path"""
        if normalize:
            self._full = os.path.abspath(os.path.normpath(path))
        else:
            self._full = os.path.abspath(path)

        self._driv,x = os.path.splitdrive(self._full)
        self._path,y = os.path.split(x)
        self._path += os.sep
        self._name,self._ext = os.path.splitext(y)

        if os.path.exists(self._full):
            self._size = os.path.getsize(self._full)
            self._time = os.path.getmtime(self._full)

        else:
            self._size = None
            self._time = None


    def all(self):
        """
        returns a tuple containing all elements of the object
        
        (abs_path, drive_letter, path_only, rootname, extension, filesize, time_in_seconds)
        """

        return (self._full, self._driv, self._path, self._name, self._ext, self._size, self._time)

    def format(self, fmt):
        """
        returns string representing the items specified in the format string

        the format string can contain:
        
            d - drive letter
            p - path
            n - name
            x - extension
            z - file size
            t - file time in seconds
        
        you can string them together, e.g. 'dpnx' returns the fully qualified name.
        
        On platforms like Unix, where drive letter doesn't make sense, it's simply
        ignored when used in a format string, making it easy to construct fully
        qualified path names in an os independent manner.
        """

        val = ''
        for x in fmt:
            if x == 'd':
                val += self._driv

            elif x == 'p':
                val += self._path

            elif x == 'n':
                val += self._name

            elif x == 'x':
                val += self._ext

            elif x == 'z':
                if self._size != None: val += str(self._size)

            elif x == 't':
                if self._time != None: val += str(self._time)

        return val

    def drive(self):
        """returns the drive letter only"""
        return self._driv

    def path(self):
        """returns the path only"""
        return self._path

    def name(self):
        """returns the name only"""
        return self._name

    def ext(self):
        """returns the extension only"""
        return self._ext

    def size(self):
        """returns the size of the file"""
        return self._size

    def datetime(self):
        """returns the time of the file in seconds"""
        return self._time


if (__name__=="__main__"):
    print('PyLib Library Module, not directly callable.')
    from sys import exit
    exit(1)
else:
    _init()
