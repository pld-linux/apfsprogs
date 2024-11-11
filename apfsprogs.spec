Summary:	Userland programs to work with the APFS (Apple File System)
Summary(pl.UTF-8):	Programy przestrzeni użytkownika do pracy z APFS (Apple File System)
Name:		apfsprogs
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/linux-apfs/apfsprogs/tags
Source0:	https://github.com/linux-apfs/apfsprogs/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b33d9efe2494536addc7ec49a63c5660
Patch0:		%{name}-verbose.patch
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
%setup -q
%patch0 -p1

%build
%{__make} -C apfs-label \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make} -C apfs-snap \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make} -C apfsck \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make} -C mkapfs \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C apfs-label install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

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
%attr(755,root,root) %{_bindir}/apfs-label
%attr(755,root,root) %{_bindir}/apfs-snap
%attr(755,root,root) %{_bindir}/apfsck
%attr(755,root,root) %{_bindir}/fsck.apfs
%attr(755,root,root) %{_bindir}/mkapfs
%attr(755,root,root) %{_bindir}/mkfs.apfs
%{_mandir}/man8/apfs-label.8*
%{_mandir}/man8/apfs-snap.8*
%{_mandir}/man8/apfsck.8*
%{_mandir}/man8/fsck.apfs.8*
%{_mandir}/man8/mkapfs.8*
%{_mandir}/man8/mkfs.apfs.8*
