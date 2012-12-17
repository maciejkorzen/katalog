prefix=/usr/local
sysconfdir=${prefix}/etc
bindir=${prefix}/bin
DESTDIR=

all:
	@echo "Type 'make install' to install katalog in system."
	@echo "Type 'make uninstall' to remove katalog from system."

install:
	if [ "`id -u`" = "0" ]; then \
	  rights="-o 0 -g 0" ;\
	else \
	  rights="" ;\
	fi ;\
	install -d $(DESTDIR)${bindir}    $(DESTDIR)${sysconfdir} ;\
	install -m 644 $$rights katalogrc $(DESTDIR)${sysconfdir} ;\
	install -m 755 $$rights katsch    $(DESTDIR)${bindir} ;\
	install -m 755 $$rights katls     $(DESTDIR)${bindir} ;\
	install -m 755 $$rights katadd    $(DESTDIR)${bindir}

uninstall:
	rm $(DESTDIR)${sysconfdir}/katalogrc
	rm $(DESTDIR)${bindir}/katsch
	rm $(DESTDIR)${bindir}/katls
	rm $(DESTDIR)${bindir}/katadd
