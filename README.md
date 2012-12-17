
			Katalog README
			
1. What is this?
Katalog is set of three sh scripts to manipulate CD catalogs.

2. katadd
It makes list of files at CD and writes it to a file. See: katadd -h.

3. katsch
Katsch is used to search for an regexp in bases. See: katsch -h.
    
4. katls
It shows you a list of currently installed databases. See: katls -h.

5. Settings
Katalog reads settings from files in following succession:
- /etc/katalogrc
- /usr/local/etc/katalogrc
- .katalogrc
- katalogrc
- $HOME/.katalogrc
Arguments used in command line override settings from files.

6. Bases
All bases are stored in /usr/share/katalog by default. Every base has it's
own .dsc file with base description. Format of bases is very simple. In one line
is location of one file on CD-ROM. Content of compressed file is separated with
# (hash). Example:

AfterStep/AfterStep-1.0.tar.gz#AfterStep-1.0/CHANGES

This means, that in archive AfterStep/AfterStep-1.0.tar.gz is file
AfterStep-1.0/CHANGES. It can take a lot of time to create a base with a lot of
compressed files and their contents, so You can turn off this feature. Now only
.tar.gz, .tar.bz2, .zip and .rpm archives are recognized. To save space on disk,
all bases are compressed with gzip or bzip2. In configuration file You can
define program used to compress bases, but only gzip and bzip2 are allowed.

7. CGI frontend
In cgi directory You will find a script called katalog.cgi. Just copy it to
/path/to/your-www-server-root-dir/cgi-bin and open
http://localhost/cgi-bin/katalog.cgi location with Your web browser.
Remember to edit katalog.cgi and set katsch location and directory where bases
are stored. You must also set read and write permissions to bases directory for
user who runs WWW server. Otherwise katsch won't run.

8. Where to find current Katalog version?
Current version with GPG signature You can find here:
http://www.ceti.pl/eaquer/katalog/. My GPG key is at
http://www.ceti.pl/eaquer/pgp.

9. Greetings
KaCzY - he found some bugs, ideas: use of bzip2, automount and reverse (-r),
Grzegorz Go�awski - for new ideas and PLD spec,
Peter Fr�bel - searching in bases descriptions, SPEC for SuSE, eject idea,
Maciej Stachura - some changes in Makefile.

10. Contact
My email address: maciek@korzen.org.

-- 
Sorry for my English. Any grammatical bug reports are welcome. :-)
 vim:tw=80:
