Name:           hello-lib
Version:        1.0
Release:        1%{?dist}
Summary:        A simple library for greetings
License:        MIT
URL:            https://github.com/eljhoset/hello-lib
Source0:        %{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++

%description
A simple library for generating greetings.

%prep
%setup -n %{name}-%{version} -c

%build
%cmake .
%make_build

%install
%cmake_install

%files
/usr/include/hello-lib/
/usr/lib/libgreet_lib.so

%changelog
* Mon Aug 01 2023 Daniel <jd-jd-@hotmail.com> - 1.0-1
- Initial version.