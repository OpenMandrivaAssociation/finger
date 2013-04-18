Summary:	The finger client
Name:		finger
Version:	0.17
Release:	19
License:	BSD
Group:		Networking/Other
Url:		http://www.ibiblio.org/pub/Linux/system/network/finger/
Source0:	http://www.ibiblio.org/pub/Linux/system/network/finger/bsd-finger-%{version}.tar.gz
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
%setup -qn bsd-finger-%{version}
%apply_patches

%build
%serverbuild_hardened

%configure2_5x \
	--enable-ipv6
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

