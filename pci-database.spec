Summary:	PCI hardware identification data
Summary(pl):	Dane s³u¿±ce do identyfikacji urz±dzeñ PCI
Name:		pci-database
Version:	0.13
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://rescuecd.pld-linux.org/pci-database/%{name}-%{version}.tar.bz2
# Source0-md5:	e225deb89d9c1649f277afef0c8a7de0
BuildRequires:	awk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pci-database contains various PCI hardware identification data, such
as scsi.pci, net.pci and ide.pci databases for SCSI, network and IDE
devices.

%description -l pl
pci-database zawiera ró¿ne dane s³u¿±ce do identyfikacji urz±dzeñ PCI,
w tym bazy danych scsi.pci, net.pci i ide.pci dla urz±dzeñ SCSI,
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
