from telethon import *
from telethon.errors import PhoneCodeInvalidError
from telethon.errors import PhoneCodeEmptyError
from telethon.errors import ApiIdInvalidError
from telethon.errors import AboutTooLongError
from telethon.errors import TimeoutError
from telethon.errors import FirstNameInvalidError
from telethon.errors import UsernameOccupiedError
from telethon.errors import UsernameNotModifiedError
from telethon.errors import UsernameInvalidError
from telethon.errors import FilePartsInvalidError
from telethon.errors import PhotoCropSizeSmallError
from telethon.errors import PhotoExtInvalidError
from telethon.errors import VideoFileInvalidError
from telethon.errors import ImageProcessFailedError
from telethon.errors import AlbumPhotosTooManyError
from telethon.errors import AuthKeyDuplicatedError
from telethon.errors import BotDomainInvalidError
from telethon.errors import ButtonDataInvalidError
from telethon.errors import NotFoundError
from telethon.errors import ButtonTypeInvalidError
from telethon.errors import ChatAdminRequiredError
from telethon.errors import ChannelPrivateError
from telethon.errors import ChannelInvalidError
from telethon.errors import ButtonUrlInvalidError
from telethon.errors import EntitiesTooLongError
from telethon.errors import ChatWriteForbiddenError
from telethon.errors import ChatIdInvalidError
from telethon.errors import ChatRestrictedError
from telethon.errors import MessageEmptyError
from telethon.errors import InputUserDeactivatedError
from telethon.errors import EntityMentionUserInvalidError
from telethon.errors import ChatWriteForbiddenError
from telethon.errors import PollOptionInvalidError
from telethon.errors import PeerIdInvalidError
from telethon.errors import MsgIdInvalidError
from telethon.errors import MessageTooLongError
from telethon.errors import ScheduleBotNotAllowedError
from telethon.errors import ScheduleDateTooLateError
from telethon.errors import ScheduleStatusPrivateError
from telethon.errors import UserIsBlockedError
from telethon.errors import YouBlockedUserError
from telethon.errors import UserBannedInChannelError
from telethon.errors import UserIsBotError
from telethon.errors import TimeoutError
from telethon.errors import ScheduleTooMuchError
from telethon.errors import ReplyMarkupInvalidError
from telethon.errors import RandomIdDuplicateError
from telethon.errors import ReplyMarkupTooLongError
from telethon.errors import ForbiddenError
from sqlite3 import OperationalError
from telethon.errors import AccessTokenExpiredError
from telethon.errors import AccessTokenInvalidError
from telethon.errors import PhoneCodeExpiredError
from telethon.errors import PhoneNumberInvalidError
from telethon.errors import PhoneNumberUnoccupiedError
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateUsernameRequest
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                      level=logging.WARNING)
import time,os,random,csv,sys
from requests.exceptions import ConnectionError
clear = lambda:os.system('clear')
r = '\033[1;31;40m'
g = '\033[1;32;40m'
b = '\033[1;34;40m'
y = '\033[1;33;40m'
def space():
   print("\n")
space()
def femi():
    print("""
  \033[1;33;40m    .           ......     ..                 ..
     . .       ...      ...  ..                 ..
  . .  . .    ..         ..  ..       .....     ..
. .      . .  ..         ..  ....... ..   ..    ..
\033[1;32;40m..        ..  ...       ...  ..      ..   ..    ..
..        ..   ...     ...   ..      .......    ..
..        ..    .........    ....... .......... ......

  \033[1;31;40m                            telegram attack
                              version 1.0                             
         \033[0;34;47m telegram @vedalogic for more info \033[0;37;48m""")

def femi():
 #  print("""
#\033[1;33;40m    **   ******  *     *  ****** ****** *    * **
#\033[1;32;40m   ****  *    *  *  *  *  ****** ****** **  ** **
#\033[1;32;40m  **  ** *    *  * * * *  **     ****** * ** * **
#\033[1;33;40m  **  ** ******  *     *  **     ****** *    * **
   ba = ("""
..ddddd...........ffffffffff...bbbbbbbb...ggggggggg
..ddd.ddd.........ff...........bbbbbbbb...gg.......
..ddd...ddd.......ff...........bb.........gg.......
..ddd.....ddd.....ffffffffff...bb.........gg...gggg
..ddf.......dd....ff...........bbbbbbbb...gg.....gg
..ddddddddddddd...ff...........bbbbbbbɓ...ggggggggg
""")
   r = '\033[1;31;40m'
   g = '\033[1;32;40m'
   b = '\033[1;34;40m'
   y = '\033[1;33;40m'


   ba = ba.replace(".","."+r)
   ba = ba.replace("d","d"+g)
   ba = ba.replace("f","f"+y)
   ba = ba.replace("b","b"+b)
   ba = ba.replace("g","g"+g)


   print(ba)

   print("""\033[1;31;40m                            telegram attack
                                version 1.0
          \033[0;34;47m telegram @devfemibadmus for more info \033[0;37;48m 
           follow @devfemibadmusgallery for hot tools""")
def option():
    print("""
  \033[1;33;40m [0]\033[1;32;40m show My_chat              \033[1;33;40m [5]\033[1;32;40m edit fist_name

  \033[1;33;40m [1]\033[1;32;40m send message              \033[1;33;40m [6]\033[1;32;40m edit last_name

  \033[1;33;40m [2]\033[1;32;40m see contacts              \033[1;33;40m [7]\033[1;32;40m edit user_name

  \033[1;33;40m [3]\033[1;32;40m share  files              \033[1;33;40m [8]\033[1;32;40m edit user_pics

  \033[1;33;40m [4]\033[1;32;40m show profile              \033[1;33;40m [9]\033[1;32;40m exist sessions

  \033[1;33;40m [a]\033[1;32;40m clear history             \033[1;33;40m [b]\033[1;32;40m exist

    """)
clear()
femi()
print(" ")
api_id = input(b+"please enter api_id: ")
api_hash = input("please enter api_hash: ")
acc = input("please enter session name: ")
try:
   print(r)
   client = TelegramClient(acc, api_id, api_hash)
   client.start()
except ConnectionError:
   print(r+"either offline mode or data exhausted")
   sys.exit()
except TimeoutError:
   print(r+" ERROR TIMEOUT!!!")
   sys.exit()
except OSError:
   print(r+"sorry device so slow inconnecting try again later")
   sys.exit()
except AccessTokenExpiredError:
   print(r+"this provided token has expired try again later")
   sys.exit()
except AccessTokenInvalidError:
   print(r+"wrong token you provided check and try again later")
   sys.exit()
except ValueError:
   print(r+"api_id: int() api_hash: str() check and try again later")
   sys.exit()
except OperationalError:
   print(r+" change the session name and try again later \n you've used it too much time")
   sys.exit()
except ApiIdInvalidError:
   print(r+"wrong api_id/api_hash, check and try again later")
   sys.exit()
except PhoneNumberInvalidError:
   print(r+"wrong number try again later")
   sys.exit()
except PhoneNumberUnoccupiedError:
   print(r+"The phone number provided is not yet USED")
   sys.exit()
except PhoneCodeInvalidError:
   print(r+"wrong code try again later")
   sys.exit()
except PhoneCodeEmptyError:
   print(r+"empty code try again later")
   sys.exit()
except PhoneCodeExpiredError:
   print(r+"expired code try again later")
   sys.exit()
except SessionPasswordNeededError:
   print(r+"Two password authentification")
   sys.exit()
except errors.FloodWaitError as e:
    print(r+'Have to sleep', e.seconds, 'seconds')
    deal = input("Due to the fact of requesting too much code on this phone, "+str(e)+" seconds? (y/n): ")
    if deal=="y" or deal== "yes":
      time.sleep(e.seconds)
    else:
      sys.exit()
clear()
space()
femi()
option()

async def main():
    me = await client.get_me()
    r = '\033[1;31;40m'
    g = '\033[1;32;40m'
    b = '\033[1;34;40m'
    y = '\033[1;33;40m'
    async def man():
      async def ti():
        try:
          t = int(input(g+" How many time should i send this msg?: "+y))
          return t
        except ValueError:
          print("\033[1;31;40m You enterred rubbish check it!")
          return 2
      async def num():
        try:
          num = int(input(g+" How many file: "+y))
          return num
        except ValueError:
          print("\033[1;31;40m You enterred rubbish check it")
          return 2
      r = '\033[1;31;40m'
      g = '\033[1;32;40m'
      b = '\033[1;34;40m'
      y = '\033[1;33;40m'
      a = input("\033[1;37;40m🙏\033[1;34;40m select an option: \033[1;33;40m")
      space()
      if  a == "1":
          name = input(g+" enter recipient name: "+y)
          message = input(g+" enter message: "+y)
          t = await ti()
          print(b+" MSG SENDS DEPEND ON UR NETWORK")
          try:
           t = t+1
           for i in range(1,t):
             print(r)
             await client.send_message(name,message)
             print(b+" SENT "+y+message+b+" to "+y+name+" "+r+str(i))
          except ValueError:
            print(r+name+" is Invalid Name.")
          except AuthKeyDuplicatedError:
            print(r+" AuthKeyDuplicatedError")
          except BotDomainInvalidError:
            print(r+" BotDomainInvalidError")
          except ForbiddenError:
            print(r+" You got blocked from "+name)
          except ButtonDataInvalidError:
            print(r+" ButtonDataInvalidError")
          except ButtonTypeInvalidError:
            print(r+" ButtonTypeInvalidError")
          except ChatAdminRequiredError:
            print(r+" ChatAdminRequiredError")
          except ChannelPrivateError:
            print(r+" ChannelPrivateError")
          except ChannelInvalidError:
            print(r+" ChannelInvalidError")
          except ButtonUrlInvalidError:
            print(r+" ButtonUrlInvalidError")
          except EntitiesTooLongError:
            print(r+" EntitiesTooLongError")
          except ChatWriteForbiddenError:
            print(r+" You not allow to message "+y+name)
          except ChatIdInvalidError:
            print(r+" ChatIdInvalidError")
          except ChatRestrictedError:
            print(r+" ChatRestrictedError")
          except MessageEmptyError:
            print(r+" MessageEmptyError")
          except InputUserDeactivatedError:
            print(r+" InputUserDeactivatedError")
          except EntityMentionUserInvalidError:
            print(r+" EntityMentionUserInvalidError")
          except ChatWriteForbiddenError:
            print(r+" ChatWriteForbiddenError")
          except PollOptionInvalidError:
            print(r+" PollOptionInvalidError")
          except ValueError:
            print(r+" Invalid name"+y+name)
          except PeerIdInvalidError:
            print(r+" PeerIdInvalidError")
          except MsgIdInvalidError:
            print(r+" MsgIdInvalidError")
          except MessageTooLongError:
            print(r+" MessageTooLongError")
          except ScheduleBotNotAllowedError:
            print(r+" ScheduleBotNotAllowedError")
          except ScheduleDateTooLateError:
            print(r+" ScheduleDateTooLateError")
          except ScheduleStatusPrivateError:
            print(r+" ScheduleStatusPrivateError")
          except UserIsBlockedError:
            print(r+" UserIsBlockedError")
          except YouBlockedUserError:
            print(r+" YouBlockedUserError")
          except UserBannedInChannelError:
            print(r+" UserBannedInChannelError")
          except UserIsBotError:
            print(r+" UserIsBotError")
          except TimeoutError:
            print(r+" TimeoutError")
          except ScheduleTooMuchError:
            print(r+" ScheduleTooMuchError")
          except ReplyMarkupInvalidError:
            print(r+" ReplyMarkupInvalidError")
          except RandomIdDuplicateError:
            print(r+" RandomIdDuplicateError")
          except ReplyMarkupTooLongError:
            print(r+" ReplyMarkupTooLongError")



      elif a == "0":
         name = input(g+" enter chat user_name: "+y)
         try:
           print(r)
           async for message in client.iter_messages(name, from_user=name):
              print(r+" THIS ARE MESSAGE FROM "+y+name)
              print('\033[1;32;40m',message.id, y,message.text)
           async for message in client.iter_messages(name, from_user=name):
              print(b+" THIS ARE MESSAGE FROM "+r+"YOU")
              print('\033[1;32;40m',message.id, r,message.text)
         except ValueError:
              print(r+" No name "+y+name+r+" in"+g+" TELEGRAM")
         except ChatAdminRequiredError:
              print(r+" NEED PERMISSION TO CHAT "+y+name)

      elif a == "2":
         print(r)
         async for dialog in client.iter_dialogs():
            a = dialog.name
            b = ' '
            c =20- len(a)
            d = b*c
            e = dialog.id
            f = 20-len(str(e))
            g = b*f
         print('\033[1;32;40m',a,d, "\033[1;33;40m has id",g, "\033[1;32;40m", dialog.id)


      elif a == "3":
           name = input(g+" enter reciepeint name: "+y)
           num = await num()
           num = num+1
           try:
             for i in range (1,num):
                fiee = input(g+" enter file path: "+y)
                print(b+" FILE SENDS DEPEND ON UR NETWORK")
                print(r)
                file = await client.upload_file(fiee)
                await client.send_file(name,file)
                print(b+" Successfully sent file "+y+i+"to"+y+name)
           except TypeError:
             for i in range (1,num):
               fiee = input(g+" enter file path: "+y)
               print(b+" FILE SENDS DEPEND ON UR NETWORK")
               print(r)
               file = await client.upload_file(fiee)
               await client.send_file(name,file)
               print(y+" SENT "+g+fiee+y+" SUCCESSFULLY")
           except FileNotFoundError:
             print(r+" No such file")
             print(r+" PLEASE "+b+" chat @devfemibadmus")
           except IsADirectoryError:
             for i in range (1,num):
                fiee = input(g+" enter file path: "+y)
                print(b+" FILE SENDS DEPEND ON UR NETWORK")
                print(r)
                file = await client.upload_file(fiee)
                await client.send_file(name,file)
                print(y+"SENT DIRECTORY "+g+fiee+y+" SUCCESSFULLY")


      elif a == "4":
           print(r)
           print(b+me.stringify())



      elif   a == "5" or a == "6":
             f  = input(g+" enter first_name: "+y)
             l  = input(g+" enter last_name: "+y)
             ab = input(g+" enter about: "+y)
             try:
               print(r)
               await client(UpdateProfileRequest(
                       about=ab,
                       first_name=f,
                       last_name=l
               ))
               print(g+" Done! Check it out!!")
             except AboutTooLongError:
                print(r+" UR ABOUT IS TOO LONG")
             except FirstNameInvalidError:
                print(r+" THE FIRST_NAME U PROVIDED IS INVALID")


      elif   a == "7":
             u = input(g+" enter NewUserName: "+y)
             try:
               print(r)
               await client(UpdateUsernameRequest(u))
               print(g+" Done! Check it out!!")
             except UsernameOccupiedError:
               print(r+" User_name taken already")
             except UsernameNotModifiedError:
               print(r+" The username is not different from the current username.")
             except UsernameInvalidError:
               print(r+" The username is unacceptable. \n too small/big")


      elif   a == "8":
             p = input(g+" enter image path: "+y)

             try:
               print(r)
               await client(UploadProfilePhotoRequest(
               await client.upload_file(p)
               ))
               print(g+" Done! Check it out!!")
             except AlbumPhotosTooManyError:
               print(r+" Too many photos were included in the album.")
             except FilePartsInvalidError:
               print(r+" The number of file parts is invalid.")
             except ImageProcessFailedError:
               print(r+"        Failure while processing image.")
             except PhotoCropSizeSmallError:
               print(r+" Image too small")
             except PhotoExtInvalidError:
               print(r+" The extension of the photo is invalid.")
             except VideoFileInvalidError:
               print(r+" The given video cannot be used.")
             except FileNotFoundError:
               print(r+" No such file")
               print(r+" PLEASE "+b+" chat @devfemibadmus")
             except TypeError:
               print(" "+r+p+" consist of invalid value check and try again later!")
             except IsADirectoryError:
               print(" "+r+p+" is a Directory")

      elif a == "9":
           await client.log_out()
           print(r+"YOU LOG_OUT "+y+acc+g+" Account!")
           sys.exit()

      elif a == "b":
           print(r+"    YOU EXIST \n         BYE!")
           sys.exit()

      elif a == "a":
           print(r)
           clear()
           space()
           femi()
           option()
      else:
           print(r+" YOU ENTERRED INVALID OPTION")
           print(r+" PLEASE "+b+" chat @devfemibadmus")

    while True:
       await man()
       space()

with client:
    client.loop.run_until_complete(main())


client.start()
client.run_until_disconnected()
