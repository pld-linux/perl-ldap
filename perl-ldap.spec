#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working ldap server and gnupg configured with key retrieval with hkp)
#
%include	/usr/lib/rpm/macros.perl
Summary:	perl-ldap module - a client interface to LDAP servers
Summary(pl.UTF-8):	Moduł perl-ldap - kliencki interfejs do serwerów LDAP
Name:		perl-ldap
Version:	0.57
Release:	1
Epoch:		3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{name}-%{version}.tar.gz
# Source0-md5:	deff50f0de5d4cf95145765b6edd67d1
Patch0:		non-unicode-dump.patch
Patch1:		ignore-uninitialized.patch
URL:		http://ldap.perl.org/
BuildRequires:	perl-Authen-SASL >= 2.00
BuildRequires:	perl-Convert-ASN1 >= 0.20
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-IO-Socket-INET6
BuildRequires:	perl-IO-Socket-SSL >= 1.26
BuildRequires:	perl-JSON
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI >= 1.1
BuildRequires:	perl-XML-SAX-Writer
BuildRequires:	perl-devel >= 1:5.18.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Module-Signature
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-libwww
%endif
Obsoletes:	perl-LDAP
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl-ldap is a collection of modules that implements a LDAP services
API for Perl programs.

%description -l pl.UTF-8
perl-ldap to zestaw modułów umożliwiających dostęp do usług LDAP z
poziomu programów w Perlu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/Bundle::Net::LDAP.3pm
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/{Bundle/Net/LDAP.pm,Net/{,LDAP/}*.pod}
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Net/LDAP/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS Changes README TODO
%{perl_vendorlib}/LWP/Protocol/ldap.pm
%{perl_vendorlib}/LWP/Protocol/ldapi.pm
%{perl_vendorlib}/LWP/Protocol/ldaps.pm
%{perl_vendorlib}/Net/LDAP*.pm
%dir %{perl_vendorlib}/Net/LDAP
%{perl_vendorlib}/Net/LDAP/*.pm
%{perl_vendorlib}/Net/LDAP/Control
%{perl_vendorlib}/Net/LDAP/Extension
%{perl_vendorlib}/Net/LDAP/Extra
%{perl_vendorlib}/Net/LDAP/Intermediate
%{_mandir}/man3/LWP::Protocol::ldap*
%{_mandir}/man3/N*
%{_examplesdir}/%{name}-%{version}
