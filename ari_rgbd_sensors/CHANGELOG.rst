^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_rgbd_sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.13 (2020-06-02)
-------------------
* Merge branch 'no-rgbd-laser' into 'ferrum-devel'
  removing rgbd laser scan
  See merge request robots/ari_navigation!14
* removing rgbd laser scan
* Contributors: Federico Nardi, procopiostein

0.0.12 (2020-05-26)
-------------------
* Merge branch 'frame-skip' into 'ferrum-devel'
  setting pointcloud_frame_skip parameter
  See merge request robots/ari_navigation!13
* Merge branch 'small-map' into 'ferrum-devel'
  added small-textured-office map
  See merge request robots/ari_navigation!12
* added new map for simulated environment + updated image topics
* setting pointcloud_frame_skip parameter
* Contributors: Federico Nardi, procopiostein

0.0.11 (2020-05-20)
-------------------
* Merge branch 'fixed-depth-proc' into 'ferrum-devel'
  added launch file for registering rgb and depth
  See merge request robots/ari_navigation!11
* added launch file for registering rgb and depth
* Merge branch 'depth-image-proc' into 'ferrum-devel'
  Depth image proc
  See merge request robots/ari_navigation!10
* Remove unecessary parts in depth_proc launch
* Update to create depth registered image topic
* Depth image processing launch file to produce /depth_registered/points topic
* Contributors: Sara Cooper, federiconardi, procopiostein

0.0.10 (2020-03-17)
-------------------
* better ls2pc config
* Contributors: Procópio Stein

0.0.9 (2020-03-13)
------------------
* Fix relay topic name
* Use relay instead of republish for raspi images, saves a lot of CPU
* Merge branch 'add-elp-launch' into 'ferrum-devel'
  added elp launch and dep for front camera
  See merge request robots/ari_navigation!7
* Parametrize elp_front.launch
* Update elp_front.launch
* Removed comments, set as arguments remaining parameters
* Add argument to set device
* Add device id to launch file
* missing format param
* added simple launch for elp
* added elp launch and dep for front camera
* Contributors: Procópio Stein, Victor Lopez, procopiostein, saracooper

0.0.8 (2020-02-11)
------------------
* removed virtual tf for laser from camera
* fixed input cloud name
* updated default args for launches
* Modified and created the structure for navigation for ARI adding the localization move_base state_machine
* added files for PC2LS
* Contributors: Procópio Stein, alessandrodifava

0.0.7 (2020-01-09)
------------------
* Add missing dependencies
* Contributors: Victor Lopez

0.0.6 (2020-01-09)
------------------
* Add head_front_camera launch
* Contributors: Victor Lopez

0.0.5 (2020-01-07)
------------------
* Merge branch 'ari_calib_odom_in_file' into 'erbium-devel'
  Ari calib odom in file
  See merge request robots/ari_navigation!3
* New odom in calib file with axis angle representation and the right axis chosen
* Configured the file for the odom in
* Contributors: Victor Lopez, alessandrodifava

0.0.4 (2019-12-17)
------------------
* Merge branch 'ari_back_camera_tf_fixing' into 'erbium-devel'
  Adding the static transformation for tf and removing the odom_tf publish to fix the tf structure
  See merge request robots/ari_navigation!1
* Adding the static transformation for tf and removing the odom_tf publish to fix the tf structure
* Contributors: Victor Lopez, alessandrodifava

0.0.3 (2019-11-08)
------------------
* Update front camera launch
* Initial commit
* Contributors: Victor Lopez
