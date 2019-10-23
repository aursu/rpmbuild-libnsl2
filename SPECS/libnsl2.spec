Name:       libnsl2
Version:    1.1.0
Release:    2%{?dist}
Summary:    Public client interface library for NIS(YP) and NIS+

License:    BSD and LGPLv2+
Group:      System Environment/Libraries
URL:        https://github.com/thkukuk/libnsl


Source0:    https://github.com/thkukuk/libnsl/archive/libnsl-%{version}.tar.gz#/libnsl-libnsl-%{version}.tar.gz

Patch0: libnsl2-1.0.5-include_stdint.patch

BuildRequires: autoconf, automake, gettext-devel, libtool, libtirpc-devel

%description
This package contains the libnsl library. This library contains
the public client interface for NIS(YP) and NIS+.
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.

%package devel
Summary: Development files for libnsl
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libnsl2


%prep
%setup -q -n libnsl-libnsl-%{version}

%patch0 -p1 -b .include_stdint

%build

export CFLAGS="%{optflags}"

autoreconf -fiv

%configure\
    --libdir=%{_libdir}/nsl\
    --includedir=%{_includedir}/nsl\

%make_build


%install

%make_install

rm %{buildroot}/%{_libdir}/nsl/libnsl.a
rm %{buildroot}/%{_libdir}/nsl/libnsl.la
mv %{buildroot}/%{_libdir}/nsl/pkgconfig %{buildroot}/%{_libdir}

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/nsl" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%dir %{_libdir}/nsl
%{_libdir}/nsl/libnsl.so.2
%{_libdir}/nsl/libnsl.so.2.0.0
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/*

%license COPYING


%files devel
%{_libdir}/nsl/libnsl.so
%{_includedir}/nsl/
%{_libdir}/pkgconfig/libnsl.pc

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Matej Mužila <mmuzila@redhat.com> 1.1.0-1
- Update to version 1.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Matej Mužila <mmuzila@redhat.com> 1.0.5-1
- Update to version 1.0.5
- Fix missing stdint.h

* Mon Apr 10 2017 Matej Mužila <mmuzila@redhat.com> 1.0.4-4
- Initial version for 1.0.4

