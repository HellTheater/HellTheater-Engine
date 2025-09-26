from .observer import Observer
from .content_injector import ContentInjector
from .stealth_operator import StealthOperator

class StrategyEngine:
    def __init__(self, level):
        self.level = level

    def execute(self, context):
        if self.level == 1:
            return Observer().analyze(context)
        elif self.level == 2:
            return ContentInjector().generate_and_schedule(context)
        elif self.level == 3:
            return StealthOperator().deploy(context)
