%global tl_name logical-markup-utils
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Packages for language-dependent inline quotes and dashes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/logical-markup-utils
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logical-markup-utils.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logical-markup-utils.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains two packages: quoted, for inserting quotation marks;
and onedash, for inserting dashes. Each package takes a language name as
an option; accepted language options are american, british, german and
polish.

