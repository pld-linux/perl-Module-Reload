%include	/usr/lib/rpm/macros.perl
Summary:	Module-Reload perl module
Summary(pl):	Modu³ perla Module-Reload
Name:		perl-Module-Reload
Version:	1.07
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/Module-Reload-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module-Reload - reloads INC files when updated on disk.

%description -l pl
Module-Reload - ³aduje ponownie pliki w INC, je¶li zosta³y
zaktualizowane na dysku.

%prep
%setup -q -n Module-Reload-%{version}

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
