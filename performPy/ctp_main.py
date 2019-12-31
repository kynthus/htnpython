import ctypes

if __name__ == '__main__':

    libctphello = ctypes.cdll.LoadLibrary('/usr/local/lib/libctphello.so')

    libctphello.hello.argtypes = [ctypes.c_char_p]
    libctphello.hello.restype = ctypes.c_int

    libctphello.hello(b'Hello, World.')
