Name:           libksba
Version:        1.3.0
Release:        1
License:        GPL-3.0+
Summary:        KSBA Library
Url:            http://www.gnupg.org/aegypten/
Group:          Development/Libraries/C and C++
Source:         libksba-%{version}.tar.bz2
BuildRequires:  libgpg-error-devel >= 1.8
BuildRequires:  libtool

%description
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data.

%package devel
License:        GPL-2.0+ ; MIT
Summary:        A X
Group:          Development/Libraries/C and C++
Requires:       libgpg-error-devel
Requires:       libksba = %{version}
Provides:       libksba:/usr/include/ksba.h

%description devel
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data.

This package contains the needed files to compile and link against the
libksba.

%prep
%setup -q -n libksba-%{version}

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
%license COPYING
%{_libdir}/libksba*.so.*


%files devel
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/libksba*.so
%{_includedir}/*
%doc %{_infodir}/ksba*
%{_datadir}/aclocal/*

%changelog
