#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	perl-ldap Perl module
Summary(pl):	Modu³ perla Perl-ldap
Name:		perl-ldap
Version:	0.2701
Release:	3
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{name}-%{version}.tar.gz
# Source0-md5:	fd3cd83810bb3163e47dedd34277da76
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Authen-SASL >= 2.00
BuildRequires:	perl-Convert-ASN1 >= 0.07
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI >= 1.08
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq "perl(Convert::ASN1::Debug)"

%description
perl-ldap is a collection of modules that implements a LDAP services
API for Perl programs.

%description -l pl
perl-ldap jest kolekcj± modu³ów umo¿liwiaj±cych dostêp do us³ug LDAP z
poziomu programów perla.

%prep
%setup -q -n perl-ldap-%{version}
find . -type f | xargs -r perl -pi -e 's|/local/bin/perl\d*|/bin/perl|g'

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -r {contrib,bin} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/LWP/Protocol/ldap.pm
%{perl_vendorlib}/Net/LDAP.pm
%dir %{perl_vendorlib}/Net/LDAP
%{perl_vendorlib}/Net/LDAP/*.pm
%{perl_vendorlib}/Net/LDAP/Control
%{perl_vendorlib}/Net/LDAP/Extension
%{perl_vendorlib}/Net/LDAPS.pm
%{_mandir}/man3/N*
%{_examplesdir}/%{name}-%{version}
