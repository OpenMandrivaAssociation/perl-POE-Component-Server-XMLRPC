%define realname   POE-Component-Server-XMLRPC

Name:		perl-%{realname}
Version:    0.05
Release:    %mkrel 6
License:	Artistic and GPL
Group:		Development/Perl
Summary:        Perl module to publish POE event handlers via XMLRPC over HTTP
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/POE/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel 
BuildRequires:  perl(POE::Component::Server::HTTP)
BuildRequires:  perl(SOAP::Lite) 
BuildArch: noarch

%description
POE::Component::Server::XMLRPC is a bolt-on component that can publish a event
handlers via XMLRPC over HTTP.

%prep
%setup -q -n POE-Component-Server-XMLRPC-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/POE
%{_mandir}/man3/*

