Name:		texlive-logical-markup-utils
Version:	20091109
Release:	1
Summary:	Packages for language-dependent inline quotes and dashes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logical-markup-utils
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logical-markup-utils.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logical-markup-utils.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle contains two packages: - quoted, for inserting
quotation marks; and - onedash, for inserting dashes. Each
package takes a language name as an option; accepted language
options are american, british, german and polish.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/logical-markup-utils/onedash.sty
%{_texmfdistdir}/tex/latex/logical-markup-utils/quoted.sty
%doc %{_texmfdistdir}/doc/latex/logical-markup-utils/COPYING
%doc %{_texmfdistdir}/doc/latex/logical-markup-utils/README
%doc %{_texmfdistdir}/doc/latex/logical-markup-utils/TODO

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
