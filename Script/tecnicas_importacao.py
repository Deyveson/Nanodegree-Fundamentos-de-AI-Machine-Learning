from collections import defaultdict, namedtuple

# import multiprocessing as mp
# importando o modulo completo

import matplotlib.pyplot as plt

from multiprocessing import cpu_count as multcpu
# importando um metodo especifico e renomeando

print(multcpu())

defaultdict()

import pytz
from datetime import datetime

utc = pytz.utc
ist = pytz.timezone('America/Sao_Paulo')

now = datetime.now(tz=utc)
#  salva o tempo atual UTC,

ist_now = now.astimezone(ist)
# ele traduz o tempo em IST, para o horario da america e armazena

print(now)
print(ist_now)

