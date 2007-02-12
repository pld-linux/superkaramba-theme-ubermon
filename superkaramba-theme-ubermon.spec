%define		theme	ubermon

Summary:	superkaramba - Ubermon theme
Summary(pl.UTF-8):	superkaramba - motyw Ubermon
Name:		superkaramba-theme-%{theme}
Version:	1.0
Release:	3
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/13166-ubermon%{version}.tar
Patch0:		ubermon.theme.patch
# Source0-md5:	f34d707f6493762ddbc24ee6c9136673
URL:		http://www.kde-look.org/content/show.php?content=13166
BuildRequires:	sed >= 4.0
Requires:	coreutils
Requires:	net-tools
Requires:	procps
Requires:	superkaramba
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

%description -l pl.UTF-8
Motyw ubermon do superkaramby. Wyświetlane informacje:
- Użytkownik@host
- Wersja jądra
- Wersja KDE
- Statystyki wykorzystania procesora
- Model procesora / Prędkość zegara / Pamięć cache
- Wykorzystanie pamięci RAM / pliku wymiany SWAP
- Monitor dysku twardego (domyślnie 4 partycje)
- Monitor ruchu sieciowego
- Adres IP
- Uptime / Godzina / Czas
- XMMS - Informacja o utworze i czasie otwarzania
- Przyciski XMMS - Poprzedni, Odtwarzaj, Stop, Pauza i Następny

%prep
%setup -q -c
%patch0 -p1

# theme modified to white/black font
cd ubermon%{version}
cp ubermon.theme ubermon-white.theme
mv ubermon.theme ubermon-black.theme

%{__sed} -i 's/0,0,0/255,255,255/' ubermon-white.theme
%{__sed} -i 's/1,1,1/254,254,254/' ubermon-white.theme

%install
rm -rf $RPM_BUILD_ROOT

# symbolic link to backward compability
cd ubermon%{version}/
ln -sf ubermon-black.theme ubermon.theme
cd -

install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon/icons
install ubermon%{version}/icons/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon/icons
install ubermon%{version}/*.pl $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon
install ubermon%{version}/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/ubermon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/superkaramba/ubermon
%attr(755,root,root) %{_datadir}/themes/superkaramba/ubermon/ipadd.pl
