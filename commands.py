import argparse
import logging


def __initialLog(command_name: str, arguments: argparse.Namespace) -> None:
    logging.log(logging.DEBUG, f"Running command: {command_name}")
    logging.log(logging.DEBUG, f"Received args: {arguments}")


def status(arguments: argparse.Namespace) -> None:
    __initialLog(command_name="status", arguments=arguments)


def install(arguments: argparse.Namespace) -> None:
    __initialLog(command_name="install", arguments=arguments)


def reinstall(arguments: argparse.Namespace) -> None:
    __initialLog(command_name="reinstall", arguments=arguments)


def uninstall(arguments: argparse.Namespace) -> None:
    __initialLog(command_name="uninstall", arguments=arguments)


def selfUpgrade(arguments: argparse.Namespace) -> None:
    __initialLog(command_name="self-upgrade", arguments=arguments)


AVAILABLE_COMMANDS: dict[str, callable] = {
    "status": status,
    "install": install,
    "reinstall": reinstall,
    "uninstall": uninstall,
    "self-upgrade": selfUpgrade,
}
