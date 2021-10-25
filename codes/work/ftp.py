from ftplib import FTP

#If no user is specified, it defaults to 'anonymous'. If user is 'anonymous', the default passwd is 'anonymous@'.

ftp = FTP("10.4.4.5")
ftp.login()
