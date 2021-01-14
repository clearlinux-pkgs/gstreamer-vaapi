#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5D2EEE6F6F349D7C (tim@centricular.com)
#
Name     : gstreamer-vaapi
Version  : 1.18.3
Release  : 40
URL      : https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-1.18.3.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-1.18.3.tar.xz
Source1  : https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-1.18.3.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: gstreamer-vaapi-lib = %{version}-%{release}
Requires: gstreamer-vaapi-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gobject-introspection-dev
BuildRequires : gst-plugins-bad-dev
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : libva-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(wayland-protocols)

%description
gstreamer-vaapi
VA-API support to GStreamer
License
-------
gstreamer-vaapi helper libraries and plugin elements are available
under the terms of the GNU Lesser General Public License v2.1+

%package lib
Summary: lib components for the gstreamer-vaapi package.
Group: Libraries
Requires: gstreamer-vaapi-license = %{version}-%{release}

%description lib
lib components for the gstreamer-vaapi package.


%package license
Summary: license components for the gstreamer-vaapi package.
Group: Default

%description license
license components for the gstreamer-vaapi package.


%prep
%setup -q -n gstreamer-vaapi-1.18.3
cd %{_builddir}/gstreamer-vaapi-1.18.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610645527
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk_doc=enabled \
-Dtests=disabled  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gstreamer-vaapi
cp %{_builddir}/gstreamer-vaapi-1.18.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/gstreamer-vaapi/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/gstreamer-1.0/libgstvaapi.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gstreamer-vaapi/01a6b4bf79aca9b556822601186afab86e8c4fbf
