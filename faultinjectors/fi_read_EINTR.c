// TODO: read wrapper
#define _GNU_SOURCE
#include <dlfcn.h>
#include <unistd.h>
#include <assert.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
typedef ssize_t (*read_type) (int, void *, size_t);
ssize_t read (int fd, void *buf, size_t count) {
    static read_type orig = 0;
    srand48(50);
    if (drand48() < 0.1) {
        errno = EINTR;
        return -1;
    }
    if (0 == orig) {
        orig = (read_type)dlsym (RTLD_NEXT, "read");
        assert (orig && "original read function not found");
    }
    return orig (fd, buf, count);
}
 