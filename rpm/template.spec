Name:           ros-indigo-moveit-python
Version:        0.2.9
Release:        0%{?dist}
Summary:        ROS moveit_python package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/moveit_python
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp-python
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-shape-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin

%description
A pure-python interaface to the MoveIt! ROS API.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Mar 28 2015 Michael Ferguson <fergs@unboundedrobotics.com> - 0.2.9-0
- Autogenerated by Bloom

* Sat Mar 21 2015 Michael Ferguson <fergs@unboundedrobotics.com> - 0.2.8-0
- Autogenerated by Bloom

* Wed Nov 19 2014 Michael Ferguson <fergs@unboundedrobotics.com> - 0.2.7-0
- Autogenerated by Bloom

* Sun Nov 16 2014 Michael Ferguson <fergs@unboundedrobotics.com> - 0.2.6-0
- Autogenerated by Bloom

