Name:		ee4j-parent
Version:	1.0.1
Release:	2%{?dist}
Summary:	Parent POM file for Eclipse Enterprise for Java projects

License:	EPL-2.0 or GPLv2 with exceptions
URL:		https://github.com/eclipse-ee4j/ee4j

Source0:	https://github.com/eclipse-ee4j/ee4j/archive/1.0.1.tar.gz

BuildArch:	noarch
ExclusiveArch: x86_64

BuildRequires:	maven-local

%description
Eclipse Enterprise for Java (EE4J) is an open source initiative to create 
standard APIs, implementations of those APIs, and technology compatibility kits
for Java run-times that enable development, deployment, and management of 
server-side and cloud-native applications.

%global tarball_name ee4j-%{version}

%prep
%setup -q -n %{tarball_name}

mv %{_builddir}/%{tarball_name}/parent/pom.xml %{_builddir}/%{tarball_name}/pom.xml
rm -r %{_builddir}/%{tarball_name}/parent/

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Thu Mar 04 2021 Alex Macdonald <almacdon@redhat.com> - 1.0.1-1
- Add ExclusiveArch: x86_64

* Fri Sep 21 2018 Salman Siddiqui <sasiddiq@redhat.com> - 1.0.1-1
- Initial packaging
