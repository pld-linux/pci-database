Summary:	PCI hardware identification data
Summary(pl):	Dane s�u��ce do identyfikacji urz�dze� PCI
Name:		pci-database
Version:	0.11
Release:	1
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	a73a66aaaeae1b7939d3a3ae9c1edfe7
BuildRequires:	awk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pci-database contains various PCI hardware identification data, such
as scsi.pci, net.pci and ide.pci databases for SCSI, network and IDE
devices.

%description -l pl
pci-database zawiera r�ne dane s�u��ce do identyfikacji urz�dze� PCI,
w tym bazy danych scsi.pci, net.pci i ide.pci dla urz�dze� SCSI,
sieciowych i IDE.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%dir %{_datadir}/pci-database
%{_datadir}/pci-database/*
%attr(755,root,root) %{_bindir}/pcidev
