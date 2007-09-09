Summary:        Java program checker
Name:           jlint
Version:        3.0
Release:        %mkrel 5
Epoch:          0
Group:          Development/Java
License:        GPL
URL:            http://jlint.sourceforge.net/
Source0:        http://osdn.dl.sourceforge.net/jlint/jlint-3.0.tar.bz2
Patch0:         %{name}-build.patch
BuildRequires:  tetex-latex
BuildRequires:  texi2html
BuildRequires:	zlib-devel
BuildRequires:  texinfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Jlint will check your Java code and find bugs, inconsistencies and
synchronization problems by doing data flow analysis and building
lock graph.

%prep
%setup -q
%patch0 -p1
%{__rm} -f manual.pdf

%build
%make CFLAGS="-c -DNDEBUG %{optflags}"
%{__make} doc

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%makeinstall INSTALL_DIR="%{buildroot}%{_bindir}"
%{__mv} -f %{buildroot}%{_bindir}/%{name}.sh %{buildroot}%{_bindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc BUGS README TODO manual.pdf
%attr(0755,root,root) %{_bindir}/antic
%attr(0755,root,root) %{_bindir}/%{name}
