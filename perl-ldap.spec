%include	/usr/lib/rpm/macros.perl
Summary:	perl-ldap perl module
Summary(pl):	Modu� perla perl-ldap
Name:		perl-ldap
Version:	0.25
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Net/%{name}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Convert-ASN1 >= 0.07
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI >= 1.08
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq "perl(Convert::ASN1::Debug)"

%description
perl-ldap is a collection of modules that implements a LDAP services
API for Perl programs.

%description -l pl
perl-ldap jest kolekcj� modu��w umo�liwiaj�cych dost�p do us�ug LDAP z
poziomu program�w perla.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_sitelib}/Authen/SASL.pm
%{perl_sitelib}/Authen/SASL
%{perl_sitelib}/LWP/Protocol/ldap.pm
%{perl_sitelib}/Net/LDAP.pm
%{perl_sitelib}/Net/LDAP
%{perl_sitelib}/Net/LDAPS.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
