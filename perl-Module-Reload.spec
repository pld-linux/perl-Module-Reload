%include	/usr/lib/rpm/macros.perl
Summary:	Module-Reload perl module
Summary(pl):	Modu³ perla Module-Reload
Name:		perl-Module-Reload
Version:	1.07
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/Module-Reload-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module-Reload - reloads INC files when updated on disk. 

%description -l pl
Module-Reload - ³aduje ponownie pliki w INC, je¶li zosta³y zaktualizowane
na dysku.

%prep
%setup -q -n Module-Reload-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Module/Reload
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Module/Reload.pm
%{perl_sitearch}/auto/Module/Reload

%{_mandir}/man3/*
