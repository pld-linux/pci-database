Summary:	PCI hardware identification data
Name:		pci-database
Version:	0.0.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	9b2702763bb5c8557d3adba7737f1960
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pci-database contains various PCI hardware identification data, such
as scsi, net and ide databases.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%dir %{_datadir}/pci-database
%{_datadir}/pci-database/*
