# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/logical-markup-utils
# catalog-date 2009-11-09 23:05:00 +0100
# catalog-license gpl3
# catalog-version undef
Name:		texlive-logical-markup-utils
Version:	20091109
Release:	3
Summary:	Packages for language-dependent inline quotes and dashes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/logical-markup-utils
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logical-markup-utils.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logical-markup-utils.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091109-2
+ Revision: 753412
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091109-1
+ Revision: 718878
- texlive-logical-markup-utils
- texlive-logical-markup-utils
- texlive-logical-markup-utils
- texlive-logical-markup-utils

