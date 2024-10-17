Name:		texlive-logical-markup-utils
Version:	15878
Release:	2
Summary:	Packages for language-dependent inline quotes and dashes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/logical-markup-utils
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logical-markup-utils.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logical-markup-utils.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains two packages: - quoted, for inserting
quotation marks; and - onedash, for inserting dashes. Each
package takes a language name as an option; accepted language
options are american, british, german and polish.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
