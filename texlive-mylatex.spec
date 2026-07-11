%global tl_name mylatex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Make a format containing a documents preamble
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mylatex
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The file mylatex.ltx permits you to create a format that pre-loads a set
of package files (and/or other macros) that you regularly use. In some
circumstances, this can be a great advantage (though on an ordinarily
fast modern computer on the desktop, gains will be limited). The general
scheme is to initialize your usage by a command of the form: latex -ini
mylatex.ltx <document> whick will create a format file mylatex.fmt,
which you then use as: latex -fmt=mylatex <document>

