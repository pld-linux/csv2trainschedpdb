Summary:	Converts CSV into a PDB - for PDA.
Summary(pl):	Konwersja CSV do PDB - dla PDA.
Name:		csv2trainschedpdb
Version:	0.3
Release:	1
License:	GPL
Group:		Utilities
Source0:	http://dl.sourceforge.net/trainsched/%{name}-src-%{version}.tar.gz
# Source0-md5:	d9c82554158a019f3cb39de6d417a2f7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool for converting CSV train/bus databases into PDB readable by trainsched
at your PalmOS.

%description -l pl
Narz�dzie konwertuj�ce plany poci�g�w/autobus�w w CSV do PDB kt�re mog�
zosta� odczytane przez trainsched'a na twoim PalmOS.

%prep
%setup -q -n %{name}-src-%{version}

%build
%{__make} CC="gcc %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README breteche.csv
%attr(755,root,root) %{_bindir}/%{name}
