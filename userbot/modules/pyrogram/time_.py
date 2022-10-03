# 

from userbot._func.decorators import Nande_cmd as sipuserbot_on_cmd
from userbot._func._helpers import edit_or_reply
import calendar
from datetime import datetime

from . import HELP


HELP(
    "time_",
)

@sipuserbot_on_cmd(['time'],
               cmd_help={
                   "help": "Check Current Date , Time & Calender.",
                   "example": "{ch}time"
              }
)
async def _d(client, message):
    year_ = datetime.now().year
    datetime.now().day
    month_ = datetime.now().month
    mydate = datetime.now()
    da = mydate.strftime("Date : %d \nMonth : %B \nYear : %Y")
    dt = mydate.strftime("Hour : %H \nMinute : %M")
    cal_ = calendar.month(year_, month_)
    f_d = f"<code>{cal_}\n{da} \n\n{dt}</code>"
    await edit_or_reply(message, f_d, parse_mode="html")
