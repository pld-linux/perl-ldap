%define		_noautoreq "perl(Convert::ASN1::Debug)"
%include	/usr/lib/rpm/macros.perl
Summary:	perl-ldap perl module
Summary(pl):	Modu³ perla perl-ldap
Name:		perl-ldap
Version:	0.25
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{name}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Convert-BER
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-libwww
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -r {contrib,bin} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Authen/SASL.pm
%{perl_sitelib}/Authen/SASL
%{perl_sitelib}/LWP/Protocol/ldap.pm
%{perl_sitelib}/Net/LDAP.pm
%{perl_sitelib}/Net/LDAP
%{perl_sitelib}/Net/LDAPS.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
