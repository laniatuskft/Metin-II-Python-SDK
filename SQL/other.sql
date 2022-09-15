SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for exp_table
-- ----------------------------
DROP TABLE IF EXISTS `exp_table`;
CREATE TABLE `exp_table`  (
  `level` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `exp` int(10) UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`level`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 121 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of exp_table
-- ----------------------------
INSERT INTO `exp_table` VALUES (1, 300);
INSERT INTO `exp_table` VALUES (2, 800);
INSERT INTO `exp_table` VALUES (3, 1500);
INSERT INTO `exp_table` VALUES (4, 2500);
INSERT INTO `exp_table` VALUES (5, 4300);
INSERT INTO `exp_table` VALUES (6, 7200);
INSERT INTO `exp_table` VALUES (7, 11000);
INSERT INTO `exp_table` VALUES (8, 17000);
INSERT INTO `exp_table` VALUES (9, 24000);
INSERT INTO `exp_table` VALUES (10, 33000);
INSERT INTO `exp_table` VALUES (11, 43000);
INSERT INTO `exp_table` VALUES (12, 58000);
INSERT INTO `exp_table` VALUES (13, 76000);
INSERT INTO `exp_table` VALUES (14, 100000);
INSERT INTO `exp_table` VALUES (15, 130000);
INSERT INTO `exp_table` VALUES (16, 169000);
INSERT INTO `exp_table` VALUES (17, 219000);
INSERT INTO `exp_table` VALUES (18, 283000);
INSERT INTO `exp_table` VALUES (19, 365000);
INSERT INTO `exp_table` VALUES (20, 472000);
INSERT INTO `exp_table` VALUES (21, 610000);
INSERT INTO `exp_table` VALUES (22, 705000);
INSERT INTO `exp_table` VALUES (23, 813000);
INSERT INTO `exp_table` VALUES (24, 937000);
INSERT INTO `exp_table` VALUES (25, 1077000);
INSERT INTO `exp_table` VALUES (26, 1237000);
INSERT INTO `exp_table` VALUES (27, 1418000);
INSERT INTO `exp_table` VALUES (28, 1624000);
INSERT INTO `exp_table` VALUES (29, 1857000);
INSERT INTO `exp_table` VALUES (30, 2122000);
INSERT INTO `exp_table` VALUES (31, 2421000);
INSERT INTO `exp_table` VALUES (32, 2761000);
INSERT INTO `exp_table` VALUES (33, 3145000);
INSERT INTO `exp_table` VALUES (34, 3580000);
INSERT INTO `exp_table` VALUES (35, 4073000);
INSERT INTO `exp_table` VALUES (36, 4632000);
INSERT INTO `exp_table` VALUES (37, 5194000);
INSERT INTO `exp_table` VALUES (38, 5717000);
INSERT INTO `exp_table` VALUES (39, 6264000);
INSERT INTO `exp_table` VALUES (40, 6837000);
INSERT INTO `exp_table` VALUES (41, 7600000);
INSERT INTO `exp_table` VALUES (42, 8274000);
INSERT INTO `exp_table` VALUES (43, 8990000);
INSERT INTO `exp_table` VALUES (44, 9753000);
INSERT INTO `exp_table` VALUES (45, 10560000);
INSERT INTO `exp_table` VALUES (46, 11410000);
INSERT INTO `exp_table` VALUES (47, 12320000);
INSERT INTO `exp_table` VALUES (48, 13270000);
INSERT INTO `exp_table` VALUES (49, 14280000);
INSERT INTO `exp_table` VALUES (50, 15340000);
INSERT INTO `exp_table` VALUES (51, 16870000);
INSERT INTO `exp_table` VALUES (52, 18960000);
INSERT INTO `exp_table` VALUES (53, 19980000);
INSERT INTO `exp_table` VALUES (54, 21420000);
INSERT INTO `exp_table` VALUES (55, 22930000);
INSERT INTO `exp_table` VALUES (56, 24530000);
INSERT INTO `exp_table` VALUES (57, 26200000);
INSERT INTO `exp_table` VALUES (58, 27960000);
INSERT INTO `exp_table` VALUES (59, 29800000);
INSERT INTO `exp_table` VALUES (60, 32780000);
INSERT INTO `exp_table` VALUES (61, 36060000);
INSERT INTO `exp_table` VALUES (62, 39670000);
INSERT INTO `exp_table` VALUES (63, 43640000);
INSERT INTO `exp_table` VALUES (64, 48000000);
INSERT INTO `exp_table` VALUES (65, 52800000);
INSERT INTO `exp_table` VALUES (66, 58080000);
INSERT INTO `exp_table` VALUES (67, 63890000);
INSERT INTO `exp_table` VALUES (68, 70280000);
INSERT INTO `exp_table` VALUES (69, 77310000);
INSERT INTO `exp_table` VALUES (70, 85040000);
INSERT INTO `exp_table` VALUES (71, 93540000);
INSERT INTO `exp_table` VALUES (72, 102900000);
INSERT INTO `exp_table` VALUES (73, 113200000);
INSERT INTO `exp_table` VALUES (74, 124500000);
INSERT INTO `exp_table` VALUES (75, 137000000);
INSERT INTO `exp_table` VALUES (76, 150700000);
INSERT INTO `exp_table` VALUES (77, 165700000);
INSERT INTO `exp_table` VALUES (78, 236990000);
INSERT INTO `exp_table` VALUES (79, 260650000);
INSERT INTO `exp_table` VALUES (80, 286780000);
INSERT INTO `exp_table` VALUES (81, 315380000);
INSERT INTO `exp_table` VALUES (82, 346970000);
INSERT INTO `exp_table` VALUES (83, 381680000);
INSERT INTO `exp_table` VALUES (84, 419770000);
INSERT INTO `exp_table` VALUES (85, 461760000);
INSERT INTO `exp_table` VALUES (86, 508040000);
INSERT INTO `exp_table` VALUES (87, 558740000);
INSERT INTO `exp_table` VALUES (88, 614640000);
INSERT INTO `exp_table` VALUES (89, 676130000);
INSERT INTO `exp_table` VALUES (90, 743730000);
INSERT INTO `exp_table` VALUES (91, 1041222000);
INSERT INTO `exp_table` VALUES (92, 1145344200);
INSERT INTO `exp_table` VALUES (93, 1259878620);
INSERT INTO `exp_table` VALUES (94, 1385866482);
INSERT INTO `exp_table` VALUES (95, 1524453130);
INSERT INTO `exp_table` VALUES (96, 1676898443);
INSERT INTO `exp_table` VALUES (97, 1844588288);
INSERT INTO `exp_table` VALUES (98, 2029047116);
INSERT INTO `exp_table` VALUES (99, 2050000000);
INSERT INTO `exp_table` VALUES (100, 2150000000);
INSERT INTO `exp_table` VALUES (101, 2210000000);
INSERT INTO `exp_table` VALUES (102, 2250000000);
INSERT INTO `exp_table` VALUES (103, 2280000000);
INSERT INTO `exp_table` VALUES (104, 2310000000);
INSERT INTO `exp_table` VALUES (105, 2330000000);
INSERT INTO `exp_table` VALUES (106, 2350000000);
INSERT INTO `exp_table` VALUES (107, 2370000000);
INSERT INTO `exp_table` VALUES (108, 2390000000);
INSERT INTO `exp_table` VALUES (109, 2400000000);
INSERT INTO `exp_table` VALUES (110, 2410000000);
INSERT INTO `exp_table` VALUES (111, 2420000000);
INSERT INTO `exp_table` VALUES (112, 2430000000);
INSERT INTO `exp_table` VALUES (113, 2440000000);
INSERT INTO `exp_table` VALUES (114, 2450000000);
INSERT INTO `exp_table` VALUES (115, 2460000000);
INSERT INTO `exp_table` VALUES (116, 2470000000);
INSERT INTO `exp_table` VALUES (117, 2480000000);
INSERT INTO `exp_table` VALUES (118, 2490000000);
INSERT INTO `exp_table` VALUES (119, 2490000000);
INSERT INTO `exp_table` VALUES (120, 2500000000);

-- ----------------------------
-- Table structure for gmconfig
-- ----------------------------
DROP TABLE IF EXISTS `gmconfig`;
CREATE TABLE `gmconfig`  (
  `authority` enum('DEVELOPER','IMPLEMENTOR','GOD','HIGH_WIZARD','WIZARD','LOW_WIZARD','PLAYER') CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'PLAYER',
  `can_drop_player_item` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_drop_gm_item` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_exchange_player_item_to_gm` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_exchange_player_item_to_player` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_exchange_gm_item_to_gm` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_exchange_gm_item_to_player` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_exchange_to_gm` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_exchange_to_player` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_buy_private_item` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_create_private_shop` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_use_safebox` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_create_player` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  `can_delete_player` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`authority`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of gmconfig
-- ----------------------------
INSERT INTO `gmconfig` VALUES ('DEVELOPER', 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

-- ----------------------------
-- Table structure for gmlist
-- ----------------------------
DROP TABLE IF EXISTS `gmlist`;
CREATE TABLE `gmlist`  (
  `mID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `mAccount` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `mName` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `mContactIP` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `mServerIP` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'ALL',
  `mAuthority` enum('DEVELOPER','IMPLEMENTOR','HIGH_WIZARD','GOD','LOW_WIZARD','PLAYER') CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'PLAYER',
  PRIMARY KEY (`mID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for locale
-- ----------------------------
DROP TABLE IF EXISTS `locale`;
CREATE TABLE `locale`  (
  `mKey` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `mValue` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`mKey`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of locale
-- ----------------------------
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE0', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE1', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE2', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE3', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE4', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE5', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE6', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL_TYPE7', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');
INSERT INTO `locale` VALUES ('LOCALE', 'hungary');
INSERT INTO `locale` VALUES ('DB_NAME_COLUMN', 'locale_name');
INSERT INTO `locale` VALUES ('SKILL_DAMAGE_BY_LEVEL_UNDER_90', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0');
INSERT INTO `locale` VALUES ('SKILL_DAMAGE_BY_LEVEL_UNDER_45', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0');
INSERT INTO `locale` VALUES ('SKILL_POWER_BY_LEVEL', '0 5 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 50 52 54 56 58 60 63 66 69 72 82 85 88 91 94 98 102 106 110 115 125 125 125 125 125');

-- ----------------------------
-- Table structure for priv_settings
-- ----------------------------
DROP TABLE IF EXISTS `priv_settings`;
CREATE TABLE `priv_settings`  (
  `priv_type` enum('PLAYER','GUILD','EMPIRE') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'EMPIRE' COMMENT 'GUILD and PLAYER are untested.',
  `id` int(10) UNSIGNED NOT NULL DEFAULT 0 COMMENT 'this is for empire_id, player_id or guild_id',
  `type` int(10) UNSIGNED NOT NULL DEFAULT 4 COMMENT '1:item_drop, 2:gold_drop, 3:gold10_drop, 4:exp (1~4)',
  `value` int(11) NOT NULL DEFAULT 0 COMMENT '0~1000%',
  `duration` datetime(0) NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`priv_type`, `id`, `type`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of priv_settings
-- ----------------------------
INSERT INTO `priv_settings` VALUES ('EMPIRE', 0, 1, 200, '2023-01-01 00:00:00');
INSERT INTO `priv_settings` VALUES ('EMPIRE', 0, 2, 200, '2023-01-01 00:00:00');
INSERT INTO `priv_settings` VALUES ('EMPIRE', 0, 3, 200, '2023-01-01 00:00:00');
INSERT INTO `priv_settings` VALUES ('EMPIRE', 0, 4, 200, '2023-01-01 00:00:00');

-- ----------------------------
-- Table structure for spam_db
-- ----------------------------
DROP TABLE IF EXISTS `spam_db`;
CREATE TABLE `spam_db`  (
  `word` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `score` int(3) NOT NULL DEFAULT 1,
  `type` enum('SPAM','MAPS') CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'SPAM',
  PRIMARY KEY (`word`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
