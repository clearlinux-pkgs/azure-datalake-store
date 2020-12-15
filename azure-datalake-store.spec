#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-datalake-store
Version  : 0.0.51
Release  : 12
URL      : https://files.pythonhosted.org/packages/2e/e8/0483d88c6dba818b5a81c410c7bf1bce5817077961f3d408731aa2481fa6/azure-datalake-store-0.0.51.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/e8/0483d88c6dba818b5a81c410c7bf1bce5817077961f3d408731aa2481fa6/azure-datalake-store-0.0.51.tar.gz
Summary  : Azure Data Lake Store Filesystem Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-datalake-store-python = %{version}-%{release}
Requires: azure-datalake-store-python3 = %{version}-%{release}
Requires: adal
Requires: azure-nspkg
Requires: cffi
Requires: pathlib2
Requires: requests
BuildRequires : adal
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : pathlib2
BuildRequires : requests

%description
=============================================================

%package python
Summary: python components for the azure-datalake-store package.
Group: Default
Requires: azure-datalake-store-python3 = %{version}-%{release}

%description python
python components for the azure-datalake-store package.


%package python3
Summary: python3 components for the azure-datalake-store package.
Group: Default
Requires: python3-core
Provides: pypi(azure_datalake_store)
Requires: pypi(adal)
Requires: pypi(cffi)
Requires: pypi(requests)

%description python3
python3 components for the azure-datalake-store package.


%prep
%setup -q -n azure-datalake-store-0.0.51
cd %{_builddir}/azure-datalake-store-0.0.51

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607993046
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3*/site-packages/samples/__init__.py
rm -f %{buildroot}/usr/lib/python3*/site-packages/samples/__pycache__/__init__.cpython-3*.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
