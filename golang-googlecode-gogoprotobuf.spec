%global debug_package   %{nil}
%global import_path     code.google.com/p/gogoprotobuf
%global gopath          %{_datadir}/gocode
%global commit          d228c1a206c3a756d7ec6cc3579d92d00c35a161
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-googlecode-gogoprotobuf
Version:        0
Release:        0.7.git%{shortcommit}%{?dist}
Summary:        A fork of goprotobuf with several extra features
License:        BSD
URL:            http://code.google.com/p/gogoprotobuf
# VCS:          https://code.google.com/p/gogoprotobuf/
# I produced this tarball with "git archive"
Source0:        %{name}-%{commit}.tar.gz
BuildRequires:  golang
Requires:       protobuf

%description
%{summary}

%package devel
Requires:       golang
Requires:       %{name}
Summary:        A fork of goprotobuf with several extra features
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -n %{name}-%{commit}

%build
unset GOPATH
export GOPATH=$(pwd)
mkdir -p src/code.google.com/p/
ln -s $(pwd) src/code.google.com/p/gogoprotobuf 
cd protoc-gen-gogo
go build

%install
install -d %{buildroot}%{_bindir}
install -m 755 protoc-gen-gogo/protoc-gen-gogo %{buildroot}/%{_bindir}/protoc-gen-gogo
install -d %{buildroot}/%{gopath}/src/%{import_path}
rm -rf proto/testdata protoc-gen-gogo/{protoc-gen-gogo,testdata}
for d in proto protoc-gen-gogo; do
   cp -av $d %{buildroot}/%{gopath}/src/%{import_path}
   find %{buildroot}/%{gopath}/ -name Makefile -delete
done

%files 
%doc CONTRIBUTORS LICENSE README
%{_bindir}/protoc-gen-gogo

%files devel
%doc CONTRIBUTORS LICENSE README
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/code.google.com
%dir %attr(755,root,root) %{gopath}/src/code.google.com/p
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/proto
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/protoc-gen-gogo
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/protoc-gen-gogo/descriptor
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/protoc-gen-gogo/generator
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/protoc-gen-gogo/plugin
%{gopath}/src/%{import_path}/proto/*.go
%{gopath}/src/%{import_path}/protoc-gen-gogo/*.go
%{gopath}/src/%{import_path}/protoc-gen-gogo/descriptor/*.pb.go*
%{gopath}/src/%{import_path}/protoc-gen-gogo/descriptor/*.go*
%{gopath}/src/%{import_path}/protoc-gen-gogo/generator/*.go
%{gopath}/src/%{import_path}/protoc-gen-gogo/plugin/*.go*

%changelog
* Thu Jul 17 2014 Colin Walters <walters@verbum.org>
- Initial package
