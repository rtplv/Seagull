import os
from xmlrpc.client import ServerProxy


class SvService:
    _server = ServerProxy(os.getenv('SUPERVISOR_RPC_HOST'))

    def get_version(self) -> str:
        """
        Supervisor version
        :return: str
        """
        return self._server.supervisor.getSupervisorVersion()

    def get_state(self) -> dict:
        """
        Supervisor main process state
        :return: dict
        """
        return self._server.supervisor.getState()

    def read_main_log_tail(self):
        return self._server.supervisor.readLog(-16384, 0)

    def clear_main_log(self):
        return self._server.supervisor.clearLog()

    def shutdown(self):
        return self._server.supervisor.shutdown()

    def restart(self):
        return self._server.supervisor.restart()

    def get_all_process_info(self):
        return self._server.supervisor.getAllProcessInfo()
