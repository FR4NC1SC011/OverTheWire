#!/usr/bin/python3

from pwn import *
import re

log.info("Leviathan 1")
shell = ssh('leviathan1', 'leviathan.labs.overthewire.org', password='rioGegei8m', port=2223)
sh = shell.run('sh')
sh.sendline('(echo sex;cat) | ./check')
sh.sendline('cat /etc/leviathan_pass/leviathan2')
passwd = sh.recvline().decode("utf-8")
log.success(passwd)

#log.warn('run -> cat /etc/leviathan_pass/leviathan2 to grab the flag!')
#sh.interactive()





