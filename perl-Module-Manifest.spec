%define realname   Module-Manifest
%define version    0.03
%define release    %mkrel 1

Name:          perl-%{realname}
Version:       %{version}
Release:       %{release}
License:       GPL or Artistic
Group:         Development/Perl
Summary:       Parse and examine a Perl distribution MANIFEST file
Source:        http://www.cpan.org/modules/by-module/Module/%{realname}-%{version}.tar.gz
Url:           http://search.cpan.org/dist/%{realname}
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
*Module::Manifest* is a simple utility module created originally for use in
the Module::Inspector manpage.

It allows you to load the _MANIFEST_ file that comes in a Perl distribution
tarball, examine the contents, and perform some simple tasks.

Granted, the functionality needed to do this is quite simple, but the Perl
distribution _MANIFEST_ specification contains a couple of little
idiosyncracies, such as line comments and space-seperated inline comments.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*
