# Generated from introspection-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gemname introspection

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Dynamic inspection of the hierarchy of method definitions on a Ruby object
Name: rubygem-%{gemname}
Version: 0.0.2
Release: 4%{?dist}
Group: Development/Languages
# https://github.com/floehopper/introspection/issues/1
License: MIT
URL: http://jamesmead.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
# Remove instantiator dependency.
# https://github.com/floehopper/introspection/issues/2
Patch0: %{name}-%{version}-update-dep.patch
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.6
Requires: ruby
Requires: rubygem(metaclass) => 0.0.1
Requires: rubygem(metaclass) < 0.1
# Seems to be useless ATM.
# https://github.com/floehopper/introspection/issues/2
# Requires: rubygem(instantiator) => 0.0.3
# Requires: rubygem(instantiator) < 0.1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) >= 1.3.6
BuildRequires: ruby
BuildRequires: rubygem(metaclass) => 0.0.1
BuildRequires: rubygem(metaclass) < 0.1
# Required to satisty the 'blankslate' require. May be replaced
# by rubygem(blankslate) when available in Fedora.
BuildRequires: rubygem(builder)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Dynamic inspection of the hierarchy of method definitions on a Ruby object


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}

pushd .%{gemdir}
%patch0 -p0
popd

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/

%check
pushd .%{geminstdir}
# Disable Bundler
sed -i '2,2d' test/test_helper.rb
testrb -Ilib test/*_test.rb
popd


%files
%dir %{geminstdir}
%exclude %{geminstdir}/.gitignore
%exclude %{geminstdir}/.travis.yml
%exclude %{geminstdir}/introspection.gemspec
%{geminstdir}/lib
%{geminstdir}/test
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{geminstdir}/README.md
%{geminstdir}/Gemfile
%{geminstdir}/Rakefile
%{geminstdir}/samples
%doc %{gemdir}/doc/%{gemname}-%{version}


%changelog
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 04 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.2-3
- Fix BuildRequires and test suite.
- Move README.md into -doc subpackage and mark it properly.

* Tue Oct 04 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.2-2
- Clarified license.

* Mon Oct 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.2-1
- Initial package
