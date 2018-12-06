%global goipath         gopkg.in/src-d/go-billy.v4
%global forgeurl        https://github.com/src-d/go-billy
Version:                4.1.1

%global common_description %{expand:
The missing interface filesystem abstraction for Go. Billy implements an
interface based on the os standard library, allowing development of applications
without the dependency on the underlying storage. Makes for a virtually free
implementation of mocks and testing over filesystem operations.}

%gometa

Name:    golang-gopkg-src-d-billy
Release: 2%{?dist}
Summary: The missing interface filesystem abstraction for Go
License: ASL 2.0
URL:     %{gourl}
Source:  %{gosource}
BuildRequires: golang(gopkg.in/check.v1)

%description
%{common_description}

%package -n %{goname}-devel
Summary:    %{summary}
BuildArch:  noarch

%description -n %{goname}-devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files -n %{goname}-devel -f devel.file-list
%license LICENSE
%doc DCO MAINTAINERS README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 05 2018 Dominik Mierzejewski <dominik@greysector.net> - 4.1.1-1
- update to 4.1.1

* Tue Apr 03 2018 Dominik Mierzejewski <dominik@greysector.net> - 4.1.0-1
- First package for Fedora
