%define		theme	ubermon

Summary:	superkaramba - Ubermon theme
Summary(pl):	superkaramba - motyw Ubermon
Name:		superkaramba-theme-%{theme}
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/13166-ubermon%{version}.tar
Patch0:		ubermon.theme.patch
# Source0-md5:	f34d707f6493762ddbc24ee6c9136673
URL:		http://www.kde-look.org/content/show.php?content=13166
Requires:	superkaramba
Requires:	coreutils
Requires:	procps
Requires:	net-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ubermon theme for superkaramba. Features:
- User@hostname Output
- Kernel Version Output
- KDE Version Output
- CPU Usage Stats
- CPU Model / Clockspeed / Cache Detection
- RAM / Swapfile Usage
- Hard Disk Drive Monitor (default 4 partitions)
- Network Traffic Monitor
- IP Address Output
- Uptime / Time / Date Output
- XMMS - Currently Playing and Time of Track Information
- XMMS Controls - Skip back, Play, Stop, Pause and Skip Forward

%description -l pl
Motyw ubermon do superkaramby. Wy¶wietlane informacje:
- U¿ytkownik@host
- Wersja j±dra
- Wersja KDE
- Statystyki wykorzystania procesora
- Model procesora / Prêdko¶æ zegara / Pamiêæ cache
- Wykorzystanie pamiêci RAM / pliku wymiany SWAP
- Monitor dysku twardego (domy¶lnie 4 partycje)
- Monitor ruchu sieciowego
- Adres IP
- Uptime / Godzina / Czas
- XMMS - Informacja o utworze i czasie otwarzania
- Przyciski XMMS - Poprzedni, Odtwarzaj, Stop, Pauza i Nastêpny

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon/icons
install ubermon%{version}/icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon/icons
install ubermon%{version}/*.pl $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon
install ubermon%{version}/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%dir %{_datadir}/themes/superkaramba/ubermon
%{_datadir}/themes/superkaramba/ubermon/
