#
# Conditional build:
# _without_dist_kernel - without kernel from distribution
#
%define		_base_name	eplip
Summary:	EPLIP (Enhanced Parallel Line IP) module
Summary(pl):	Modu³ EPLIP (Enhanced Parallel Line IP)
Name:		kernel-%{_base_name}
Version:	0.5.6
%define	_rel	5
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://e-plip.sourceforge.net/%{_base_name}-%{version}.tar.gz
# Source0-md5:	43019250e7227857ae13bdd39a45494d
Patch0:		%{name}-Rules.make-fix.patch
Patch1:		%{name}-WIRING.patch
%{!?_without_dist_kernel:BuildRequires:         kernel-headers}
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveOS:	Linux
ExclusiveArch:	%{ix86}

%description
EPLIP (Enhanced Parallel Line IP) module.

%description -l pl
Modu³ EPLIP (Enhanced Parallel Line IP).

%package -n kernel-smp-eplip
Summary:	EPLIP (Enhanced Parallel Line IP) SMP module
Summary(pl):	Modu³ SMP EPLIP (Enhanced Parallel Line IP)
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{!?_without_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-eplip
EPLIP (Enhanced Parallel Line IP) SMP module.

%description -n kernel-smp-eplip -l pl
Modu³ SMP EPLIP (Enhanced Parallel Line IP).

%prep
%setup -q -n %{_base_name}-%{version}
cp Rules.make Rules.make.smp
%patch0 -p1
%patch1 -p1

%build
cp Rules.make Rules.make.up
mv Rules.make.smp Rules.make
%{__make} CONFIG_X86=1 CONFIG_ISA=1
mv eplip.o eplip-smp
mv Rules.make.up Rules.make
%{__make} clean
%{__make} CONFIG_X86=1 CONFIG_ISA=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc
install eplip-smp $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/eplip.o
install eplip.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/depmod -a %{!?_without_dist_kernel:-F /boot/System.map-%{_kernel_ver} }%{_kernel_ver}

%postun
/sbin/depmod -a %{!?_without_dist_kernel:-F /boot/System.map-%{_kernel_ver} }%{_kernel_ver}

%post	-n kernel-smp-eplip
/sbin/depmod -a %{!?_without_dist_kernel:-F /boot/System.map-%{_kernel_ver}smp }%{_kernel_ver}smp

%postun -n kernel-smp-eplip
/sbin/depmod -a %{!?_without_dist_kernel:-F /boot/System.map-%{_kernel_ver}smp }%{_kernel_ver}smp

%files
%defattr(644,root,root,755)
%doc ChangeLog LAME-TESTS README TODO TODO-done WIRING
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-eplip
%defattr(644,root,root,755)
%doc ChangeLog LAME-TESTS README TODO TODO-done WIRING 
/lib/modules/%{_kernel_ver}smp/misc/*
