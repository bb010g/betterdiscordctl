import argparse
import logging
import unittest

import commands


class CommandsTest(unittest.TestCase):
    def validateLogMessage(self, log: str, level: str, message: str) -> None:
        self.assertIn(level, log)
        self.assertIn(message, log)

    def testStatusCommand(self) -> None:
        dummy_args = argparse.Namespace(verbose=True)
        expected_logs_amount = 2

        with self.assertLogs(level=logging.DEBUG) as logger:
            commands.status(dummy_args)
            output = logger.output
            self.assertEqual(expected_logs_amount, len(output))
            self.validateLogMessage(log=output[0], level="DEBUG", message="Running command: status")
            self.validateLogMessage(
                log=output[1], level="DEBUG",
                message="Received args: Namespace(verbose=True)",
            )

    def testInstallCommand(self) -> None:
        dummy_args = argparse.Namespace(verbose=True, d_install="flatpak")
        expected_logs_amount = 2

        with self.assertLogs(level=logging.DEBUG) as logger:
            commands.install(dummy_args)
            output = logger.output
            self.assertEqual(expected_logs_amount, len(output))
            self.validateLogMessage(
                log=output[0], level="DEBUG",
                message="Running command: install",
            )
            self.validateLogMessage(
                log=output[1], level="DEBUG",
                message="Received args: Namespace(verbose=True, d_install='flatpak')",
            )

    def testReinstallCommand(self) -> None:
        dummy_args = argparse.Namespace(verbose=True)
        expected_logs_amount = 2

        with self.assertLogs(level=logging.DEBUG) as logger:
            commands.reinstall(dummy_args)
            output = logger.output
            self.assertEqual(expected_logs_amount, len(output))
            self.validateLogMessage(
                log=output[0], level="DEBUG",
                message="Running command: reinstall",
            )
            self.validateLogMessage(
                log=output[1], level="DEBUG",
                message="Received args: Namespace(verbose=True)",
            )

    def testUninstallCommand(self) -> None:
        dummy_args = argparse.Namespace(verbose=True)
        expected_logs_amount = 2

        with self.assertLogs(level=logging.DEBUG) as logger:
            commands.uninstall(dummy_args)
            output = logger.output
            self.assertEqual(expected_logs_amount, len(output))
            self.validateLogMessage(
                log=output[0], level="DEBUG",
                message="Running command: uninstall",
            )
            self.validateLogMessage(
                log=output[1], level="DEBUG",
                message="Received args: Namespace(verbose=True)",
            )

    def testSelfUpgradeCommand(self) -> None:
        dummy_args = argparse.Namespace(verbose=True)
        expected_logs_amount = 2

        with self.assertLogs(level=logging.DEBUG) as logger:
            commands.selfUpgrade(dummy_args)
            output = logger.output
            self.assertEqual(expected_logs_amount, len(output))
            self.validateLogMessage(
                log=output[0], level="DEBUG",
                message="Running command: self-upgrade",
            )
            self.validateLogMessage(
                log=output[1], level="DEBUG",
                message="Received args: Namespace(verbose=True)",
            )


if __name__ == '__main__':
    unittest.main()
