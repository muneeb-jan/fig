// TODO: malloc wrapper
// TODO: write wrapper

#define _GNU_SOURCE
#include <dlfcn.h>
#include <unistd.h>
#include <assert.h>
#include <errno.h>


typedef void* (*malloc_type) (size_t size);
void *malloc(size_t size){
    static malloc_type orig = 0;
    //if (drand48 () < 0.1) {
        errno = ENOMEM;
        return -1;
    //}
    /*if (0 == orig) {
        orig = (malloc_type)dlsym (RTLD_NEXT, "malloc");
        assert (orig && "original malloc function not found");
    }
    return orig (size);*/
}
