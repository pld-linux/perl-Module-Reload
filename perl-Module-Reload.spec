%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Reload
Summary:	Module::Reload perl module
Summary(pl):	Modu³ perla Module::Reload
Name:		perl-Module-Reload
Version:	1.07
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Reload - reloads INC files when updated on disk.

%description -l pl
Module::Reload - ³aduje ponownie pliki w INC, je¶li zosta³y
zaktualizowane na dysku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Module/Reload.pm
%{_mandir}/man3/*
