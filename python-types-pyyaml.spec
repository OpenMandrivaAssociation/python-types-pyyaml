%define module types-pyyaml
%define oname types_pyyaml

Name:		python-types-pyyaml
Version:	6.0.12.20250915
Release:	1
Summary:	Typing stubs for PyYAML
URL:		https://pypi.org/project/types-pyyaml/
License:	None
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/t/types-pyyaml/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Typing stubs for PyYAML

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py3_install

%files
%{python3_sitelib}/yaml-stubs
%{python3_sitelib}/%{oname}-%{version}.dist-info
%license LICENSE
