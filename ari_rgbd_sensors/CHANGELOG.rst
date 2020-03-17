^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_rgbd_sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
