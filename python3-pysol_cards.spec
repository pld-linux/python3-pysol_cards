%define		module		pysol_cards
Summary:	Deal PySol FC Cards
# Name must match the python module/package name (as on pypi or in 'import' statement)
Name:		python3-%{module}
Version:	0.14.2
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pysol-cards/
Source0:	https://files.pythonhosted.org/packages/source/p/pysol-cards/%{module}-%{version}.tar.gz
# Source0-md5:	294d856b219f0aeaa70e1c32a917487b
URL:		https://pypi.org/project/pysol-cards/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pysol-cards python modules allow the python developer to generate
the initial deals of some PySol FC games. It also supports PySol
legacy deals and Microsoft FreeCell / Freecell Pro deals.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
