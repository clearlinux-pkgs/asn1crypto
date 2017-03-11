#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asn1crypto
Version  : 0.21.1
Release  : 1
URL      : https://pypi.python.org/packages/ce/39/17e90c2efacc4060915f7d1f9b8d2a5b20e54e46233bdf3092e68193407d/asn1crypto-0.21.1.tar.gz
Source0  : https://pypi.python.org/packages/ce/39/17e90c2efacc4060915f7d1f9b8d2a5b20e54e46233bdf3092e68193407d/asn1crypto-0.21.1.tar.gz
Summary  : Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP
Group    : Development/Tools
License  : MIT
Requires: asn1crypto-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the asn1crypto package.
Group: Default

%description python
python components for the asn1crypto package.


%prep
%setup -q -n asn1crypto-0.21.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489262474
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489262474
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
