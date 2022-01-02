windres -J rc -O coff -i cmdbkg.rc -o cmdbkg.res
gcc -o cmdbkg.exe cmdbkg.c cmdbkg.res -Os -s -lgdi32 -ldwmapi -lgdiplus
