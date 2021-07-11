from random import randint

from config.settings import AUTHOR, VERSION


cat = """\r\n
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  version: {0}
                          author : {1}
""".format(VERSION, AUTHOR)


cat2 = """\r\n
      \    /\
       )  ( ')
      (  /  )
       \(__)|     version : {0}
                  author  : {1}
""".format(VERSION, AUTHOR)

car = """\r\n
            version {0}
            author  {1}
|^^^^^^^^^^^\||____
| The STFU Truck |||""'|""\__,_
| _____________ l||__|__|__|)
...|(@)@)"""""""**|(@)(@)**|(@)
""".format(VERSION, AUTHOR)


LOGOS = [car, cat, cat2]


def show_banner():
    return LOGOS[randint(0, 1)]
