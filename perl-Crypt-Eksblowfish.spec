#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-Crypt-Eksblowfish
Version  : 0.009
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Crypt-Eksblowfish-0.009.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Crypt-Eksblowfish-0.009.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libcrypt-eksblowfish-perl/libcrypt-eksblowfish-perl_0.009-2.debian.tar.xz
Summary  : 'the Eksblowfish block cipher'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Crypt-Eksblowfish-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Mix)
BuildRequires : perl(Params::Classify)
BuildRequires : perl-Module-Build
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Crypt::Eksblowfish - the Eksblowfish block cipher
DESCRIPTION
Eksblowfish is a variant of the Blowfish cipher, modified to make the
key setup very expensive.  ("Eks" stands for "expensive key schedule".)
This doesn't make it significantly cryptographically stronger, but is
intended to hinder brute-force attacks.  It also makes it unsuitable for
any application requiring key agility.  It was designed by Niels Provos
and David Mazieres for password hashing in OpenBSD.

%package dev
Summary: dev components for the perl-Crypt-Eksblowfish package.
Group: Development
Provides: perl-Crypt-Eksblowfish-devel = %{version}-%{release}
Requires: perl-Crypt-Eksblowfish = %{version}-%{release}

%description dev
dev components for the perl-Crypt-Eksblowfish package.


%package perl
Summary: perl components for the perl-Crypt-Eksblowfish package.
Group: Default
Requires: perl-Crypt-Eksblowfish = %{version}-%{release}

%description perl
perl components for the perl-Crypt-Eksblowfish package.


%prep
%setup -q -n Crypt-Eksblowfish-0.009
cd %{_builddir}
tar xf %{_sourcedir}/libcrypt-eksblowfish-perl_0.009-2.debian.tar.xz
cd %{_builddir}/Crypt-Eksblowfish-0.009
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Crypt-Eksblowfish-0.009/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::Eksblowfish.3
/usr/share/man/man3/Crypt::Eksblowfish::Bcrypt.3
/usr/share/man/man3/Crypt::Eksblowfish::Blowfish.3
/usr/share/man/man3/Crypt::Eksblowfish::Family.3
/usr/share/man/man3/Crypt::Eksblowfish::Subkeyed.3
/usr/share/man/man3/Crypt::Eksblowfish::Uklblowfish.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
