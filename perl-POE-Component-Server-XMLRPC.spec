%define upstream_name    POE-Component-Server-XMLRPC
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl module to publish POE event handlers via XMLRPC over HTTP
License:	Artistic and GPL+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(POE::Component::Server::HTTP)
BuildRequires:  perl(SOAP::Lite) 
BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
POE::Component::Server::XMLRPC is a bolt-on component that can publish a event
handlers via XMLRPC over HTTP.

%prep
%setup -q -n POE-Component-Server-XMLRPC-%{upstream_version}

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
