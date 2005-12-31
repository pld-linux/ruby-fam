%define	tarname			fam-ruby
Summary:	FAM module for Ruby
Summary(pl):	Modu³ FAM dla Ruby
Name:		ruby-Fam
Version:	0.1.4
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	http://www.pablotron.org/download/%{tarname}-%{version}.tar.gz
# Source0-md5:	2f05d10545139ca1aedba18ee3cbc012
Source1:	http://www.pablotron.org/software/fam-ruby/examples/dirmon.rb
# Source1-md5:	83ff885769efdb729df6899cd8d40c8c
URL:		http://www.pablotron.org/software/fam-ruby/
BuildRequires:	fam-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAM module for Ruby.

%description -l pl
Modu³ FAM dla Ruby.

%prep
%setup -q -n %{tarname}-%{version}

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

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
install %{SOURCE1}  $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_archdir}/*
%{ruby_ridir}/*
%{_examplesdir}/%{name}-%{version}
