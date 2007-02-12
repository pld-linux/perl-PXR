#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PXR
Summary:	PXR - Perl XML router tools for use in other projects
Summary(pl.UTF-8):   PXR - narzędzia routera XML w Perlu do wykorzystania w innych projektach
Name:		perl-PXR
Version:	0.1.5
Release:	2
# package have GPLv2 attached in Source0
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/N/NP/NPEREZ/%{pdir}-%{version}.tar.gz
# Source0-md5:	ee51da0051dc83824b69eddab013f1d8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE-Filter-XML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl XML Router tools that contains:
- PXR::Node	- provides an slick, featureful XML node representation;
- PXR::Parser	- a simple, speedy, efficient pure Perl SAX XML parser;
- PXR::NS	- namespace constants for PXR/JABBER(tm)/XMPP
		  development;
- PXR::Utils	- general purpose common utility functions for PXR
		  Tools.

%description -l pl.UTF-8
Narzędzia routera XML w Perlu, zawierające:
- PXR::Node	- udostępnia zgrabną, posiadającą duże możliwości
		  reprezentację węzłów XML;
- PXR::Parser	- prosty, szybki, wydajny analizator SAX XML w czystym
		  Perlu;
- PXR::NS	- stałe przestrzeni nazw dla tworzenia programów
		  korzystających z PXR/JABBER(tm)/XMPP;
- PXR::Utils	- funkcje narzędziowe ogólnego stosowania dla PXR Tools.

%prep
%setup -q -n %{pdir}-%{version}

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
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/%{pdir}
%{_mandir}/man3/*
