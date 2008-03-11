%bcond_with     doc

Name:           jlint
Version:        3.1
Release:        %mkrel 0.0.1
Epoch:          0
Summary:        Java program checker
Group:          Development/Java
License:        GPL
URL:            http://jlint.sourceforge.net/
Source0:        http://osdn.dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         jlint-3.1-64bit.patch
%if %with doc
BuildRequires:  tetex-latex
BuildRequires:  texi2html
BuildRequires:  texinfo
%endif
BuildRequires:	zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Jlint will check your Java code and find bugs, inconsistencies and
synchronization problems by doing data flow analysis and building
lock graph.

%prep
%setup -q
%patch0 -p1
%if %with doc
%{__rm} -f manual.pdf
%endif

%build
%{make} CFLAGS="-c -DNDEBUG %{optflags}"
%if %with doc
%{__make} doc
%endif

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{makeinstall} INSTALL_DIR="%{buildroot}%{_bindir}"
%{__mv} %{buildroot}%{_bindir}/%{name}.sh %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc BUGS README TODO manual.pdf
%attr(0755,root,root) %{_bindir}/antic
%attr(0755,root,root) %{_bindir}/%{name}
