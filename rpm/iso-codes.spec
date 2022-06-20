Name:       iso-codes
Summary:    ISO code lists and translations
Version:    3.79
Release:    1
Group:      System/Base
License:    LGPLv2+
BuildArch:  noarch
URL:        https://github.com/sailfishos/iso-codes
Source0:    %{name}-%{version}.tar.xz

# for /usr/share/xml
Requires:   xml-common

BuildRequires: gettext >= 0.16
BuildRequires: python3-base

%description
This package provides the ISO 639 Language code list, the ISO 4217
Currency code list, the ISO 3166 Territory code list, and ISO 3166-2
sub-territory lists, and all their translations in gettext format.


%package devel
Summary:    Files for development using %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the pkg-config files for development
when building programs that use %{name}.


%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./bootstrap
%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%find_lang iso-codes --all-name

%files -f iso-codes.lang
%defattr(-,root,root,-)
%doc COPYING
%dir %{_datadir}/xml/iso-codes
%{_datadir}/xml/iso-codes/*.xml
%dir %{_datadir}/iso-codes/json
%{_datadir}/iso-codes/json/*.json

%files devel
%defattr(-,root,root,-)
%doc ChangeLog
%{_datadir}/pkgconfig/iso-codes.pc
