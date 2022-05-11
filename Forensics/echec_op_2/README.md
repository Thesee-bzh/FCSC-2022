# Forensics / Echec OP 2/3

## Challenge :star:
> Retrouvez le mot de passe de l'utilisateur principal de ce serveur. La force ne résout pas tout... Le mot de passe correspond au flag, entouré de FCSC{}, par exemple : FCSC{password}. Aussi, l'administrateur de ce serveur a chiffré son disque et le mot de passe est fcsc2022.

## Input
- A 10GB drive image (not included here)

## Solution
This follows challenge `Echec OP 1/3`. Switch to `root` user to inspect ``/mnt/root`:
```console
$ sudo su
root@kali:/mnt# ll
bash: ll: command not found
root@kali:/mnt# cd root
root@kali:/mnt/root# ls -al
total 28
drwx------  4 root root 4096 Mar 27 00:14 .
drwxr-xr-x 19 root root 4096 Mar 26 23:47 ..
-rw-------  1 root root   46 Mar 27 17:39 .bash_history
-rw-r--r--  1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
drwx------  3 root root 4096 Mar 26 23:49 snap
drwx------  2 root root 4096 Mar 26 23:49 .ssh
```

The bash history file is interesting. Sometimes, passwords get logged there accidentally!
```console
root@kali:/mnt/root# cat .bash_history
exit
passwd obob
CZSITvQm2MBT+n1nxgghCJ
exit
```

Bingo, obob's password is logged in here.

## Flag
FCSC{CZSITvQm2MBT+n1nxgghCJ}
