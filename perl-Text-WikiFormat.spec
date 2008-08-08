#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Text::WikiFormat perl module for translating Wiki formatted text into other formats
Name:		perl-Text-WikiFormat
Version:	0.79
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/Text-WikiFormat-%{version}.tar.gz
# Source0-md5:	7f3e888ff898f67332216c4a25523f30
BuildRequires:  perl-devel >= 1:5.8.0
BuildRequires:  rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::WikiFormat - the original Wiki web site had a very simple
interface to edit and to add pages. Its formatting rules are simple
and easy to use. They are also easy to translate into other, more
complicated markup languages with this module. It creates HTML by
default, but can produce valid POD, DocBook, XML, or any other format
imaginable.

%prep
%setup -q -n Text-WikiFormat-%{version}

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
%doc Changes README
%{perl_vendorlib}/Text/WikiFormat.pm
%{perl_vendorlib}/Text/WikiFormat
%{_mandir}/man3/*
