Name:          harbour-dyncal-it
Version:       0.1.0
Release:       1
Summary:       DynCal Italy
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires: harbour-dyncal >= 0.3.0-1
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
Change Calendar icon accordingly with the day. It features Italian holidays.

%pre
mkdir /usr/share/harbour-dyncal/backup
cp /usr/share/harbour-dyncal/icons/*.* /usr/share/harbour-dyncal/backup/

%files
%defattr(-,root,root,-)
/usr/share/*

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
cp /usr/share/harbour-dyncal/backup/*.* /usr/share/harbour-dyncal/icons/
rm -rf /usr/share/harbour-dyncal/backup
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
/usr/share/harbour-dyncal/harbour-dyncal.sh
fi
fi

%changelog
* Sat Dec 12 2015 0.1
- First build.
