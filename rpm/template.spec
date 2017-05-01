Name:           ros-lunar-stage-ros
Version:        1.8.0
Release:        0%{?dist}
Summary:        ROS stage_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/stage_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-nav-msgs
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-stage
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
Requires:       ros-lunar-tf
BuildRequires:  boost-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-nav-msgs
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-stage
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-std-srvs
BuildRequires:  ros-lunar-tf

%description
This package provides ROS specific hooks for stage

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sun Apr 30 2017 William Woodall <william@osrfoundation.org> - 1.8.0-0
- Autogenerated by Bloom

