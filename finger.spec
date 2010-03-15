Summary:	The finger client
Name:		finger
Version:	0.17
Release:	%mkrel 12
License:	BSD
Group:		Networking/Other
URL:		ftp://sunsite.unc.edu/pub/Linux/system/network/finger
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/finger/bsd-finger-%{version}.tar.bz2
Source1:	finger.xinetd
Patch0:		bsd-finger-0.16-pts.patch
Patch1:		bsd-finger-0.10-exact.patch
Patch2:		bsd-finger-0.16-allocbroken.patch
Patch3:		bsd-finger-0.17-rfc742.patch
Patch4:		bsd-finger-0.17-glibc-2.2.2.patch
BuildRoot:	%{_tmppath}/%{name}-root

%description
Finger is a utility which allows users to see information about system users
(login name, home directory, name, how long they've been logged in to the
system, etc.). The finger package includes a standard finger client.

You should install finger if you'd like to retreive finger information from
other systems.

%package	server
Summary:	The finger daemon
Group:		System/Servers
Requires(post): xinetd
Requires(postun): xinetd

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
%patch0 -p1
#%patch2 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
sh configure
perl -pi -e '
    s,^CC=.*$,CC=cc,;
    s,-O2,\$(RPM_OPT_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' MCONFIG
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}}

install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xinetd.d/finger

make INSTALLROOT=%{buildroot} install

%post server
/sbin/service xinetd reload > /dev/null 2>&1 || :

%postun server
/sbin/service xinetd reload > /dev/null 2>&1 || :

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/finger
%{_mandir}/man1/finger.1*

%files server
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/xinetd.d/finger
%{_sbindir}/in.fingerd
%{_mandir}/man8/in.fingerd.8*
%{_mandir}/man8/fingerd.8*


