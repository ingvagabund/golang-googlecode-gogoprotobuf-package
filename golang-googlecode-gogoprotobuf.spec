%global debug_package   %{nil}
%global import_path     code.google.com/p/gogoprotobuf
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
ExclusiveArch:  %{go_arches} noarch
Requires:       protobuf

%description
%{summary}

%package devel
BuildArch:      noarch
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Requires:       %{name}
Summary:        A fork of goprotobuf with several extra features
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/fieldpath) = %{version}-%{release}
Provides:       golang(%{import_path}/parser) = %{version}-%{release}
Provides:       golang(%{import_path}/io) = %{version}-%{release}
Provides:       golang(%{import_path}/proto) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo/descriptor) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo/generator) = %{version}-%{release}
Provides:       golang(%{import_path}/protoc-gen-gogo/plugin) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/defaultcheck) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/description) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/embedcheck) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/enumstringer) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/equal) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/face) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/gostring) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/marshalto) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/populate) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/size) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/stringer) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/testgen) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/union) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/unmarshal) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/unsafemarshaler) = %{version}-%{release}
Provides:       golang(%{import_path}/plugin/unsafeunmarshaler) = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -q -n %{name}-%{commit}

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
rm -rf proto/testdata protoc-gen-gogo/{protoc-gen-gogo,testdata} fieldpath/fieldpath-gen
mkdir -p %{buildroot}/%{gopath}/src/%{import_path}
for d in fieldpath io parser plugin proto protoc-gen-gogo; do
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
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/fieldpath
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/parser
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/defaultcheck
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/description
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/embedcheck
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/enumstringer
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/equal
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/face
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/gostring
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/marshalto
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/populate
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/size
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/stringer
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/testgen
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/union
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/unmarshal
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/unsafemarshaler
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/plugin/unsafeunmarshaler
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/io
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/proto
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/protoc-gen-gogo
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/protoc-gen-gogo/descriptor
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/protoc-gen-gogo/generator
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/protoc-gen-gogo/plugin
%{gopath}/src/%{import_path}/fieldpath/*.go
%{gopath}/src/%{import_path}/io/*.go
%{gopath}/src/%{import_path}/parser/*.go
%{gopath}/src/%{import_path}/plugin/defaultcheck/*.go
%{gopath}/src/%{import_path}/plugin/description/*.go
%{gopath}/src/%{import_path}/plugin/embedcheck/*.go
%{gopath}/src/%{import_path}/plugin/enumstringer/*.go
%{gopath}/src/%{import_path}/plugin/equal/*.go
%{gopath}/src/%{import_path}/plugin/face/*.go
%{gopath}/src/%{import_path}/plugin/gostring/*.go
%{gopath}/src/%{import_path}/plugin/marshalto/*.go
%{gopath}/src/%{import_path}/plugin/populate/*.go
%{gopath}/src/%{import_path}/plugin/size/*.go
%{gopath}/src/%{import_path}/plugin/stringer/*.go
%{gopath}/src/%{import_path}/plugin/testgen/*.go
%{gopath}/src/%{import_path}/plugin/union/*.go
%{gopath}/src/%{import_path}/plugin/unmarshal/*.go
%{gopath}/src/%{import_path}/plugin/unsafemarshaler/*.go
%{gopath}/src/%{import_path}/plugin/unsafeunmarshaler/*.go
%{gopath}/src/%{import_path}/proto/*.go
%{gopath}/src/%{import_path}/protoc-gen-gogo/*.go
%{gopath}/src/%{import_path}/protoc-gen-gogo/descriptor/*.pb.go*
%{gopath}/src/%{import_path}/protoc-gen-gogo/descriptor/*.go*
%{gopath}/src/%{import_path}/protoc-gen-gogo/generator/*.go
%{gopath}/src/%{import_path}/protoc-gen-gogo/plugin/*.go*

%changelog
* Thu Jul 17 2014 Colin Walters <walters@verbum.org> - 0-0.7.gitd228c1a
- Initial package
