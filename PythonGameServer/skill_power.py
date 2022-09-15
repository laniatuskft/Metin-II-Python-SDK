class CTableBySkill(singleton):
    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_aiSkillPowerByLevelFromType = [None]
        self._m_aiSkillDamageByLevel = []

        self._m_aiSkillDamageByLevel = None
        job = 0
        while job < EJobs.JOB_MAX_NUM * 2:
            self._m_aiSkillPowerByLevelFromType[job] = None
            job += 1

    def close(self):
        self.DeleteAll()
## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: bool Check() const
    def Check(self):
        job = 0
        while job < (EJobs.JOB_MAX_NUM * 2):
            if self._m_aiSkillPowerByLevelFromType[job] == 0:
                fprintf(stderr, "[NO SETTING SKILL] aiSkillPowerByLevelFromType[%d]", job)
                return LGEMiscellaneous.DEFINECONSTANTS.false
            job += 1

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def DeleteAll(self):
        job = 0
        while job < EJobs.JOB_MAX_NUM * 2:
            self.DeleteSkillPowerByLevelFromType(job)
            job += 1

        self.DeleteSkillDamageByLevelTable()

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetSkillPowerByLevelFromType(int job, int skillgroup, int skilllevel, bool bMob) const
    def GetSkillPowerByLevelFromType(self, job, skillgroup, skilllevel, bMob):
        if bMob:
            return self._m_aiSkillPowerByLevelFromType[0][skilllevel]

        if job >= EJobs.JOB_MAX_NUM or skillgroup == 0:
            return 0

        idx = (job * 2) + (skillgroup - 1)

        return self._m_aiSkillPowerByLevelFromType[idx][skilllevel]

    def SetSkillPowerByLevelFromType(self, idx, aTable):
        self.DeleteSkillPowerByLevelFromType(idx)

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int* aiSkillTable = LG_NEW_M2 int[LG_SKILL_MAX_LEVEL+1];
        aiSkillTable = LG_NEW_M2 int[(int)LGEMiscellaneous.LG_SKILL_MAX_LEVEL+1]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(aiSkillTable, aTable, sizeof(int) * (LGEMiscellaneous.LG_SKILL_MAX_LEVEL + 1))
        self._m_aiSkillPowerByLevelFromType[idx] = aiSkillTable

    def DeleteSkillPowerByLevelFromType(self, idx):
        if None != self._m_aiSkillPowerByLevelFromType[idx]:
            LG_DEL_MEM_ARRAY(self._m_aiSkillPowerByLevelFromType[idx])
            self._m_aiSkillPowerByLevelFromType[idx] = None

## Laniatus Games Studio Inc. | WARNING: 'const' methods are not available in Python:
#ORIGINAL METINII C CODE: int GetSkillDamageByLevel(int Level) const
    def GetSkillDamageByLevel(self, Level):
        if Level < 0 or Level >= LGEMiscellaneous.PLAYER_MAX_LEVEL_CONST:
            return 0

        return self._m_aiSkillDamageByLevel[Level]

    def SetSkillDamageByLevelTable(self, aTable):
        self.DeleteSkillDamageByLevelTable()

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to pointers to value types:
#ORIGINAL METINII C CODE: int* aiSkillDamageTable = LG_NEW_M2 int[PLAYER_MAX_LEVEL_CONST];
        aiSkillDamageTable = LG_NEW_M2 int[(int)LGEMiscellaneous.PLAYER_MAX_LEVEL_CONST]

## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: The memory management function 'memcpy' has no equivalent in Python: For corresponding functionality, review the attachment in the email content distributed to the Laniatus teams.
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: There is no Python equivalent to 'sizeof':
        memcpy(aiSkillDamageTable, aTable, sizeof(int) * (LGEMiscellaneous.PLAYER_MAX_LEVEL_CONST))

        self._m_aiSkillDamageByLevel = aiSkillDamageTable

    def DeleteSkillDamageByLevelTable(self):
        if None != self._m_aiSkillDamageByLevel:
            LG_DEL_MEM_ARRAY(self._m_aiSkillDamageByLevel)
            self._m_aiSkillDamageByLevel = None


