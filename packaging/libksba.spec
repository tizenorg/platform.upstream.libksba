Name:           libksba
Version:        1.2.0
Release:        1
License:        GPL-3.0+
Summary:        A X
Url:            http://www.gnupg.org/aegypten/
Group:          Development/Libraries/C and C++
# change also name and nfb
%define nld_build 0
Source:         libksba-%{version}.tar.bz2
Patch1:         nld-build.diff
BuildRequires:  libgpg-error-devel >= 1.8
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data.

%package devel
License:        GPL-2.0+ ; MIT
Summary:        A X
Group:          Development/Libraries/C and C++
%if %nld_build
Conflicts:      libksba-devel
%else
Requires:       libgpg-error-devel
Requires:       libksba = %{version}
Provides:       libksba:/usr/include/ksba.h
%endif

%description devel
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data.

This package contains the needed files to compile and link against the
libksba.

%prep
%setup -q -n libksba-%{version}
%if %nld_build
%patch1
%endif

%build
autoreconf -fi
%configure --disable-static --with-pic
make %{?_smp_mflags}

%check
make check

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libksba*.so.*

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/ksba.info.gz

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ksba.info.gz

%files devel
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/libksba*.so
%{_includedir}/*
%doc %{_infodir}/ksba*
%{_datadir}/aclocal/*

%changelog
