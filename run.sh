#!/bin/sh

<your-fault-injection-tool> read_EIO
<your-fault-injection-tool> read_EINTR
<your-fault-injection-tool> write_ENOSPC
<your-fault-injection-tool> write_EIO
<your-fault-injection-tool> select_ENOMEM
<your-fault-injection-tool> malloc_ENOMEM
