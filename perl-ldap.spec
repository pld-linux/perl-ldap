%include	/usr/lib/rpm/macros.perl
Summary:	perl-ldap perl module
Summary(pl):	Modu³ perla perl-ldap
Name:		perl-ldap
Version:	0.13
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module//%{name}-%{version}.tar.gz
Patch0:		perl-ldap-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Convert-BER
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl-ldap is a collection of modules that implements a LDAP services
API for Perl programs.

%description -l pl
perl-ldap jest kolekcj± modu³ów umo¿liwiaj±cych dostêp do us³ug LDAP z
poziomu programów perla.

%prep
%setup -q -n perl-ldap-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}
cp -r {contrib,bin} $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/perl-ldap
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,TODO}.gz

%{perl_sitelib}/Authen/SASL.pm
%{perl_sitelib}/Authen/SASL
%{perl_sitelib}/LWP/Protocol/ldap.pm
%{perl_sitelib}/Net/LDAP.pm
%{perl_sitelib}/Net/LDAP

%{perl_sitearch}/auto/perl-ldap

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}-%{version}
