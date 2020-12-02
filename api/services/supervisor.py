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
        info = self._server.supervisor.getAllProcessInfo()

        for proc in info:
            proc['state'] = SvService.humanize_process_state(proc['statename'])

        return info

    def start_process(self, name, wait=False):
        return self._server.supervisor.startProcess(name, wait)

    def stop_process(self, name, wait=False):
        return self._server.supervisor.stopProcess(name, wait)

    @staticmethod
    def humanize_process_state(state):
        base_state = {
            'name': state
        }

        if state == 'STARTING':
            return {
                **base_state,
                'color': 'yellow',
                'title': 'Запускается'
            }
        elif state == 'RUNNING':
            return {
                **base_state,
                'color': 'green',
                'title': 'Запущено'
            }
        elif state == 'STOPPED':
            return {
                **base_state,
                'color': 'yellow',
                'title': 'Остановлено'
            }
        elif state == 'EXITED':
            return {
                **base_state,
                'color': 'yellow',
                'title': 'Завершено',
                'description': 'Процесс завершился (ожидаемо или нет)'
            }
        elif state == 'BACKOFF':
            return {
                **base_state,
                'color': 'red',
                'title': 'Остановлено до запуска',
                'description': 'Процесс завершился слишком быстро, не успев перейти в состояние "Запущено"'
            }
        elif state == 'FATAL':
            return {
                **base_state,
                'color': 'red',
                'title': 'Ошибка при запуске',
                'description': 'В процессе запуска произошла ошибка'
            }
        elif state == 'UNKNOWN':
            return {
                **base_state,
                'color': 'red',
                'title': 'Неизвестно',
                'description': 'Неизвестный статус (ошибка supervisord)'
            }