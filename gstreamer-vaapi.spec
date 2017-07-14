#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0668CC1486C2D7B5 (slomo@debian.org)
#
Name     : gstreamer-vaapi
Version  : 1.12.2
Release  : 8
URL      : https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-1.12.2.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-1.12.2.tar.xz
Source99 : https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-1.12.2.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: gstreamer-vaapi-lib
Requires: gstreamer-vaapi-doc
BuildRequires : docbook-xml
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gst-plugins-bad-dev
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-wayland)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xrender)

%description
gstreamer-vaapi
VA-API support to GStreamer
License
-------
gstreamer-vaapi helper libraries and plugin elements are available
under the terms of the GNU Lesser General Public License v2.1+

%package doc
Summary: doc components for the gstreamer-vaapi package.
Group: Documentation

%description doc
doc components for the gstreamer-vaapi package.


%package lib
Summary: lib components for the gstreamer-vaapi package.
Group: Libraries

%description lib
lib components for the gstreamer-vaapi package.


%prep
%setup -q -n gstreamer-vaapi-1.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500045726
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1500045726
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/api-index-full.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/ch01.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/ch02.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/ch03.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-1.0.devhelp2
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-plugin-vaapi.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapidecodebin.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapih263dec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapih264dec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapih264enc.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapih265dec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapih265enc.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapijpegdec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapijpegenc.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapimpeg2dec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapimpeg2enc.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapimpeg4dec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapipostproc.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapisink.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapivc1dec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapivp8dec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapivp8enc.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapivp9dec.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-plugins-vaapivp9enc.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/gstreamer-vaapi-running.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/home.png
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/index.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/left-insensitive.png
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/left.png
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/object-tree.html
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/right-insensitive.png
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/right.png
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/style.css
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/up-insensitive.png
/usr/share/gtk-doc/html/gstreamer-vaapi-plugins-1.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/gstreamer-1.0/libgstvaapi.so
