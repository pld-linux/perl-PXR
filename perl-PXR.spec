#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PXR
Summary:	PXR - Perl XML Router Tools for use in other projects
#Summary(pl):	
Name:		perl-PXR
Version:	0.1.5
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/N/NP/NPEREZ/%{pdir}-%{version}.tar.gz
# Source0-md5:	ee51da0051dc83824b69eddab013f1d8
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE-Filter-XML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PXR::Node
    Provides an slick, featureful XML node representation

PXR::Parser
    A simple, speedy, efficient pure perl SAX XML parser

PXR::NS
    Namespace constants for PXR/JABBER(tm)/XMPP development

PXR::Utils
    General purpose common utility functions for PXR Tools

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
