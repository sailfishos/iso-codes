# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       iso-codes

# >> macros
# << macros

Summary:    ISO code lists and translations
Version:    3.38
Release:    1
Group:      System/Base
License:    LGPLv2+
BuildArch:  noarch
URL:        http://alioth.debian.org/projects/pkg-isocodes/
Source0:    http://pkg-isocodes.alioth.debian.org/downloads/iso-codes-%{version}.tar.xz
Source100:  iso-codes.yaml
Requires:   xml-common
BuildRequires:  gettext >= 0.16

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
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%find_lang iso-codes --all-name

%files -f iso-codes.lang
%defattr(-,root,root,-)
# >> files
%doc ChangeLog README LICENSE
%dir %{_datadir}/xml/iso-codes
%{_datadir}/xml/iso-codes/*.xml
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_datadir}/pkgconfig/iso-codes.pc
# << files devel
