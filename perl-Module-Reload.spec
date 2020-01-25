#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Module
%define		pnam	Reload
Summary:	Module::Reload perl module
Summary(pl.UTF-8):	Moduł perla Module::Reload
Name:		perl-Module-Reload
Version:	1.07
Release:	11
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	17fa42608052a79bf2f0c24221bd8c31
URL:		http://search.cpan.org/dist/Module-Reload/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Reload - reloads INC files when updated on disk.

%description -l pl.UTF-8
Module::Reload - ładuje ponownie pliki w INC, jeśli zostały
zaktualizowane na dysku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Module/Reload.pm
%{_mandir}/man3/*
