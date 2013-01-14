Summary:	The finger client
Name:		finger
Version:	0.17
Release:	19
License:	BSD
Group:		Networking/Other
URL:		ftp://sunsite.unc.edu/pub/Linux/system/network/finger
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/finger/bsd-finger-%{version}.tar.bz2
Source1:	finger.socket
Source2:	finger@.service
# fedora patches
Patch1:		bsd-finger-0.16-pts.patch
Patch2:		bsd-finger-0.17-exact.patch
Patch3:		bsd-finger-0.16-allocbroken.patch
Patch4:		bsd-finger-0.17-rfc742.patch
Patch5:		bsd-finger-0.17-time.patch
Patch6:		bsd-finger-0.17-usagi-ipv6.patch
Patch7:		bsd-finger-0.17-typo.patch
Patch8:		bsd-finger-0.17-strip.patch
Patch9:		bsd-finger-0.17-utmp.patch
Patch10:	bsd-finger-wide-char-support5.patch
Patch11:	bsd-finger-0.17-init-realname.patch
Patch12:	bsd-finger-0.17-host-info.patch
Patch13:	bsd-finger-0.17-match_sigsegv.patch
Patch14:	bsd-finger-0.17-man_page_systemd.patch

# mandriva patches
Patch100:	bsd-finger-0.17-autotoolish.patch

%description
Finger is a utility which allows users to see information about system users
(login name, home directory, name, how long they've been logged in to the
system, etc.). The finger package includes a standard finger client.

You should install finger if you'd like to retreive finger information from
other systems.

%package	server
Summary:	The finger daemon
Group:		System/Servers

%description	server
Finger is a utility which allows users to see information about system users
(login name, home directory, name, how long they've been logged in to the
system, etc.). The finger-server package includes a standard finger server. The
server daemon (fingerd) runs from /etc/inetd.conf, which must be modified to
disable finger requests.

You should install finger-server if your system is used by multiple users and
you'd like finger information to be available.

%prep
%setup -q -n bsd-finger-%{version}
%apply_patches

%build
%serverbuild_hardened

%configure	--enable-ipv6
%make

%install
install -m644 %{SOURCE1} -D %{buildroot}%{_unitdir}/finger.socket
install -m644 %{SOURCE2} -D %{buildroot}%{_unitdir}/finger@.service

%makeinstall_std

%files
%{_bindir}/finger
%{_mandir}/man1/finger.1*

%files server
%{_unitdir}/finger.socket
%{_unitdir}/finger@.service
%{_sbindir}/in.fingerd
%{_mandir}/man8/in.fingerd.8*
%{_mandir}/man8/fingerd.8*

%changelog
* Mon Jan 14 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.17-19
- enable %%serverbuild_hardened

* Sat Jan 12 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.17-18
- enable ipv6 support

* Sat Jan 12 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.17-17
- provide native systemd service file (rhbz#737178)
- make compatible with autotools arguments & variables (P100)
- cleanups
- sync patches with fedora

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.17-14mdv2011.0
+ Revision: 664308
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.17-13mdv2011.0
+ Revision: 605143
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.17-12mdv2010.1
+ Revision: 520108
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.17-11mdv2010.0
+ Revision: 424442
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.17-10mdv2009.0
+ Revision: 220825
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.17-9mdv2008.1
+ Revision: 149726
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.17-8mdv2007.1
+ Revision: 145531
- Import finger

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.17-8mdv2007.1
- use the %%mrel macro
- bunzip patches

* Mon May 15 2006 Stefan van der Eijk <stefan@eijk.nu> 0.17-7mdk
- rebuild for sparc

* Fri Oct 14 2005 Pixel <pixel@mandriva.com> 0.17-6mdk
- rebuild

