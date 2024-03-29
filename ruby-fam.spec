%define	pkgname	fam
Summary:	FAM module for Ruby
Summary(pl.UTF-8):	Moduł FAM dla Ruby
Name:		ruby-%{pkgname}
Version:	0.1.4
Release:	4
License:	GPL
Group:		Development/Languages
Source0:	http://www.pablotron.org/download/%{pkgname}-ruby-%{version}.tar.gz
# Source0-md5:	2f05d10545139ca1aedba18ee3cbc012
Source1:	http://www.pablotron.org/software/fam-ruby/examples/dirmon.rb
# Source1-md5:	83ff885769efdb729df6899cd8d40c8c
URL:		http://www.pablotron.org/software/fam-ruby/
BuildRequires:	fam-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8.4-5
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-Fam
Provides:	ruby-Fam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAM module for Ruby.

%description -l pl.UTF-8
Moduł FAM dla Ruby.

%prep
%setup -q -n %{pkgname}-ruby-%{version}

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

rdoc --ri -o ri
rdoc -o rdoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}
install -d $RPM_BUILD_ROOT%{ruby_ridir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
install %{SOURCE1}  $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_archdir}/*
%{ruby_ridir}/*
%{_examplesdir}/%{name}-%{version}
