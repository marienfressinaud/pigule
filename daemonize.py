import sys
import os
import signal

import daemon.runner
import lockfile


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
DEFAULT_PID_PATHNAME = os.path.join(DATA_DIR, 'pigule.pid')


class AppDaemon:
    def __init__(self, app_class):
        self.app_class = app_class

        # Set variables required by DaemonRunner
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = DEFAULT_PID_PATHNAME
        self.pidfile_timeout = 5

    def run(self):
        self.app = self.app_class()
        self.app.run()

    def stop(self, signum, frame):
        self.app.stop()


def daemonize(app_class):
    def _execute():
        try:
            daemon_runner.do_action()
        except (lockfile.LockTimeout, daemon.runner.DaemonRunnerStartFailureError):
            sys.stderr.write('ERROR: Daemon seems already running!\n')
        except daemon.runner.DaemonRunnerStopFailureError:
            sys.stderr.write('ERROR: Daemon is not running!\n')

    app_daemon = AppDaemon(app_class)

    daemon_runner = daemon.runner.DaemonRunner(app_daemon)
    daemon_runner.daemon_context.signal_map = {
        signal.SIGTERM: app_daemon.stop,
        signal.SIGINT: app_daemon.stop
    }

    daemon_runner.execute = _execute

    return daemon_runner
