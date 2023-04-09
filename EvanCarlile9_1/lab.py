class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    volume_memory = 0

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__volume = Television.volume_memory
                self.__muted = False
            else:
                Television.volume_memory = self.__volume
                self.__volume = 0
                self.__muted = True

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__muted:
            self.mute()
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__muted:
            self.mute()
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        return f'TV status: Power = {self.__status}, Channel = {self.__channel},' \
               f' Volume = {self.__volume}'

