cmd_isoimage := ld -z max-page-size=0x1000 -melf_x86_64 -dp  -o isoimage -T link/nautilus.ld  src/built-in.o --start-group  lib/built-in.o `locate libstdc++.a | head -1` --end-group
