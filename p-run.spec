%define name p-run
%define version 0.1
%define release %mkrel 4

Summary: Runs program, script or commands on large number of hosts in parallel
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0:	p-run-Makefile.patch
License: GPL
Group: Networking/Remote access
Url: http://www.sorensonfamily.com/~frank/projects/p-run/

BuildRequires: expect-devel

%description
p-run is a utility that runs a program, script, or series of commands on
a large number of hosts in parallel. It simplifies management of machines
in computer labs. It uses ssh, and supports password and key-based 
authentication. p-run uses libexpect, and will run in parallel across as 
many processes as specified. When run on a large number of hosts, its 
parallel nature significantly speeds up administration.

%files
%defattr(-,root,root)
%doc Copying README TODO
%attr(755,root,root) %{_bindir}/*

#--------------------------------------------------------------------

%prep
%setup -q
%patch -p0

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
cp -v %name %{buildroot}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

