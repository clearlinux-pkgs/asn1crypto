#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asn1crypto
Version  : 1.4.0
Release  : 45
URL      : https://files.pythonhosted.org/packages/6b/b4/42f0e52ac2184a8abb31f0a6f98111ceee1aac0b473cee063882436e0e09/asn1crypto-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6b/b4/42f0e52ac2184a8abb31f0a6f98111ceee1aac0b473cee063882436e0e09/asn1crypto-1.4.0.tar.gz
Summary  : Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP
Group    : Development/Tools
License  : MIT
Requires: asn1crypto-license = %{version}-%{release}
Requires: asn1crypto-python = %{version}-%{release}
Requires: asn1crypto-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
A fast, pure Python library for parsing and serializing ASN.1 structures.
        
         - [Features](#features)
         - [Why Another Python ASN.1 Library?](#why-another-python-asn1-library)
         - [Related Crypto Libraries](#related-crypto-libraries)
         - [Current Release](#current-release)
         - [Dependencies](#dependencies)
         - [Installation](#installation)
         - [License](#license)
         - [Documentation](#documentation)
         - [Continuous Integration](#continuous-integration)
         - [Testing](#testing)
         - [Development](#development)
         - [CI Tasks](#ci-tasks)

%package license
Summary: license components for the asn1crypto package.
Group: Default

%description license
license components for the asn1crypto package.


%package python
Summary: python components for the asn1crypto package.
Group: Default
Requires: asn1crypto-python3 = %{version}-%{release}

%description python
python components for the asn1crypto package.


%package python3
Summary: python3 components for the asn1crypto package.
Group: Default
Requires: python3-core
Provides: pypi(asn1crypto)

%description python3
python3 components for the asn1crypto package.


%prep
%setup -q -n asn1crypto-1.4.0
cd %{_builddir}/asn1crypto-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595959229
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/asn1crypto
cp %{_builddir}/asn1crypto-1.4.0/LICENSE %{buildroot}/usr/share/package-licenses/asn1crypto/6755b3daebb93d8e3568dac92e1f275ac289ffda
cp %{_builddir}/asn1crypto-1.4.0/asn1crypto.egg-info/LICENSE %{buildroot}/usr/share/package-licenses/asn1crypto/6755b3daebb93d8e3568dac92e1f275ac289ffda
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/asn1crypto/6755b3daebb93d8e3568dac92e1f275ac289ffda

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
