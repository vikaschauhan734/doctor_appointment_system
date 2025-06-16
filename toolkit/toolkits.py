import pandas as pd
from typing import Literal
from langchain_core.tools import tool
from data_models.models import *

@tool
def check_availability_by_doctor():
    pass

@tool
def check_availability_by_specialization():
    pass

@tool
def set_appointment():
    pass

@tool
def cancel_appointment():
    pass

@tool
def reschedule_appointment():
    pass