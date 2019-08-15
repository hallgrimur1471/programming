# fd

The `read` function is from `unistd.h`, see `man 2 read`.

We make it read from file descriptor 0 which is standard input and to standard input we write "LETMEWIN\n"

```
./pwn_fd.py
```
