import os
import signal

import daemon.runner
import lockfile


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
DEFAULT_PID_PATHNAME = os.path.join(DATA_DIR, 'pigule.pid')


def daemonize(app):
    def _stop_daemon(signum, frame):
        app.stop()

    def _execute():
        try:
            daemon_runner.do_action()
        except (lockfile.LockTimeout, daemon.runner.DaemonRunnerStartFailureError):
            sys.stderr.write('ERROR: Daemon seems already running!\n')
        except daemon.runner.DaemonRunnerStopFailureError:
            sys.stderr.write('ERROR: Daemon is not running!\n')

    # Set variables required by DaemonRunner
    app.stdin_path = '/dev/null'
    app.stdout_path = '/dev/tty'
    app.stderr_path = '/dev/tty'
    app.pidfile_path = DEFAULT_PID_PATHNAME
    app.pidfile_timeout = 5

    app.stop_daemon = _stop_daemon

    daemon_runner = daemon.runner.DaemonRunner(app)
    daemon_runner.daemon_context.signal_map = {
        signal.SIGTERM: _stop_daemon,
        signal.SIGINT: _stop_daemon
    }

    daemon_runner.execute = _execute

    return daemon_runner
