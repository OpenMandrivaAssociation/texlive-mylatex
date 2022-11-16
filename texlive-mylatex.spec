Name:		texlive-mylatex
Version:	56751
Release:	1
Summary:	Make a format containing a document's preamble
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mylatex
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file mylatex.ltx permits you to create a format that
pre-loads a set of package files (and/or other macros) that you
regularly use. In some circumstances, this can be a great
advantage (though on an ordinarily fast modern computer on the
desktop, gains will be limited). The general scheme is to
initialise your usage by a command of the form: latex -ini
mylatex.ltx <document> whick will create a format file
mylatex.fmt, which you then use as: latex -fmt=mylatex
<document>

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mylatex
%doc %{_texmfdistdir}/doc/latex/mylatex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
