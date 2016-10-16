Name:           ros-kinetic-moveit-python
Version:        0.2.17
Release:        1%{?dist}
Summary:        ROS moveit_python package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/moveit_python
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp-python
Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-moveit-msgs
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-shape-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin

%description
A pure-python interaface to the MoveIt! ROS API.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Oct 15 2016 Michael Ferguson <fergs@unboundedrobotics.com> - 0.2.17-1
- Autogenerated by Bloom

* Tue Aug 23 2016 Michael Ferguson <fergs@unboundedrobotics.com> - 0.2.17-0
- Autogenerated by Bloom

