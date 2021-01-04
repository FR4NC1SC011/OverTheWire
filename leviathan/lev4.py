#!/usr/bin/python3

from pwn import *

log.info('Leviathan 4')
shell = ssh('leviathan3', 'leviathan.labs.overthewire.org', password='Ahdiemoo1j', port=2223)
sh = shell.run('sh')
sh.sendline('(echo snlprintf;cat) | ./level3')
log.warn('run -> cat /etc/leviathan_pass/leviathan4 to grab the flag!')
sh.interactive()

