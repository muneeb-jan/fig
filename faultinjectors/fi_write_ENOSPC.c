// TODO: write wrapper

#define _GNU_SOURCE
#include <dlfcn.h>
#include <unistd.h>
#include <assert.h>
#include <errno.h>

typedef ssize_t (*write_type) (int fd, const void *buf, size_t count);
ssize_t write (int fd, const void *buf, size_t count) {
    static write_type orig = 0;
    //if (drand48 () < 0.1) {
        errno = ENOSPC;
        return -1;
    //}
    /*if (0 == orig) {
        orig = (write_type)dlsym (RTLD_NEXT, "write");
        assert (orig && "original write function not found");
    }
    return orig (fd, buf, count);*/
}
