import argparse
import logging
import os
import unittest

import betterdiscordpy
from util import exceptions


class MainFunctionsTest(unittest.TestCase):
    def testVerbosityLevelGetter(self) -> None:
        self.assertRaises(
            exceptions.InvalidVerbosityConfigurationException, betterdiscordpy.getVerbosityLevel,
            argparse.Namespace(quiet=True, verbose=True),
        )
        self.assertEqual(
            logging.WARNING,
            betterdiscordpy.getVerbosityLevel(argparse.Namespace(quiet=True, verbose=False)),
        )
        self.assertEqual(
            logging.DEBUG,
            betterdiscordpy.getVerbosityLevel(argparse.Namespace(quiet=False, verbose=True)),
        )
        self.assertEqual(
            logging.INFO,
            betterdiscordpy.getVerbosityLevel(argparse.Namespace(quiet=False, verbose=False)),
        )

    def testConfigDirGetter(self) -> None:
        self.assertRaises(
            exceptions.InvalidInstallTypeException, betterdiscordpy.getLinuxConfigDir,
            "I don't exist",
        )
        self.assertEqual(
            betterdiscordpy.TRADITIONAL_LINUX_CONFIG_DIR,
            betterdiscordpy.getLinuxConfigDir("traditional"),
        )

        os.environ["SNAP_USER_DATA"] = "dummy"
        self.assertEqual(
            os.path.join("dummy", "discord", ".config"),
            betterdiscordpy.getLinuxConfigDir("snap"),
        )
        os.environ["SNAP_USER_DATA"] = ""

        # TODO test flatpak one


if __name__ == '__main__':
    unittest.main()
