%define upstream_name    Module-Manifest
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Parse and examine a Perl distribution MANIFEST file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
*Module::Manifest* is a simple utility module created originally for use in
the Module::Inspector manpage.

It allows you to load the _MANIFEST_ file that comes in a Perl distribution
tarball, examine the contents, and perform some simple tasks.

Granted, the functionality needed to do this is quite simple, but the Perl
distribution _MANIFEST_ specification contains a couple of little
idiosyncracies, such as line comments and space-seperated inline comments.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 658536
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 552414
- update to 1.08

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 403866
- rebuild using %%perl_convert_version

* Sat May 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2010.0
+ Revision: 370492
- update to new version 0.07

* Fri Mar 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.1
+ Revision: 354491
- update to new version 0.06

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 354177
- update to new version 0.05

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 314252
- update to new version 0.04

* Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.03-1mdv2009.0
+ Revision: 277651
- import perl-Module-Manifest


