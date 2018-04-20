# Script generated with Bloom
pkgdesc="ROS - A pure-python interaface to the MoveIt! ROS API."
url='http://ros.org/wiki/moveit_python'

pkgname='ros-kinetic-moveit-python'
pkgver='0.2.17_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('python2-pyassimp'
'ros-kinetic-actionlib'
'ros-kinetic-geometry-msgs'
'ros-kinetic-moveit-msgs'
'ros-kinetic-rospy'
'ros-kinetic-shape-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=moveit_python
source=()
md5sums=()

prepare() {
    cp -R $startdir/moveit_python $srcdir/moveit_python
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

