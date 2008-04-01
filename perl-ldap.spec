#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working ldap server and gnupg configured with key retrieval with hkp)
#
%include	/usr/lib/rpm/macros.perl
Summary:	perl-ldap module - a client interface to LDAP servers
Summary(pl.UTF-8):	Moduł perl-ldap - kliencki interfejs do serwerów LDAP
Name:		perl-ldap
Version:	0.34
Release:	1
Epoch:		3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{name}-%{version}.tar.gz
# Source0-md5:	398689b0a7b1615075a6b5035f6e3e91
URL:		http://ldap.perl.org/
BuildRequires:	perl-Authen-SASL >= 2.00
BuildRequires:	perl-Convert-ASN1 >= 0.07
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-IO-Socket-SSL >= 0.81
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Module-Signature
BuildRequires:	perl-URI >= 1.08
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-libwww
%endif
Obsoletes:	perl-LDAP
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq 'perl(Convert::ASN1::Debug)'

%description
perl-ldap is a collection of modules that implements a LDAP services
API for Perl programs.

%description -l pl.UTF-8
perl-ldap to zestaw modułów umożliwiających dostęp do usług LDAP z
poziomu programów w Perlu.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

# this must be done after tests because of signature checking
find blib -type f | xargs -r perl -pi -e 's|/local/bin/perl\d*|/bin/perl|g'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT
cp -r {contrib,bin} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Net/LDAP/.packlist
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/Bundle::Net::LDAP.3pm
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/{Bundle/Net/LDAP.pm,Net/{,LDAP/}*.pod}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS Changes README TODO
%{perl_vendorlib}/LWP/Protocol/ldap.pm
%{perl_vendorlib}/Net/LDAP*.pm
%dir %{perl_vendorlib}/Net/LDAP
%{perl_vendorlib}/Net/LDAP/*.pm
%{perl_vendorlib}/Net/LDAP/Control
%{perl_vendorlib}/Net/LDAP/Extension
%{_mandir}/man3/N*
%{_examplesdir}/%{name}-%{version}
