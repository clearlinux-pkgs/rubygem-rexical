#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rexical
Version  : 1.0.5
Release  : 5
URL      : https://rubygems.org/downloads/rexical-1.0.5.gem
Source0  : https://rubygems.org/downloads/rexical-1.0.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: rubygem-rexical-bin
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= Rexical
* http://github.com/tenderlove/rexical/tree/master
== DESCRIPTION
Rexical is a lexical scanner generator.
It is written in Ruby itself, and generates Ruby program.
It is designed for use with Racc.

%package bin
Summary: bin components for the rubygem-rexical package.
Group: Binaries

%description bin
bin components for the rubygem-rexical package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rexical-1.0.5
gem spec %{SOURCE0} -l --ruby > rubygem-rexical.gemspec

%build
gem build rubygem-rexical.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rexical-1.0.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/rexical-1.0.5
ruby -v -I.:lib test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/rexical-1.0.5.gem
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Cmd/cdesc-Cmd.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Cmd/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Cmd/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Cmd/usage-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/add_footer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/add_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/add_inner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/add_macro-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/add_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/add_rule-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/cdesc-Generator.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/class_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/debug-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/exclusive_states-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/grammar_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/grammar_lines-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/ignorecase-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/independent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/lineno-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/module_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/next_line-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/parse_action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/parse_rule-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/read_grammar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/rules-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/scanner_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/scanner_io-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/Generator/write_scanner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/ParseError/cdesc-ParseError.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/Rexical/cdesc-Rexical.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/page-CHANGELOG_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/page-DOCUMENTATION_en_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/rexical-1.0.5/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/CHANGELOG.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/DOCUMENTATION.en.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/DOCUMENTATION.ja.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/README.ja
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/bin/rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/lib/rexical.rb
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/lib/rexical/generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/lib/rexical/rexcmd.rb
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/a.cmd
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/b.cmd
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/c.cmd
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/calc3.racc
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/calc3.rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/calc3.rex.rb
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/calc3.tab.rb
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/error1.rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/error2.rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/sample.html
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/sample.rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/sample.rex.rb
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/sample.xhtml
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/sample1.c
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/sample1.rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/sample2.bas
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/sample2.rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/simple.html
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/simple.xhtml
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/xhtmlparser.racc
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/sample/xhtmlparser.rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/test/assets/test.rex
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/test/rex-20060125.rb
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/test/rex-20060511.rb
/usr/lib64/ruby/gems/2.2.0/gems/rexical-1.0.5/test/test_generator.rb
/usr/lib64/ruby/gems/2.2.0/specifications/rexical-1.0.5.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/rex
