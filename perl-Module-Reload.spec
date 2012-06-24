%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Reload
Summary:	Module::Reload perl module
Summary(pl):	Modu� perla Module::Reload
Name:		perl-Module-Reload
Version:	1.07
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Reload - reloads INC files when updated on disk.

%description -l pl
Module::Reload - �aduje ponownie pliki w INC, je�li zosta�y
zaktualizowane na dysku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Module/Reload.pm
%{_mandir}/man3/*
