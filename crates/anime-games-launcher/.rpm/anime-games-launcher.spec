%define __spec_install_post %{nil}
%define __os_install_post %{_dbpath}/brp-compress
%define debug_package %{nil}

Name: anime-games-launcher
Summary: Universal games launcher powered by luau scripts with in-house APIs 
Version: 2.0.0
Release: 1%{?dist}
License: GPLv3+
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/an-anime-team/anime-games-launcher

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%build
rm -rf %{buildroot}
mkdir -p %{buildroot}
cargo build --release

%install
mkdir -p %{buildroot}/usr/bin
cp target/anime-games-launcher %{buildroot}/usr/bin
chmod +x %{buildroot}/usr/bin/anime-games-launcher

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
