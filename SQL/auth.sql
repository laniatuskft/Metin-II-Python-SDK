SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `AccountList`;
CREATE TABLE `AccountList`  (
  `pid` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `accId` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '' COMMENT 'LOGIN_MAX_LEN=30',
  `culture` varchar(4) NOT NULL DEFAULT 'tr',
  `hwidNumber` varchar(255) DEFAULT NULL,
  `securityPass` varchar(42) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '' COMMENT 'PASSWD_MAX_LEN=16; default 45 size',
  `deleteCode` varchar(7) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `emailaddress` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `accStatus` varchar(8) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT 'OK',
  `banDate` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `accCreateDate` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `lastPlayDate` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `goldbonus` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `silverbonus` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `storagebonus` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `lootbonus` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `fishexpire` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `marriageexpire` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `moneyexpire` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `husname` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT '',
  `secques1` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `secansw1` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `secques2` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `secansw2` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `point` int(11) NULL DEFAULT 0,
  PRIMARY KEY (`pid`) USING BTREE,
  UNIQUE INDEX `accId`(`accId`) USING BTREE,
  INDEX `deleteCode`(`deleteCode`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for block_exception
-- ----------------------------
DROP TABLE IF EXISTS `block_exception`;
CREATE TABLE `block_exception`  (
  `accId` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT ''
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of block_exception
-- ----------------------------
INSERT INTO `block_exception` VALUES ('NONE');

-- ----------------------------
-- Table structure for gametime
-- ----------------------------
DROP TABLE IF EXISTS `gametime`;
CREATE TABLE `gametime`  (
  `UserID` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `paymenttype` tinyint(2) NOT NULL DEFAULT 1,
  `LimitTime` int(11) UNSIGNED NULL DEFAULT 0,
  `LimitDt` datetime(0) NULL DEFAULT current_timestamp(),
  `Scores` int(11) NULL DEFAULT 0,
  PRIMARY KEY (`UserID`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for gametimeip
-- ----------------------------
DROP TABLE IF EXISTS `gametimeip`;
CREATE TABLE `gametimeip`  (
  `ipid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `ip` varchar(15) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '000.000.000.000',
  `startIP` int(11) NOT NULL DEFAULT 0,
  `endIP` int(11) NOT NULL DEFAULT 255,
  `paymenttype` tinyint(2) NOT NULL DEFAULT 1,
  `LimitTime` int(11) NOT NULL DEFAULT 0,
  `LimitDt` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `readme` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ipid`) USING BTREE,
  UNIQUE INDEX `ip_uniq`(`ip`, `startIP`, `endIP`) USING BTREE,
  INDEX `ip_idx`(`ip`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for gametimelog
-- ----------------------------
DROP TABLE IF EXISTS `gametimelog`;
CREATE TABLE `gametimelog`  (
  `login` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `type` enum('IP_FREE','FREE','IP_TIME','IP_DAY','TIME','DAY') CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `logon_time` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `logout_time` datetime(0) NOT NULL DEFAULT current_timestamp(),
  `use_time` int(11) UNSIGNED NULL DEFAULT NULL,
  `ip` varchar(15) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '000.000.000.000',
  `server` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  INDEX `login_key`(`login`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for iptocountry
-- ----------------------------
DROP TABLE IF EXISTS `iptocountry`;
CREATE TABLE `iptocountry`  (
  `IP_FROM` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `IP_TO` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `COUNTRY_NAME` varchar(56) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of iptocountry
-- ----------------------------
INSERT INTO `iptocountry` VALUES ('0.0.0.0', '0.0.0.0', 'NONE');

-- ----------------------------
-- Table structure for string
-- ----------------------------
DROP TABLE IF EXISTS `string`;
CREATE TABLE `string`  (
  `name` varchar(64) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `text` text CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  PRIMARY KEY (`name`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hwid_allow
-- ----------------------------
DROP TABLE IF EXISTS `hwid_allow`;
CREATE TABLE `hwid_allow` (
  `id` int(11) NOT NULL,
  `aid` int(11) NOT NULL,
  `hwid` int(11) DEFAULT NULL,
  `active` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=38648 DEFAULT CHARSET=ascii;

-- ----------------------------
-- Records of hwid_allow
-- ----------------------------

-- ----------------------------
-- Table structure for hwid_block
-- ----------------------------
DROP TABLE IF EXISTS `hwid_block`;
CREATE TABLE `hwid_block` (
  `id` int(11) NOT NULL,
  `hwid` varchar(64) DEFAULT NULL,
  `bannedUntil` datetime DEFAULT NULL,
  `reason` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=38648 DEFAULT CHARSET=ascii;

SET FOREIGN_KEY_CHECKS = 1;
