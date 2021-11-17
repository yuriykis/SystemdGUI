from enum import Enum


class ServiceAction(Enum):
    SERVICE_START_OK = 1
    SERVICE_START_FAILED = 2
    SERVICE_RESTART_OK = 3
    SERVICE_RESTART_FAILED = 4
    SERVICE_STOP_OK = 5
    SERVICE_STOP_FAILED = 6
    SERVICE_NONE_ACTION = 7
    SERVICE_ENABLE_OK = 8
    SERVICE_ENABLE_FAILED = 9
