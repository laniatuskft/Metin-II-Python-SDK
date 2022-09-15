## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define NEED_TARGET (1 << 0)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define NEED_PC (1 << 1)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define WOMAN_ONLY (1 << 2)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define OTHER_SEX_ONLY (1 << 3)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define SELF_DISARM (1 << 4)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define TARGET_DISARM (1 << 5)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define IGNORE_BLOCK (1 << 6)
## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define BOTH_DISARM (SELF_DISARM | TARGET_DISARM)

class emotion_type_s:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.command = '\0'
        self.command_to_client = '\0'
        self.flag = 0
        self.extra_delay = 0
