%define version  0.9.0
%define release  %mkrel 6
%define src_name honoka-plugin-romkan

%define honoka_version   0.9.0

Name:       scim-honoka-plugin-romkan
Summary:    A Romaji-Hiraga input plugin for honoka
Version:    %{version}
Release:    %{release}
Group:      System/Internationalization
License:    GPL
URL:        http://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bhonoka%5D%5D
Source0:    http://nop.net-p.org/files/honoka/%{src_name}-%{version}.tar.bz2
Patch0:     honoka-plugin-romkan_change_default_romaji_tables.diff
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: scim-honoka-devel >= %{honoka_version}
BuildRequires: automake
BuildRequires: libltdl-devel

%description
A Romaji-Hiraga input plugin for honoka.

%prep
%setup -q -n %{src_name}-%{version}
%patch0 -p0

%build
autoreconf
[[ -f configure ]] || ./bootstrap

%configure2_5x
# (tv) parallel build is broken:
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove devel files
rm -f $RPM_BUILD_ROOT/%{scim_plugins_dir}/honoka/*.{a,la}

%find_lang honoka-plugin-romkan

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -f honoka-plugin-romkan.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README.jp
%{_datadir}/scim/honoka/*.rkt
%{scim_plugins_dir}/honoka/*.so
