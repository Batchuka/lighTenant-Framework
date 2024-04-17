# pytrobot/__init__.py

# API para o desenvolvedor implementar
from pytrobot.core import PyTRobot, State, First, BaseState, TransactionData
from pytrobot.debug import debug_entrypoint as debug
from pytrobot.debug import auto_import_states as auto_import

# Definição dos elementos da API que serão publicamente acessíveis ao importar 'pytrobot'
__all__ = ['PyTRobot', 'State', 'First', 'BaseState', 'TransactionData', 'debug', 'auto_import']

# Versão do pacote
__version__ = '3.1.0'