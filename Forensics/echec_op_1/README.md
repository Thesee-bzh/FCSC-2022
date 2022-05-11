# Forensics / Echec OP 1/3

## Challenge :star:
> L'administrateur de ce serveur a chiffré son disque, le mot de passe est fcsc2022.
> Quelle est la date de la création du système de fichiers en UTC ?
> Le flag est au format ISO 8601, tel que dans l'exemple suivant : FCSC{2022-04-22T06:59:59Z}.

## Input
- A 10GB drive image (not included here)

## Solution
Check the disk with `fdisk`:
```console
$ fdisk -l fcsc.raw
Disk fcsc.raw: 10 GiB, 10737418240 bytes, 20971520 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 60DA4A85-6F6F-4043-8A38-0AB83853E6DC

Device       Start      End  Sectors  Size Type
fcsc.raw1     2048     4095     2048    1M BIOS boot
fcsc.raw2     4096  1861631  1857536  907M Linux filesystem
fcsc.raw3  1861632 20969471 19107840  9.1G Linux filesystem
```

Extract the 9.1G Linux filesystem using `dd`, providing start and number of blocks to extract. Output file is `fcsc.raw3`.
```console
$ dd if=fcsc.raw of=fcsc.raw3 skip=1861632 count=19107840
```

The extracted `fcsc.raw3` is a `LUKS` encrypted file:
```console
$ file fcsc.raw3
fcsc.raw3: LUKS encrypted file, ver 2 [, , sha256] UUID: 45e2f0c4-6640-453d-8b7a-8a60bd61c63d
```

Use the provided password `fcsc2022` to open it (in `/dev/mapper/fcsc3`):
```console
$ sudo cryptsetup luksOpen fcsc.raw3  fcsc3
[sudo] password for kali:
Enter passphrase for fcsc.raw3:
$ ll /dev/mapper/
total 0
crw------- 1 root root 10, 236 May  8 06:25 control
lrwxrwxrwx 1 root root       7 May  8 06:25 fcsc3 -> ../dm-0
lrwxrwxrwx 1 root root       7 May  8 06:25 ubuntu--vg-ubuntu--lv -> ../dm-1
```

Finally mount it in `/mnt`:
```console
$ sudo mount /dev/mapper/ubuntu--vg-ubuntu--lv /mnt
$ cd /mnt/
$ ll
total 1777748
lrwxrwxrwx   1 root root          7 Feb 23 03:49 bin -> usr/bin
drwxr-xr-x   2 root root       4096 Mar 26 23:44 boot
drwxr-xr-x   5 root root       4096 Feb 23 03:54 dev
drwxr-xr-x 100 root root       4096 Mar 27 17:39 etc
drwxr-xr-x   3 root root       4096 Mar 26 23:49 home
lrwxrwxrwx   1 root root          7 Feb 23 03:49 lib -> usr/lib
lrwxrwxrwx   1 root root          9 Feb 23 03:49 lib32 -> usr/lib32
lrwxrwxrwx   1 root root          9 Feb 23 03:49 lib64 -> usr/lib64
lrwxrwxrwx   1 root root         10 Feb 23 03:49 libx32 -> usr/libx32
drwx------   2 root root      16384 Mar 26 23:44 lost+found
drwxr-xr-x   2 root root       4096 Feb 23 03:50 media
drwxr-xr-x   2 root root       4096 Feb 23 03:50 mnt
drwxr-xr-x   2 root root       4096 Feb 23 03:50 opt
drwxr-xr-x   2 root root       4096 Apr 15  2020 proc
drwx------   4 root root       4096 Mar 27 00:14 root
drwxr-xr-x  11 root root       4096 Feb 23 03:57 run
lrwxrwxrwx   1 root root          8 Feb 23 03:49 sbin -> usr/sbin
drwxr-xr-x   6 root root       4096 Feb 23 03:57 snap
drwxr-xr-x   2 root root       4096 Feb 23 03:50 srv
-rw-------   1 root root 1820327936 Mar 26 23:45 swap.img
drwxr-xr-x   2 root root       4096 Apr 15  2020 sys
drwxrwxrwt   9 root root       4096 Mar 27 17:51 tmp
drwxr-xr-x  14 root root       4096 Feb 23 03:53 usr
drwxr-xr-x  14 root root       4096 Mar 27 00:13 var
```

Use `tune2fs` to extract the File System creation time:
```console
$ sudo tune2fs -l /dev/mapper/ubuntu--vg-ubuntu--lv
tune2fs 1.45.6 (20-Mar-2020)
Filesystem volume name:   <none>
Last mounted on:          /mnt
Filesystem UUID:          20e4352b-6b51-4a6c-91ec-a0c76bfdea06
Filesystem magic number:  0xEF53
Filesystem revision #:    1 (dynamic)
Filesystem features:      has_journal ext_attr resize_inode dir_index filetype needs_recovery extent 64bit flex_bg sparse_super large_file huge_file dir_nlink extra_isize metadata_csum
Filesystem flags:         signed_directory_hash
Default mount options:    user_xattr acl
Filesystem state:         clean
Errors behavior:          Continue
Filesystem OS type:       Linux
Inode count:              596848
Block count:              2383872
Reserved block count:     119193
Free blocks:              1244216
Free inodes:              514896
First block:              0
Block size:               4096
Fragment size:            4096
Group descriptor size:    64
Reserved GDT blocks:      1024
Blocks per group:         32768
Fragments per group:      32768
Inodes per group:         8176
Inode blocks per group:   511
Flex block group size:    16
Filesystem created:       Sat Mar 26 23:44:49 2022
Last mount time:          Sun May  8 06:27:50 2022
Last write time:          Sun May  8 06:27:50 2022
Mount count:              10
Maximum mount count:      -1
Last checked:             Sat Mar 26 23:44:49 2022
Check interval:           0 (<none>)
Lifetime writes:          11 GB
Reserved blocks uid:      0 (user root)
Reserved blocks gid:      0 (group root)
First inode:              11
Inode size:               256
Required extra isize:     32
Desired extra isize:      32
Journal inode:            8
Default directory hash:   half_md4
Directory Hash Seed:      997a6484-569a-4ff3-b774-720f4ee5c988
Journal backup:           inode blocks
Checksum type:            crc32c
```

So here is the FS creation time.. but I'm not sure of its format (we want it in UTC time):
```
Filesystem created:       Sat Mar 26 23:44:49 2022
```

Looking around in the File System itself, file `lost+found` has the same time:
```console
drwx------   2 root root      16384 Mar 26 23:44 lost+found
```

Doing 'ls --full-time lost+found' shows a time delay -0400.

So the File creation time I have is -4h00 to UTC, so it should be: 2022-03-27 03:44:49 UTC.

Finally, the correctly formatted time 2022-03-27T03:44:49Z validates the challenge.

## Flag
FCSC{2022-03-27T03:44:49Z}
