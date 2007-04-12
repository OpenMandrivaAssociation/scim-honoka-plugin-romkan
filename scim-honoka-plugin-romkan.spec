%define version  0.9.0
%define release  %mkrel 1
%define src_name honoka-plugin-romkan

%define honoka_version   0.9.0

Name:       scim-honoka-plugin-romkan
Summary:    A Romaji-Hiraga input plugin for honoka
Version:    %{version}
Release:    %{release}
Group:      System/Internationalization
License:    GPL
URL:        http://sourceforge.jp/projects/scim-imengine/
Source0:    %{src_name}-%{version}.tar.bz2
Patch0:     honoka-plugin-romkan_change_default_romaji_tables.diff
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: scim-honoka-devel >= %{honoka_version}
BuildRequires: automake1.8
BuildRequires: libltdl-devel

%description
A Romaji-Hiraga input plugin for honoka.


%prep
%setup -q -n %{src_name}-%{version}
%patch0 -p0
cp /usr/share/automake-1.9/mkinstalldirs .

%build
[[ -f configure ]] || ./bootstrap

%configure2_5x
# (tv) parallel build is broken:
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove devel files
rm -f $RPM_BUILD_ROOT/%{_libdir}/scim-1.0/honoka/*.{a,la}

%find_lang honoka-plugin-romkan

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f honoka-plugin-romkan.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README.jp
%{_datadir}/scim/honoka/*.rkt
%{_libdir}/scim-1.0/honoka/*.so


