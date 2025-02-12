class ActorType(object):
    Null = 0
    Player = 1
    BattleNpc = 2
    EventNpc = 3
    Treasure = 4
    Aetheryte = 5
    GatheringPoint = 6
    EventObj = 7
    MountType = 8
    Companion = 9  # minion
    Retainer = 10
    Area = 11
    Housing = 12
    Cutscene = 13
    CardStand = 14


class JobClass(object):
    Paladin = 19  # 骑士PLD
    Monk = 20  # 武僧MNK
    Warrior = 21  # 战士WAR
    Dragoon = 22  # 龙骑士DRG
    Bard = 23  # 吟游诗人BRD
    WhiteMage = 24  # 白魔法师WHM
    BlackMage = 25  # 黑魔法师BLM
    Arcanist = 26  # 秘术师ACN
    Summoner = 27  # 召唤师SMN
    Scholar = 28  # 学者SCH
    Ninja = 30  # 忍者NIN
    Machinist = 31  # 机工士MCH
    DarkKnight = 32  # 暗黑骑士DRK
    Astrologian = 33  # 占星术士AST
    Samurai = 34  # 武士SAM
    RedMage = 35  # 赤魔法师RDM
    Gunbreaker = 37  # 绝枪战士GNB
    Dancer = 38  # 舞者DNC


class ChatType(object):
    none = 0
    Debug = 1
    Urgent = 2
    Notice = 3
    Say = 10
    Shout = 11
    TellOutgoing = 12
    TellIncoming = 13
    Party = 14
    Alliance = 15
    Linkshell1 = 16
    Linkshell2 = 17
    Linkshell3 = 18
    Linkshell4 = 19
    Linkshell5 = 20
    Linkshell6 = 21
    Linkshell7 = 22
    Linkshell8 = 23
    FreeCompany = 24
    NoviceNetwork = 27
    CustomEmote = 28
    StandardEmote = 29
    Yell = 30
    CrossParty = 32
    PvPTeam = 36
    CrossLinkShell1 = 37
    Echo = 56
    SystemError = 58
    SystemMessage = 57
    GatheringSystemMessage = 59
    ErrorMessage = 60
    RetainerSale = 71
    CrossLinkShell2 = 101
    CrossLinkShell3 = 102
    CrossLinkShell4 = 103
    CrossLinkShell5 = 104
    CrossLinkShell6 = 105
    CrossLinkShell7 = 106
    CrossLinkShell8 = 107
