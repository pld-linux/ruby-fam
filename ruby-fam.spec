%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define	tarname			fam-ruby
Summary:	FAM module for Ruby
Summary(pl):	Modu³ FAM dla Ruby
Name:		ruby-Fam
Version:	0.1.3
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.pablotron.org/download/%{tarname}-%{version}.tar.gz
# Source0-md5:	a3ca0f91ac1f694f34121d6b21022aad
Source1:	http://www.pablotron.org/software/fam-ruby/examples/dirmon.rb
# Source1-md5:	83ff885769efdb729df6899cd8d40c8c
URL:		http://www.pablotron.org/software/fam-ruby/
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	fam-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAM module for Ruby.

%description -l pl
Modu³ FAM dla Ruby.

%prep
%setup -q -n %{tarname}-%{version}

%build
ruby extconf.rb 
%{__make}
rdoc --ri -o ri
rdoc -o rdoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}
install -d $RPM_BUILD_ROOT%{ruby_ridir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}
install %{SOURCE1}  $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_archdir}/*
%{_examplesdir}/*
%{ruby_ridir}/*
