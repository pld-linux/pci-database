Summary:	PCI hardware identification data
Summary(pl):	Dane s³u¿±ce do identyfikacji urz±dzeñ PCI
Name:		pci-database
Version:	0.10
Release:	1
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	7f672ca76350eff3f7b0ac874e19da1a
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
