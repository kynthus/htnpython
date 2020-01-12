import cffi

if __name__ == "__main__":
    ffi = cffi.FFI()
    ffi.cdef(csource='''extern int hello(const char *);''')

    lib = ffi.dlopen('libcffihello.so')
    lib.hello(b'Hello, World.')
