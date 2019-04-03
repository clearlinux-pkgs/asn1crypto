#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asn1crypto
Version  : 0.24.0
Release  : 27
URL      : http://pypi.debian.net/asn1crypto/asn1crypto-0.24.0.tar.gz
Source0  : http://pypi.debian.net/asn1crypto/asn1crypto-0.24.0.tar.gz
Summary  : Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP
Group    : Development/Tools
License  : MIT
Requires: asn1crypto-license = %{version}-%{release}
Requires: asn1crypto-python = %{version}-%{release}
Requires: asn1crypto-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python-core
BuildRequires : setuptools-legacypython

%description
# asn1crypto
A fast, pure Python library for parsing and serializing ASN.1 structures.

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

%description python3
python3 components for the asn1crypto package.


%prep
%setup -q -n asn1crypto-0.24.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554305420
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/asn1crypto
cp LICENSE %{buildroot}/usr/share/package-licenses/asn1crypto/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/asn1crypto/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
