Summary:	Userland programs to work with the APFS (Apple File System)
Summary(pl.UTF-8):	Programy przestrzeni użytkownika do pracy z APFS (Apple File System)
Name:		apfsprogs
Version:	0
%define	gitref	e6591615e4ceff37a43575b1255ab64954a10a28
%define	snap	20230310
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/linux-apfs/apfsprogs/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	6c55f283f41ac4bbd341f7985d4f1bf9
URL:		https://github.com/linux-apfs/apfsprogs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apfsprogs is a suite of userland software to work with the APFS (Apple
File System) on Linux. For now only mkfs and fsck tools are available,
both functional but lacking in features. Compatibility with the Apple
implementations has barely been tested; please exercise caution, and
report any issues that you find.

%description -l pl.UTF-8
Apfsprogs to zbiór programów przestrzeni użytkownika do pracy z
systemem plików APFS (Apple File System) pod Linuksem. Obecnie
dostępne są tylko mkfs i fsck - działające, ale z brakującymi
funkcjami. Zgodność z implementacjami Apple była słabo testowana -
należy próbować ostrożnie i zgłaszać napotkane problemy.

%prep
%setup -q -n %{name}-%{gitref}

%build
%{__make} -C apfs-snap \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make} -C apfsck \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make} -C mkapfs \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C apfs-snap install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

%{__make} -C apfsck install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

%{__make} -C mkapfs install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/apfs-snap
%attr(755,root,root) %{_bindir}/apfsck
%attr(755,root,root) %{_bindir}/fsck.apfs
%attr(755,root,root) %{_bindir}/mkapfs
%attr(755,root,root) %{_bindir}/mkfs.apfs
%{_mandir}/man8/apfs-snap.8*
%{_mandir}/man8/apfsck.8*
%{_mandir}/man8/fsck.apfs.8*
%{_mandir}/man8/mkapfs.8*
%{_mandir}/man8/mkfs.apfs.8*
