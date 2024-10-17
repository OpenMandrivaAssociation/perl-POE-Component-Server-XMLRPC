%define upstream_name    POE-Component-Server-XMLRPC
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module to publish POE event handlers via XMLRPC over HTTP
License:	Artistic and GPL+
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(POE::Component::Server::HTTP)
BuildRequires:	perl(SOAP::Lite) 
BuildArch:	noarch

%description
POE::Component::Server::XMLRPC is a bolt-on component that can publish a event
handlers via XMLRPC over HTTP.

%prep
%setup -q -n POE-Component-Server-XMLRPC-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/POE
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 406182
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-7mdv2009.0
+ Revision: 258273
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.05-6mdv2009.0
+ Revision: 246330
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.05-4mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.05-4mdv2008.0
+ Revision: 25146
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-3mdk
- Fix According to perl Policy
	- BuildRequires
	- URL
	- Source URL

* Wed Mar 29 2006 Michael Scherer <misc@mandriva.org> 0.05-2mdk
- fix BuildRequires

* Fri Jan 27 2006 Michael Scherer <misc@mandriva.org> 0.05-1mdk
- First Mandriva package

